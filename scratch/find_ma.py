import os
from PIL import Image, ImageDraw, ImageFont

SHREE_PATH = "public/SHREE-TEL.ttf"
REF_PATH = "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"
shree_font = ImageFont.truetype(SHREE_PATH, 50)
ref_font = ImageFont.truetype(REF_PATH, 50)
lbl_font = ImageFont.load_default()

candidates = [0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x4D, 0x55, 0x83, 0x87, 0xCF, 0xC3]

img = Image.new("RGB", (900, len(candidates) * 55 + 50), (255, 255, 255))
d = ImageDraw.Draw(img)

for i, code in enumerate(candidates):
    y = 20 + i * 55
    d.text((20, y + 10), f"0x{code:02X}", font=lbl_font, fill=(0, 0, 0))
    d.text((150, y), "మ", font=ref_font, fill=(0, 0, 200))
    try:
        # single
        d.text((300, y), chr(code), font=shree_font, fill=(200, 0, 0))
        # with talakattu E6
        d.text((450, y), chr(code) + chr(0xE6), font=shree_font, fill=(200, 0, 0))
        # with talakattu E7
        d.text((600, y), chr(code) + chr(0xE7), font=shree_font, fill=(200, 0, 0))
        # with talakattu E8
        d.text((750, y), chr(code) + chr(0xE8), font=shree_font, fill=(200, 0, 0))
    except:
        pass

img.save("scratch/telugu_out/find_ma.png")
