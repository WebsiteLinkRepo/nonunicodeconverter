#!/usr/bin/env python3
"""
Telugu Shree-Lipi (Shree-Tel-0908) mapping verification harness.

Two jobs:

  1. IDENTIFY  - given a Unicode Telugu syllable, rank the font's byte sequences by
                 shape similarity, and render a contact sheet so the call can be
                 confirmed by eye instead of guessed.
  2. VERIFY    - given the converter's actual output, render it beside the Unicode
                 reference and score it, so a regression is caught mechanically.

Why shape matching at all: the font's glyph names are generic Latin ('A', 'B', ...),
so there is no semantic information in the font to read. The only ground truth is
what the glyph looks like.

No numpy in this environment, so masks are packed into Python big-ints and compared
with bitwise ops + popcount. That is fast enough for a ~7k candidate sweep.

Usage:
    python3 scratch/telugu_verify.py identify క ఖ గ        # rank candidates
    python3 scratch/telugu_verify.py sweep మ ప ఫ           # + base:mark compositions
    python3 scratch/telugu_verify.py marks                 # chart of combining marks
    python3 scratch/telugu_verify.py chart                 # chart of every code
    python3 scratch/telugu_verify.py verify                # score converter output
"""
import os
import sys
import math
import json
import subprocess

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHREE = os.path.join(ROOT, "public", "SHREE-TEL.ttf")
REFS = [
    "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf",
    "/usr/share/fonts/noto/NotoSerifTelugu-Regular.ttf",
]
OUT = os.path.join(ROOT, "scratch", "telugu_out")

TALAKATTU = 0xE6

# Advance-width classes. The font mixes three kinds of glyph and mixing them up is
# what produced every bug in this table so far:
#   MARK  - combining, draws over/under the previous glyph, contributes no width
#   BASE  - narrow, incomplete letter that REQUIRES the talakattu 0xE6 on top
#   FULL  - complete spacing letter that must NOT get a talakattu
MARK_MAX = 60
BASE_MAX = 300

N = 72           # normalised mask is N x N
W = 88           # row stride, leaves margin so shift search cannot wrap rows
M = (W - N) // 2

_fonts = {}


def font(path, size):
    key = (path, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]


def bits(text, path, keep_aspect=True, size=110):
    """Rasterise `text`, tight-crop, normalise to NxN, pack into a big-int bitset."""
    img = Image.new("L", (1400, 560), 0)
    ImageDraw.Draw(img).text((220, 130), text, fill=255, font=font(path, size))
    box = img.getbbox()
    if not box:
        return None
    crop = img.crop(box)
    w, h = crop.size
    if w > 5 * h or h > 5 * w:      # degenerate sliver, never a letter
        return None
    if keep_aspect:
        s = min(N / w, N / h)
        nw, nh = max(1, round(w * s)), max(1, round(h * s))
        crop = crop.resize((nw, nh), Image.LANCZOS)
        out = Image.new("L", (N, N), 0)
        out.paste(crop, ((N - nw) // 2, (N - nh) // 2))
    else:
        out = crop.resize((N, N), Image.LANCZOS)
    px = out.load()
    v = 0
    for y in range(N):
        row = 0
        for x in range(N):
            if px[x, y] > 60:
                row |= 1 << x
        v |= row << ((y + M) * W + M)
    return v


def score(ref, cand, radius=4):
    """Best intersection-over-union over a small translation search."""
    best = 0.0
    for dy in range(-radius, radius + 1):
        shifted = cand << (dy * W) if dy >= 0 else cand >> (-dy * W)
        for dx in range(-radius, radius + 1):
            k = shifted << dx if dx >= 0 else shifted >> -dx
            union = (ref | k).bit_count()
            if union:
                best = max(best, (ref & k).bit_count() / union)
    return best


class Font:
    def __init__(self, path=SHREE):
        self.tt = TTFont(path)
        self.cmap = self.tt.getBestCmap()
        hmtx = self.tt["hmtx"]
        self.adv = {c: hmtx[self.cmap[c]][0] for c in self.cmap}
        glyphs = self.tt.getGlyphSet()
        self.blank = set()
        for c in self.cmap:
            pen = BoundsPen(glyphs)
            glyphs[self.cmap[c]].draw(pen)
            if pen.bounds is None:
                self.blank.add(c)

    def cls(self, c):
        a = self.adv[c]
        return "MARK" if a <= MARK_MAX else ("BASE" if a < BASE_MAX else "FULL")

    def codes(self, kind=None):
        return [c for c in sorted(self.cmap)
                if kind is None or self.cls(c) == kind]


def hexs(text):
    return "+".join(f"{ord(c):02X}" for c in text)


def refmasks(target):
    out = []
    for r in REFS:
        if os.path.exists(r):
            out.append((bits(target, r, True), bits(target, r, False)))
    return out


def best_score(target_refs, ka, st):
    b = 0.0
    for rka, rst in target_refs:
        if rka is not None and ka is not None:
            b = max(b, score(rka, ka))
        if rst is not None and st is not None:
            b = max(b, score(rst, st))
    return b


def build_candidates(f, with_compositions=False):
    """Byte sequences that could plausibly render as one standalone letter."""
    strings = []
    for c in f.codes():
        if c in f.blank:
            continue
        k = f.cls(c)
        if k == "MARK":
            continue                            # a mark alone is never a letter
        strings.append(chr(c))
        if k == "BASE":
            strings.append(chr(c) + chr(TALAKATTU))
    if with_compositions:
        marks = [c for c in f.codes("MARK") if c != TALAKATTU and c not in f.blank]
        for b in f.codes("BASE"):
            if b in f.blank:
                continue
            for m in marks:
                strings.append(chr(b) + chr(m))
                strings.append(chr(b) + chr(m) + chr(TALAKATTU))
                strings.append(chr(b) + chr(TALAKATTU) + chr(m))
    seen, uniq = set(), []
    for s in strings:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def rank(f, targets, with_compositions=False, top=10):
    cands = []
    for s in build_candidates(f, with_compositions):
        ka = bits(s, SHREE, True)
        if ka is not None:
            cands.append((s, ka, bits(s, SHREE, False)))
    print(f"# {len(cands)} candidate byte sequences", file=sys.stderr)
    results = {}
    for tg in targets:
        refs = refmasks(tg)
        scored = [(best_score(refs, ka, st), s) for s, ka, st in cands]
        scored.sort(reverse=True)
        results[tg] = scored[:top]
        print(f"{tg}  " + "  ".join(f"{hexs(s)}:{v:.3f}" for v, s in scored[:6]))
        sys.stdout.flush()
    return results


def sheet(results, name, cols=8, cell=(150, 168)):
    """Contact sheet: Unicode reference (green) then ranked candidates (black)."""
    os.makedirs(OUT, exist_ok=True)
    cw, chh = cell
    big = font(SHREE, 82)
    ref = font(REFS[0], 76)
    lab = font("/usr/share/fonts/TTF/DejaVuSans.ttf", 14)
    rows = len(results)
    img = Image.new("RGB", (170 + cols * cw + 12, rows * chh + 12), "white")
    d = ImageDraw.Draw(img)
    for i, (tg, scored) in enumerate(results.items()):
        y = 6 + i * chh
        d.rectangle([4, y, img.size[0] - 6, y + chh - 6], outline=(150, 150, 150))
        d.text((10, y + 6), f"REF {tg}", fill=(0, 0, 190), font=lab)
        d.text((22, y + 30), tg, fill=(0, 130, 0), font=ref)
        for j, (v, s) in enumerate(scored[:cols]):
            x = 170 + j * cw
            d.text((x, y + 6), f"{hexs(s)}  {v:.2f}", fill=(0, 0, 190), font=lab)
            d.text((x + 8, y + 30), s, fill="black", font=big)
    path = os.path.join(OUT, f"{name}.png")
    img.save(path)
    # split tall sheets so they stay legible when viewed
    h = img.size[1]
    parts = max(1, math.ceil(rows / 4))
    if parts > 1:
        for k in range(parts):
            top, bot = k * h // parts, (k + 1) * h // parts
            img.crop((0, top, img.size[0], bot)).save(
                os.path.join(OUT, f"{name}_{k}.png"))
    print(f"wrote {path} ({parts} part(s))")
    return path


def chart(f, kind=None, name="chart"):
    """Every code in the font (or one advance class), bare and with talakattu."""
    os.makedirs(OUT, exist_ok=True)
    codes = f.codes(kind)
    big = font(SHREE, 74)
    lab = font("/usr/share/fonts/TTF/DejaVuSans.ttf", 14)
    cols, cw, chh = 6, 250, 150
    rows = math.ceil(len(codes) / cols)
    img = Image.new("RGB", (cols * cw + 16, rows * chh + 16), "white")
    d = ImageDraw.Draw(img)
    for i, c in enumerate(codes):
        r, cc = divmod(i, cols)
        x, y = 8 + cc * cw, 8 + r * chh
        d.rectangle([x, y, x + cw - 4, y + chh - 4], outline=(170, 170, 170))
        d.text((x + 4, y + 3), f"{c:04X} adv{f.adv[c]} {f.cls(c)}",
               fill=(0, 0, 190), font=lab)
        # marks draw over the preceding glyph, so offset them to stay visible
        ox = 60 if f.cls(c) == "MARK" else 10
        d.text((x + ox, y + 26), chr(c), fill="black", font=big)
        if f.cls(c) == "BASE":
            d.text((x + 130, y + 26), chr(c) + chr(TALAKATTU),
                   fill=(200, 0, 0), font=big)
    parts = max(1, math.ceil(rows / 5))
    h = img.size[1]
    for k in range(parts):
        top, bot = k * h // parts, (k + 1) * h // parts
        img.crop((0, top, img.size[0], bot)).save(
            os.path.join(OUT, f"{name}_{k}.png"))
    print(f"wrote {parts} part(s) of {name} ({len(codes)} codes)")


# ---------------------------------------------------------------- verify mode

VOWELS = "అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ".split()
CONSONANTS = ("క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న "
              "ప ఫ బ భ మ య ర ల ళ వ శ ష స హ").split()
MATRAS = ["", "ా", "ి", "ీ", "ు", "ూ", "ృ", "ె", "ే", "ై", "ొ", "ో", "ౌ"]


def convert(strings):
    """Run the real TypeScript converter over `strings` and return its output."""
    tmp = "/tmp/telugu_verify"
    os.makedirs(tmp, exist_ok=True)
    esbuild = os.path.join(ROOT, "node_modules", ".bin", "esbuild")
    src = os.path.join(ROOT, "src", "utils", "shreeLipiTeluguConverter.ts")
    subprocess.run([esbuild, src, "--format=esm", f"--outfile={tmp}/conv.mjs",
                    "--log-level=error"], check=True)
    with open(f"{tmp}/run.mjs", "w") as fh:
        fh.write(
            "import {convertUnicodeToShreeLipiTelugu as C} from '%s/conv.mjs';\n"
            "const inp=JSON.parse(process.argv[2]);\n"
            "console.log(JSON.stringify(inp.map(s=>C(s))));\n" % tmp)
    r = subprocess.run(["node", f"{tmp}/run.mjs", json.dumps(strings)],
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def verify(targets, name="verify", threshold=0.55):
    """Render converter output beside the Unicode reference and score each row."""
    os.makedirs(OUT, exist_ok=True)
    outs = convert(targets)
    rows = []
    for tg, got in zip(targets, outs):
        refs = refmasks(tg)
        ka, st = bits(got, SHREE, True), bits(got, SHREE, False)
        rows.append((tg, got, best_score(refs, ka, st)))

    big = font(SHREE, 74)
    ref = font(REFS[0], 68)
    lab = font("/usr/share/fonts/TTF/DejaVuSans.ttf", 14)
    cols, cw, chh = 5, 320, 130
    nrows = math.ceil(len(rows) / cols)
    img = Image.new("RGB", (cols * cw + 16, nrows * chh + 16), "white")
    d = ImageDraw.Draw(img)
    for i, (tg, got, s) in enumerate(rows):
        r, cc = divmod(i, cols)
        x, y = 8 + cc * cw, 8 + r * chh
        ok = s >= threshold
        d.rectangle([x, y, x + cw - 4, y + chh - 4],
                    outline=(0, 150, 0) if ok else (220, 0, 0), width=2 if ok else 3)
        d.text((x + 5, y + 4), f"{'ok ' if ok else 'BAD'} {hexs(got)}  {s:.2f}",
               fill=(0, 120, 0) if ok else (200, 0, 0), font=lab)
        d.text((x + 10, y + 26), tg, fill=(0, 130, 0), font=ref)
        d.text((x + 160, y + 26), got, fill="black", font=big)
    parts = max(1, math.ceil(nrows / 5))
    h = img.size[1]
    for k in range(parts):
        top, bot = k * h // parts, (k + 1) * h // parts
        img.crop((0, top, img.size[0], bot)).save(
            os.path.join(OUT, f"{name}_{k}.png"))

    bad = [(t, g, s) for t, g, s in rows if s < threshold]
    print(f"{len(rows) - len(bad)}/{len(rows)} above {threshold} — "
          f"wrote {parts} part(s) of {name}")
    for t, g, s in bad:
        print(f"  BAD  {t}  ->  {hexs(g)}  {s:.3f}")
    return bad


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    args = sys.argv[2:]
    f = Font()
    if cmd == "identify":
        sheet(rank(f, args or CONSONANTS), "identify")
    elif cmd == "sweep":
        sheet(rank(f, args or CONSONANTS, with_compositions=True), "sweep")
    elif cmd == "marks":
        chart(f, "MARK", "marks")
    elif cmd == "bases":
        chart(f, "BASE", "bases")
    elif cmd == "full":
        chart(f, "FULL", "full")
    elif cmd == "chart":
        chart(f, None, "chart")
    elif cmd == "verify":
        targets = args or (VOWELS + CONSONANTS)
        bad = verify(targets, "verify")
        sys.exit(1 if bad else 0)
    elif cmd == "guninthalu":
        targets = [c + m for c in (args or CONSONANTS) for m in MATRAS]
        bad = verify(targets, "guninthalu")
        sys.exit(1 if bad else 0)
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
