#!/usr/bin/env python3
"""Row-per-letter sheet: reference glyph followed by candidate SHREE-TEL strings.
Usage: tel_rows.py out.png 'ref:cand,cand,...' 'ref:cand,...'
Candidates are '+'-joined hex codes, e.g. 'ba+ee'."""
import sys
from PIL import Image, ImageDraw, ImageFont

SHREE = ImageFont.truetype("public/SHREE-TEL.ttf", 96)
REF = ImageFont.truetype("/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf", 96)
LBL = ImageFont.load_default(17)

out = sys.argv[1]
rows = [a.split(":", 1) for a in sys.argv[2:]]
maxc = max(len(r[1].split(",")) for r in rows)
CW, CH = 260, 195
img = Image.new("RGB", ((maxc + 1) * CW, len(rows) * CH), "white")
d = ImageDraw.Draw(img)
for ri, (ref, cands) in enumerate(rows):
    y = ri * CH
    d.rectangle([0, y, CW - 1, y + CH - 1], outline="red", width=3)
    d.text((8, y + 5), "REF", fill="red", font=LBL)
    d.text((70, y + 40), ref, fill="black", font=REF)
    for ci, c in enumerate(cands.split(",")):
        x = (ci + 1) * CW
        s = "".join(chr(int(p, 16)) for p in c.split("+"))
        d.rectangle([x, y, x + CW - 1, y + CH - 1], outline="#bbb")
        d.text((x + 8, y + 5), c, fill="blue", font=LBL)
        d.text((x + 60, y + 40), s, fill="black", font=SHREE)
img.save(out)
print("wrote", out)
