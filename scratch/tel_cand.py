#!/usr/bin/env python3
"""Reference Telugu vowel vs. candidate SHREE-TEL strings, rendered large."""
import sys
from PIL import Image, ImageDraw, ImageFont

SHREE = ImageFont.truetype("public/SHREE-TEL.ttf", 110)
REF = ImageFont.truetype("/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf", 110)
LBL = ImageFont.load_default(18)

ref_text = sys.argv[1]
cands = sys.argv[2:]

CW, CH, COLS = 300, 230, 5
rows = 1 + (len(cands) + COLS - 1) // COLS
img = Image.new("RGB", (COLS * CW, rows * CH), "white")
d = ImageDraw.Draw(img)

d.rectangle([0, 0, CW - 1, CH - 1], outline="red", width=3)
d.text((10, 8), f"REFERENCE {ref_text}", fill="red", font=LBL)
d.text((60, 50), ref_text, fill="black", font=REF)

for i, c in enumerate(cands):
    s = "".join(chr(int(p, 16)) for p in c.split("+"))
    x = ((i + 1) % COLS) * CW
    y = ((i + 1) // COLS) * CH
    d.rectangle([x, y, x + CW - 1, y + CH - 1], outline="#bbb")
    d.text((x + 10, y + 8), c, fill="blue", font=LBL)
    d.text((x + 60, y + 50), s, fill="black", font=SHREE)

out = f"scratch/cand_{ord(ref_text[0]):04x}.png"
img.save(out)
print("wrote", out)
