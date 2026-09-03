import os
from PIL import Image, ImageDraw, ImageFont

SHREE_PATH = "public/SHREE-TEL.ttf"
REF_PATH = "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"
shree_font = ImageFont.truetype(SHREE_PATH, 40)
ref_font = ImageFont.truetype(REF_PATH, 40)
lbl_font = ImageFont.load_default()

bases = [
    ('క', 0x4D, 0xE6), ('ఖ', 0x51, 0), ('గ', 0x56, 0xE6), ('ఘ', 0x55, 0xE6), ('ఙ', 0x5D, 0),
    ('చ', 0x5E, 0xE6), ('ఛ', 0x62, 0), ('జ', 0x67, 0), ('ఝ', 0x6D, 0), ('ఞ', 0x70, 0),
    ('ట', 0x72, 0), ('ఠ', 0x75, 0xE6), ('డ', 0x79, 0xE6), ('ఢ', 0xC9, 0xE6), ('ణ', 0xD7, 0),
    ('త', 0x2122, 0xE6), ('థ', 0xA3, 0xE6), ('ద', 0xA7, 0xE6), ('ధ', 0xA4, 0xE6), ('న', 0xAF, 0xE6),
    ('ప', 0xB3, 0xE7), ('ఫ', 0xB8, 0xE7), ('బ', 0xBA, 0), ('భ', 0xBE, 0xE7), ('మ', 0xC3, 0xE6),
    ('య', 0xC4, 0xE8), ('ర', 0xC6, 0xE6), ('ల', 0xCC, 0), ('ళ', 0xE2, 0xE6), ('వ', 0xD0, 0xE6),
    ('శ', 0xD4, 0xE6), ('ష', 0xD9, 0xE7), ('స', 0xDC, 0xE7), ('హ', 0xDF, 0),
    ('క్ష', 0x201E, 0), ('ఱ', 0x201A, 0)
]

img = Image.new("RGB", (1000, len(bases) * 50 + 50), (255, 255, 255))
d = ImageDraw.Draw(img)

for i, (char, base_code, tk_code) in enumerate(bases):
    y = 20 + i * 50
    d.text((20, y), char, font=ref_font, fill=(0, 0, 200))

    txt = chr(base_code) + (chr(tk_code) if tk_code else "")
    d.text((200, y - 5), txt, font=shree_font, fill=(200, 0, 0))
    d.text((400, y), f"Base: {base_code:#04x}, TK: {tk_code:#04x}", font=lbl_font, fill=(0, 0, 0))

img.save("scratch/telugu_out/base_check.png")
print("Saved base_check.png")
