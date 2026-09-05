#!/usr/bin/env python3
"""
Labelled sheets for a human to judge. No browser, no shaping - both are unnecessary here
and the browser path (refsheet.mjs) can only render whole clusters, not numbered candidates.

    python3 scratch/telugu0908/eyeball.py alphabet          # out/alphabet.png
    python3 scratch/telugu0908/eyeball.py cand మ ఘ ష స ప ఫ  # out/cand_<letter>.png each

Every cell shows the Unicode reference (grey, Noto Serif Telugu) above the converter's
Shree-Tel output (black) for the same letter, captioned with the legacy codes and the IoU.
The only question per cell is "is the black one the same letter as the grey one".

Why a human decides: between two correct Telugu fonts this IoU scores tha-vs-dha at 0.93,
ttha-vs-ra 0.92, pa-vs-sa 0.79, pha-vs-ssa 0.69, gha-vs-ma 0.65. Every letter that shipped
wrong sits inside one of those pairs, and the top-ranked candidate is the same string for
both members. The metric ranks; it cannot decide.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))

import heads as H
import tel908 as T
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(HERE, 'out')
MONO = '/usr/share/fonts/TTF/DejaVuSansMono.ttf'
TELU = '/usr/share/fonts/noto/NotoSerifTelugu-Regular.ttf'
VARGA = 'కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలళవశషసహఱ'
LETTERS = list(VARGA) + ['క్ష']   # 36 items: what the user pasted in
GREY, INK, DIM = (120, 130, 150), (0, 0, 0), (150, 150, 150)


def ref_render(text, height=110):
    """Unicode `text` in Noto Serif Telugu, properly shaped. Pillow is built with Raqm here,
    so HarfBuzz does the layout - which tel908.render_unicode cannot, and which క్ష and any
    vowel sign need. Returns a tight-cropped 'L' mask, ink = 255."""
    size = 160
    f = ImageFont.truetype(TELU, size)
    img = Image.new('L', (size * 4, size * 3), 0)
    ImageDraw.Draw(img).text((size, size // 2), text, fill=255, font=f)
    bb = img.getbbox()
    if bb is None:
        return None
    img = img.crop(bb)
    s = height / img.size[1]
    return img.resize((max(1, round(img.size[0] * s)), height), Image.LANCZOS)


def legacy(c):
    """The exact string the shipped converter emits for the bare consonant `c`."""
    return ''.join(chr(x) for x in H.head(c))


def codes(s):
    return ' '.join(f'{ord(ch):02X}' for ch in s)


def paste(img, glyph, box, colour):
    """Fit a rendered 'L' mask into `box` (x, y, w, h), centred, tinted `colour`."""
    if glyph is None:
        return
    w, h = glyph.size
    s = min(box[2] / w, box[3] / h)
    g = glyph.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    layer = Image.new('RGB', g.size, colour)
    img.paste(layer, (box[0] + (box[2] - g.size[0]) // 2,
                      box[1] + (box[3] - g.size[1]) // 2), g)


class Sheet:
    """A grid of ref-above / output-below cells with a caption line each."""

    def __init__(self, cols, rows, title, cw=214, ch=246):
        self.cols, self.cw, self.ch = cols, cw, ch
        self.img = Image.new('RGB', (cols * cw + 2, rows * ch + 44), 'white')
        self.d = ImageDraw.Draw(self.img)
        self.f_cap = ImageFont.truetype(MONO, 15)
        self.f_sub = ImageFont.truetype(MONO, 12)
        self.f_ttl = ImageFont.truetype(MONO, 17)
        self.d.text((8, 12), title, fill=INK, font=self.f_ttl)
        self.n = 0

    def cell(self, ref, out, caption, sub):
        i = self.n
        self.n += 1
        x, y = (i % self.cols) * self.cw + 1, (i // self.cols) * self.ch + 40
        self.d.rectangle([x, y, x + self.cw - 3, y + self.ch - 3], outline=(215, 215, 215))
        self.d.text((x + 7, y + 5), caption, fill=INK, font=self.f_cap)
        self.d.text((x + 7, y + 24), sub, fill=DIM, font=self.f_sub)
        paste(self.img, ref, (x + 6, y + 42, self.cw - 15, 88), GREY)
        self.d.line([x + 18, y + 134, x + self.cw - 21, y + 134], fill=(230, 230, 230))
        paste(self.img, out, (x + 6, y + 140, self.cw - 15, 96), INK)

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.img.save(path)
        print(f'{path}  {self.img.size[0]}x{self.img.size[1]}  {self.n} cells')


# --------------------------------------------------------------------------- scoring
N, STRIDE, JIT = 64, 80, 3


def bits(img):
    if img is None:
        return None
    bb = img.point(lambda v: 255 if v >= 128 else 0).getbbox()
    if bb is None:
        return None
    c = img.crop(bb)
    w, h = c.size
    s = N / max(w, h)
    nw, nh = max(1, round(w * s)), max(1, round(h * s))
    px = c.resize((nw, nh)).load()
    ox, oy = (N - nw) // 2 + JIT, (N - nh) // 2 + JIT
    b = 0
    for yy in range(nh):
        acc = 0
        for xx in range(nw):
            if px[xx, yy] >= 128:
                acc |= 1 << (xx + ox)
        b |= acc << ((yy + oy) * STRIDE)
    return b, b.bit_count()


def iou(a, b):
    if not a or not b:
        return 0.0
    ab, an = a
    bb, _ = b
    best = 0.0
    for dy in range(-JIT, JIT + 1):
        sh = dy * STRIDE
        s1 = bb << sh if sh >= 0 else bb >> -sh
        for dx in range(-JIT, JIT + 1):
            c = s1 << dx if dx >= 0 else s1 >> -dx
            i = (ab & c).bit_count()
            if i:
                best = max(best, i / (an + c.bit_count() - i))
    return best


# --------------------------------------------------------------------------- sheets
def alphabet(shree, noto):
    sh = Sheet(6, 6, 'Shree-Tel-0908 alphabet. Grey = Unicode reference (Noto Serif '
                     'Telugu). Black = what the converter emits. Same letter or not?')
    for i, c in enumerate(LETTERS):
        s = legacy(c)
        ref = ref_render(c)
        out = T.render(shree, s, height=110)
        v = iou(bits(ref), bits(out))
        sh.cell(ref, out, f'{i + 1:>2}. {c}   {v:.2f}', codes(s))
    sh.save(os.path.join(OUT, 'alphabet.png'))


def pool(shree):
    """Every slot with an outline that the shipped tables do not already use, plus the
    letter's own run slots. Byte order (runs.py) says an overflow head must come from here."""
    used = set()
    for c, (h, tk, narrow, _) in H.HEAD.items():
        used |= {h, H.VATTU[c]} | ({narrow} if narrow else set())
        used |= set(H.PRECOMP_I.get(c, ())) | set(H.PRECOMP_U.get(c, ()))
    for m, v in H.MATRA_VARIANTS.items():
        used |= set(v)
    for cps in list(H.VOWELS.values()) + list(H.DIGITS.values()) + list(H.LIGATURES.values()):
        used |= set(cps)
    used |= {H.PENDANT, H.ANUSVARA, H.VISARGA, H.POLLU, H.NAKAARA_POLLU, H.REPH,
             H.AI_LENGTH, H.TA_RA, 0xE6, 0xE7, 0xE8} | set(H.POLLU_ALT) | set(H.STUBS)
    free = []
    for cp in sorted(shree.plat3):
        m = shree.metrics(cp)
        if cp not in used and m['contours'] and m['adv'] >= 150:
            free.append(cp)
    return free, used


HOOKS = (None, 0xE6, 0xE7, 0xE8)


def candidates(shree, letters):
    """Numbered candidate grid per letter, best shape score first.

    Candidate space, in the order the evidence justifies it:
      * the letter's own run slots (head, narrow base) alone and with each talakattu hook -
        for a letter runs.py marks "in run" the slot is pinned and only the hook is open;
      * every unassigned slot with an outline, alone and with each hook - the pool an
        overflow head has to come from;
      * slot + each below-baseline mark, because Modular Infotech spells the overflow
        letters as compositions (the Kannada map has ma = va + talakattu + hook).
    """
    free, _ = pool(shree)
    allslots = [cp for cp in sorted(shree.plat3)
                if shree.metrics(cp)['contours'] and shree.metrics(cp)['adv'] >= 150]
    below = [cp for cp in sorted(shree.plat3)
             if shree.metrics(cp)['adv'] <= 60 and shree.metrics(cp)['contours']
             and cp not in HOOKS and (shree.metrics(cp)['bbox'] or (0, 0, 0, 0))[3] < 400]
    for c in letters:
        h, tk, narrow, _ = H.HEAD[c]
        own = [h] + ([narrow] if narrow else [])
        strings = []
        # every main-line slot with and without each talakattu hook: nothing is excluded,
        # because a head can also be wrong by sitting on a slot another letter has claimed
        for cp in allslots:
            for hk in HOOKS:
                strings.append(chr(cp) + (chr(hk) if hk else ''))
        # compositions, for the overflow letters: slot + a below-baseline mark
        for cp in own + free:
            for mk in below:
                strings.append(chr(cp) + chr(mk))
        ref = bits(ref_render(c))
        scored = []
        seen = set()
        for s in strings:
            if s in seen:
                continue
            seen.add(s)
            img = T.render(shree, s, height=110)
            if img is None:
                continue
            scored.append((iou(ref, bits(img)), s, img))
        scored.sort(key=lambda t: -t[0])
        top = scored[:36]
        cur = legacy(c)
        if cur not in [s for _, s, _ in top]:
            img = T.render(shree, cur, height=110)
            if img is not None:
                top.append((iou(ref, bits(img)), cur, img))
        refimg = ref_render(c)
        sh = Sheet(6, (len(top) + 5) // 6,
                   f'Candidates for {c} - grey is {c} in Noto Serif Telugu, black is the '
                   f'candidate. Give me the number of the cell that IS {c}. '
                   f'"now" = what ships today.')
        for i, (v, s, img) in enumerate(top):
            tag = '  <= now' if s == cur else ''
            sh.cell(refimg, img, f'{i + 1:>2}. {v:.2f}{tag}', codes(s))
        sh.save(os.path.join(OUT, f'cand_{c}.png'))


def main():
    shree = T.Face(os.path.join(REPO, 'public', 'SHREE-TEL.ttf'))
    noto = T.Face(TELU)
    mode = sys.argv[1] if len(sys.argv) > 1 else 'alphabet'
    if mode == 'alphabet':
        alphabet(shree, noto)
    elif mode == 'cand':
        candidates(shree, sys.argv[2:] or ['మ'])
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
