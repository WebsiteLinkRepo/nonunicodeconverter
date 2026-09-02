#!/usr/bin/env python3
"""Rank SHREE-TEL cmap codes by shape similarity to a reference Unicode syllable."""
import sys
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

SHREE = "public/SHREE-TEL.ttf"
REF = "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"
N = 72  # normalized box

def bitmap(font, text):
    img = Image.new("L", (400, 260), 255)
    ImageDraw.Draw(img).text((40, 40), text, font=font, fill=0)
    bbox = Image.eval(img, lambda p: 255 - p).getbbox()
    if not bbox:
        return None
    return img.crop(bbox).resize((N, N), Image.LANCZOS).point(lambda p: 0 if p < 160 else 255)

def iou(a, b):
    pa, pb = a.load(), b.load()
    inter = union = 0
    for y in range(N):
        for x in range(N):
            ia, ib = pa[x, y] == 0, pb[x, y] == 0
            if ia or ib:
                union += 1
                if ia and ib:
                    inter += 1
    return inter / union if union else 0.0

shree_font = ImageFont.truetype(SHREE, 96)
ref_font = ImageFont.truetype(REF, 96)
codes = sorted(TTFont(SHREE).getBestCmap())
shree_bmp = {c: bitmap(shree_font, chr(c)) for c in codes}

for target in sys.argv[1:]:
    rb = bitmap(ref_font, target)
    if rb is None:
        print(f"{target!r}: reference did not render"); continue
    scores = sorted(((iou(rb, b), c) for c, b in shree_bmp.items() if b),
                    reverse=True)[:8]
    print(f"\n=== {target!r} (U+{ord(target[0]):04X}) top candidates ===")
    for s, c in scores:
        print(f"  {s:.3f}  {c:#04x}  {chr(c)!r}")
