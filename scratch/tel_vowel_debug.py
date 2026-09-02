#!/usr/bin/env python3
"""Render a large, readable chart of SHREE-TEL glyphs in the ranges that matter
for independent vowels, so we can identify which code holds ఋ / ౠ / sunna."""
import sys
from PIL import Image, ImageDraw, ImageFont

FONT = "public/SHREE-TEL.ttf"
SIZE = 64

codes = [int(a, 0) for a in sys.argv[2:]] if len(sys.argv) > 2 else list(range(0x20, 0x100))
out = sys.argv[1] if len(sys.argv) > 1 else "scratch/tel_vowel_debug.png"

font = ImageFont.truetype(FONT, SIZE)
label = ImageFont.load_default(16)

COLS = 8
CW, CH = 150, 150
rows = (len(codes) + COLS - 1) // COLS
img = Image.new("RGB", (COLS * CW, rows * CH), "white")
d = ImageDraw.Draw(img)

for i, c in enumerate(codes):
    x = (i % COLS) * CW
    y = (i // COLS) * CH
    d.rectangle([x, y, x + CW - 1, y + CH - 1], outline="#ccc")
    d.text((x + 6, y + 4), f"{hex(c)} {chr(c)!r}", fill="blue", font=label)
    try:
        d.text((x + 20, y + 34), chr(c), fill="black", font=font)
    except Exception as e:
        d.text((x + 20, y + 34), "ERR", fill="red", font=label)

img.save(out)
print("wrote", out, "codes:", len(codes))
