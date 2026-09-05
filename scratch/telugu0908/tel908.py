"""
Shared toolkit for reverse-engineering the Shree-Tel-0908 legacy Telugu encoding.

Why this exists
---------------
Shree-Tel-0908 has no GSUB/GPOS/kern. A browser renders it as "look each character up in
the (3,1) Unicode cmap, draw the glyph, advance by hmtx". That is fully reproducible
offline, so we can render exactly what a user will see without a browser or HarfBuzz.

Two coordinate systems, do not mix them up:
  * "byte"  - the font's (1,0) cmap. What Windows apps send. NOT what we emit.
  * "plat3" - the font's (3,1) cmap. What a browser looks up, so what the converter
              must put in its output strings. All repo tables are in plat3. So are we.

Run with /usr/bin/python3 (has fontTools + Pillow). The repo venv has no Pillow.
"""
import json
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen

LEGACY = 'public/SHREE-TEL.ttf'
NOTO_SANS = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'
NOTO_SERIF = '/usr/share/fonts/noto/NotoSerifTelugu-Regular.ttf'
TALAKATTU = 0xE6  # plat3; adv 40, bbox (-104,320)-(196,503) -> draws back over the base


# ---------------------------------------------------------------- outlines

def _flatten(rec, steps=12):
    """RecordingPen value -> list of closed contours [(x,y), ...], curves polygonised."""
    contours, cur = [], []

    def quad(p0, p1, p2):
        for i in range(1, steps + 1):
            t = i / steps
            mt = 1 - t
            cur.append((mt * mt * p0[0] + 2 * mt * t * p1[0] + t * t * p2[0],
                        mt * mt * p0[1] + 2 * mt * t * p1[1] + t * t * p2[1]))

    def cubic(p0, c1, c2, p3):
        for i in range(1, steps + 1):
            t = i / steps
            mt = 1 - t
            cur.append((mt**3 * p0[0] + 3 * mt * mt * t * c1[0] + 3 * mt * t * t * c2[0] + t**3 * p3[0],
                        mt**3 * p0[1] + 3 * mt * mt * t * c1[1] + 3 * mt * t * t * c2[1] + t**3 * p3[1]))

    for op, args in rec:
        if op == 'moveTo':
            if cur:
                contours.append(cur[:]); cur.clear()
            cur.append(tuple(args[0]))
        elif op == 'lineTo':
            cur.append(tuple(args[0]))
        elif op == 'qCurveTo':
            pts = [tuple(a) if a is not None else None for a in args]
            if pts[-1] is None:                       # all off-curve, closed (TT circle)
                offs = pts[:-1]
                if not cur:
                    cur.append(((offs[0][0] + offs[-1][0]) / 2, (offs[0][1] + offs[-1][1]) / 2))
                for i, c in enumerate(offs):
                    nx = offs[(i + 1) % len(offs)]
                    quad(cur[-1], c, ((c[0] + nx[0]) / 2, (c[1] + nx[1]) / 2))
            else:
                offs, end = pts[:-1], pts[-1]
                for i, c in enumerate(offs):
                    e = end if i == len(offs) - 1 else ((c[0] + offs[i + 1][0]) / 2,
                                                       (c[1] + offs[i + 1][1]) / 2)
                    quad(cur[-1], c, e)
        elif op == 'curveTo':
            pts = [tuple(a) for a in args]
            if len(pts) == 3:
                cubic(cur[-1], pts[0], pts[1], pts[2])
            else:
                cur.extend(pts)
        elif op in ('closePath', 'endPath'):
            if cur:
                contours.append(cur[:]); cur.clear()
    if cur:
        contours.append(cur[:])
    return contours


class Face:
    """A font, addressed by plat3 codepoint."""

    def __init__(self, path):
        self.path = path
        self.tt = TTFont(path, lazy=True)
        self.gs = self.tt.getGlyphSet()
        self.hmtx = self.tt['hmtx']
        self.glyf = self.tt['glyf'] if 'glyf' in self.tt else None
        self.upem = self.tt['head'].unitsPerEm
        self.plat3, self.plat1 = {}, {}
        for t in self.tt['cmap'].tables:
            if t.platformID == 3:
                self.plat3.update(t.cmap)
            elif t.platformID == 1:
                self.plat1.update(t.cmap)
        # plat3 codepoint -> font byte, via shared glyph name
        g2b = {}
        for b, gn in sorted(self.plat1.items()):
            g2b.setdefault(gn, b)
        self.byte_of = {cp: g2b.get(gn) for cp, gn in self.plat3.items()}
        self._cache = {}

    def has(self, cp):
        return cp in self.plat3

    def metrics(self, cp):
        gn = self.plat3[cp]
        adv = self.hmtx[gn][0]
        g = self.glyf[gn] if self.glyf and gn in self.glyf.glyphs else None
        nc = getattr(g, 'numberOfContours', 0)
        try:
            bbox = (g.xMin, g.yMin, g.xMax, g.yMax)
        except Exception:
            bbox = None
        return {'glyph': gn, 'adv': adv, 'contours': nc, 'bbox': bbox,
                'byte': self.byte_of.get(cp)}

    def contours(self, cp):
        if cp not in self._cache:
            pen = RecordingPen()
            self.gs[self.plat3[cp]].draw(pen)
            self._cache[cp] = _flatten(pen.value)
        return self._cache[cp]

    def layout(self, text):
        """Compose plat3 characters on advance widths. Returns (contours, union_bbox, pen_end)."""
        out, x = [], 0
        for ch in text:
            cp = ord(ch)
            if cp not in self.plat3:
                x += self.upem // 3
                continue
            for c in self.contours(cp):
                out.append([(px + x, py) for px, py in c])
            x += self.hmtx[self.plat3[cp]][0]
        if not out:
            return [], None, x
        xs = [p[0] for c in out for p in c]
        ys = [p[1] for c in out for p in c]
        return out, (min(xs), min(ys), max(xs), max(ys)), x


# ---------------------------------------------------------------- rasterising

def rasterize(contours, box, W, H, ss=3):
    """Nonzero-winding scanline fill -> PIL 'L' image (255 = ink), antialiased by ss.

    Nonzero rather than even-odd on purpose: TrueType is nonzero, and even-odd produces
    spurious full-width bands on glyphs whose contours overlap in the same direction.
    """
    from PIL import Image
    x0, y0, x1, y1 = box
    if x1 <= x0 or y1 <= y0:
        return Image.new('L', (max(W, 1), max(H, 1)), 0)
    sw, sh = W * ss, H * ss
    sx, sy = (x1 - x0) / sw, (y1 - y0) / sh
    buf = bytearray(sw * sh)
    edges = []
    for c in contours:
        n = len(c)
        for i in range(n):
            ax, ay = c[i]
            bx, by = c[(i + 1) % n]
            if ay != by:
                edges.append((ax, ay, bx, by))
    for r in range(sh):
        yc = y1 - (r + 0.5) * sy
        xs = []
        for ax, ay, bx, by in edges:
            if (ay <= yc < by) or (by <= yc < ay):
                xs.append((ax + (yc - ay) / (by - ay) * (bx - ax), 1 if by > ay else -1))
        if not xs:
            continue
        xs.sort()
        wind = 0
        row = r * sw
        for i in range(len(xs) - 1):
            wind += xs[i][1]
            if wind != 0:
                ca = int((xs[i][0] - x0) / sx)
                cb = int((xs[i + 1][0] - x0) / sx)
                if cb < ca:
                    ca, cb = cb, ca
                for cc in range(max(0, ca), min(sw, cb + 1)):
                    buf[row + cc] = 255
    img = Image.frombytes('L', (sw, sh), bytes(buf))
    return img.resize((W, H), Image.LANCZOS) if ss > 1 else img


def render(face, text, height=64, pad_em=0.10, ss=3):
    """Render plat3 `text` with `face` at ~`height` px of ink. Returns PIL 'L' or None."""
    contours, box, _ = face.layout(text)
    if box is None:
        return None
    pad = face.upem * pad_em
    box = (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad)
    bw, bh = box[2] - box[0], box[3] - box[1]
    H = height
    W = max(4, int(round(H * bw / bh)))
    return rasterize(contours, box, W, H, ss)


def render_unicode(face, text, height=64, pad_em=0.10, ss=3):
    """Same, but `text` is real Unicode looked up in a Unicode font's cmap.

    NOTE: no shaping. Fine for single codepoints (bare consonants, vowels, isolated
    marks); NOT valid for clusters that need GSUB reordering/ligatures - use the
    Chromium harness (verify_browser.mjs) for those.
    """
    return render(face, text, height, pad_em, ss)


def ink_mask(img, thresh=128):
    """PIL 'L' -> set of (x,y) ink pixels, tight-cropped and normalised to origin."""
    bbox = img.point(lambda v: 255 if v >= thresh else 0).getbbox()
    if bbox is None:
        return set(), (0, 0)
    crop = img.crop(bbox)
    px = crop.load()
    w, h = crop.size
    return {(x, y) for y in range(h) for x in range(w) if px[x, y] >= thresh}, (w, h)


def iou(a_img, b_img, size=64, thresh=128, jitter=2):
    """Scale-normalised bitmap IoU with a small translation search. Triage only."""
    from PIL import Image

    def norm(img):
        bbox = img.point(lambda v: 255 if v >= thresh else 0).getbbox()
        if bbox is None:
            return None
        c = img.crop(bbox)
        w, h = c.size
        s = size / max(w, h)
        nw, nh = max(1, int(round(w * s))), max(1, int(round(h * s)))
        canvas = Image.new('L', (size + 2 * jitter, size + 2 * jitter), 0)
        canvas.paste(c.resize((nw, nh), Image.LANCZOS),
                     (jitter + (size - nw) // 2, jitter + (size - nh) // 2))
        return canvas

    A, B = norm(a_img), norm(b_img)
    if A is None or B is None:
        return 0.0
    ap, bp = A.load(), B.load()
    W, H = A.size
    a = {(x, y) for y in range(H) for x in range(W) if ap[x, y] >= thresh}
    best = 0.0
    for dx in range(-jitter, jitter + 1):
        for dy in range(-jitter, jitter + 1):
            b = {(x + dx, y + dy) for y in range(H) for x in range(W) if bp[x, y] >= thresh}
            if not a and not b:
                continue
            inter = len(a & b)
            union = len(a | b)
            if union:
                best = max(best, inter / union)
    return best
