#!/usr/bin/env python3
"""Chamfer-match reference Telugu letters against every SHREE-TEL code
(bare and with talakattu appended). Pure stdlib + PIL."""
import sys
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

SHREE_PATH = "public/SHREE-TEL.ttf"
REF_PATH = "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"
TALAKATTU = 0xE6
H = 56                     # normalized ink height
CANVAS = (150, 110)

def ink(font, text):
    """Render text, return sorted list of ink pixels normalized to height H,
    anchored at (left, baseline-ish top of bbox)."""
    img = Image.new("L", (600, 400), 255)
    ImageDraw.Draw(img).text((80, 90), text, font=font, fill=0)
    inv = Image.eval(img, lambda p: 255 - p)
    bb = inv.getbbox()
    if not bb:
        return None
    crop = img.crop(bb)
    w, h = crop.size
    if h == 0:
        return None
    scale = H / h
    nw = max(1, int(round(w * scale)))
    crop = crop.resize((nw, H), Image.LANCZOS)
    px = crop.load()
    pts = [(x, y) for y in range(H) for x in range(nw) if px[x, y] < 150]
    return pts or None

def dmap(pts, size):
    """Brute-force 2-pass chamfer distance map over a small canvas."""
    W, Hh = size
    BIG = 10**6
    d = [[BIG] * W for _ in range(Hh)]
    for x, y in pts:
        if 0 <= x < W and 0 <= y < Hh:
            d[y][x] = 0
    for y in range(Hh):
        for x in range(W):
            best = d[y][x]
            if y: best = min(best, d[y-1][x] + 3)
            if x: best = min(best, d[y][x-1] + 3)
            if y and x: best = min(best, d[y-1][x-1] + 4)
            if y and x + 1 < W: best = min(best, d[y-1][x+1] + 4)
            d[y][x] = best
    for y in range(Hh - 1, -1, -1):
        for x in range(W - 1, -1, -1):
            best = d[y][x]
            if y + 1 < Hh: best = min(best, d[y+1][x] + 3)
            if x + 1 < W: best = min(best, d[y][x+1] + 3)
            if y + 1 < Hh and x + 1 < W: best = min(best, d[y+1][x+1] + 4)
            if y + 1 < Hh and x: best = min(best, d[y+1][x-1] + 4)
            d[y][x] = best
    return d

def cost(a_pts, b_dmap, b_pts, a_dmap, dx):
    """Symmetric mean chamfer cost with horizontal offset dx applied to a."""
    W, Hh = CANVAS
    s1 = n1 = 0
    for x, y in a_pts:
        xx = x + dx
        if 0 <= xx < W and 0 <= y < Hh:
            s1 += b_dmap[y][xx]; n1 += 1
    s2 = n2 = 0
    for x, y in b_pts:
        xx = x - dx
        if 0 <= xx < W and 0 <= y < Hh:
            s2 += a_dmap[y][xx]; n2 += 1
    if not n1 or not n2:
        return 10**6
    return 0.5 * (s1 / n1 + s2 / n2)

shree_font = ImageFont.truetype(SHREE_PATH, 120)
ref_font = ImageFont.truetype(REF_PATH, 120)
codes = sorted(TTFont(SHREE_PATH).getBestCmap())

# build candidate table: (label, points, dmap)
cands = []
for c in codes:
    for suffix, tag in ((0, ""), (TALAKATTU, "+tk")):
        text = chr(c) + (chr(suffix) if suffix else "")
        p = ink(shree_font, text)
        if p:
            cands.append((f"{c:#04x}{tag}", p, dmap(p, CANVAS)))
print(f"{len(cands)} candidates built", file=sys.stderr)

for target in sys.argv[1:]:
    rp = ink(ref_font, target)
    if not rp:
        print(f"{target}: no render"); continue
    rd = dmap(rp, CANVAS)
    scored = []
    for lbl, p, d in cands:
        best = min(cost(rp, d, p, rd, dx) for dx in (-6, -3, 0, 3, 6))
        scored.append((best, lbl))
    scored.sort()
    top = "  ".join(f"{l}({s:.1f})" for s, l in scored[:6])
    print(f"{target}\t{top}")
