#!/usr/bin/env python3
"""Render every SHREE-TEL cmap code at large size, in batches."""
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

SHREE = ImageFont.truetype("public/SHREE-TEL.ttf", 100)
LBL = ImageFont.load_default(18)
codes = sorted(TTFont("public/SHREE-TEL.ttf").getBestCmap())

CW, CH, COLS, PER = 280, 215, 5, 45
for b in range(0, len(codes), PER):
    chunk = codes[b:b + PER]
    rows = (len(chunk) + COLS - 1) // COLS
    img = Image.new("RGB", (COLS * CW, rows * CH), "white")
    d = ImageDraw.Draw(img)
    for i, c in enumerate(chunk):
        x, y = (i % COLS) * CW, (i // COLS) * CH
        d.rectangle([x, y, x + CW - 1, y + CH - 1], outline="#bbb")
        d.text((x + 8, y + 6), f"{c:#04x}", fill="blue", font=LBL)
        d.text((x + 55, y + 45), chr(c), fill="black", font=SHREE)
    out = f"scratch/sheet_{b // PER}.png"
    img.save(out)
    print("wrote", out, len(chunk))
