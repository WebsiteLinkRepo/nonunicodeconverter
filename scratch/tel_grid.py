#!/usr/bin/env python3
"""Render a labeled grid of SHREE-TEL strings. Usage: tel_grid.py out.png cols 'label:codes' ..."""
import sys
from PIL import Image, ImageDraw, ImageFont
SH = ImageFont.truetype("public/SHREE-TEL.ttf", 96)
LBL = ImageFont.load_default(17)
out, cols = sys.argv[1], int(sys.argv[2])
items = [a.split(":",1) for a in sys.argv[3:]]
CW, CH = 270, 200
rows = (len(items)+cols-1)//cols
img = Image.new("RGB", (cols*CW, rows*CH), "white")
d = ImageDraw.Draw(img)
for i,(lab,codes) in enumerate(items):
    x,y = (i%cols)*CW, (i//cols)*CH
    s = "".join(chr(int(p,16)) for p in codes.split("+"))
    d.rectangle([x,y,x+CW-1,y+CH-1], outline="#bbb")
    d.text((x+8,y+6), lab, fill="blue", font=LBL)
    d.text((x+60,y+45), s, fill="black", font=SH)
img.save(out); print("wrote", out, len(items))
