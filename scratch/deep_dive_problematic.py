from PIL import Image, ImageDraw, ImageFont

SHREE_PATH = "public/SHREE-TEL.ttf"
REF_PATH = "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"

shree_font = ImageFont.truetype(SHREE_PATH, 70)
ref_font = ImageFont.truetype(REF_PATH, 70)
label_font = ImageFont.load_default()

items_to_check = [
    ('ఘ', [
        ('0x50+e6', chr(0x50) + chr(0xe6)),
        ('0x50+e9', chr(0x50) + chr(0xe9)),
        ('0x52+e6', chr(0x52) + chr(0xe6)),
        ('0x50', chr(0x50)),
    ]),
    ('ఙ', [
        ('0x5a', chr(0x5a)),
        ('0x5a+e6', chr(0x5a) + chr(0xe6)),
        ('0x5c', chr(0x5c)),
        ('0x66', chr(0x66)),
    ]),
    ('ధ', [
        ('0xa3+24', chr(0xa3) + chr(0x24)),
        ('0xa3+e6+24', chr(0xa3) + chr(0xe6) + chr(0x24)),
        ('0xa7+24', chr(0xa7) + chr(0x24)),
        ('0xa7+e6+24', chr(0xa7) + chr(0xe6) + chr(0x24)),
        ('0xa3+e6+a2', chr(0xa3) + chr(0xe6) + chr(0xa2)),
        ('0xa3+e6+ad', chr(0xa3) + chr(0xe6) + chr(0xad)),
        ('0xa3+e6+2c', chr(0xa3) + chr(0xe6) + chr(0x2c)),
        ('0xae', chr(0xae)),
        ('0xae+e6', chr(0xae) + chr(0xe6)),
    ]),
    ('ప', [
        ('0xb2+e6', chr(0xb2) + chr(0xe6)),
        ('0xb3+e6', chr(0xb3) + chr(0xe6)),
        ('0xb4+e6', chr(0xb4) + chr(0xe6)),
        ('0xb5+e6', chr(0xb5) + chr(0xe6)),
    ]),
    ('బ', [
        ('0xba', chr(0xba)),
        ('0xba+e6', chr(0xba) + chr(0xe6)),
        ('0xbb+e6', chr(0xbb) + chr(0xe6)),
        ('0xbb', chr(0xbb)),
    ]),
    ('మ', [
        ('0xb4+e6', chr(0xb4) + chr(0xe6)),
        ('0xb5+e6', chr(0xb5) + chr(0xe6)),
        ('0xb2+e6', chr(0xb2) + chr(0xe6)),
        ('0xc4+e6', chr(0xc4) + chr(0xe6)),
        ('0x47+e6', chr(0x47) + chr(0xe6)),
    ]),
    ('య', [
        ('0xc4+e6', chr(0xc4) + chr(0xe6)),
        ('0xc5+e6', chr(0xc5) + chr(0xe6)),
        ('0xc4', chr(0xc4)),
        ('0xc5', chr(0xc5)),
    ]),
    ('ల', [
        ('0xcc', chr(0xcc)),
        ('0xcb+e6', chr(0xcb) + chr(0xe6)),
        ('0xcb', chr(0xcb)),
    ]),
    ('ష', [
        ('0xd9+e6', chr(0xd9) + chr(0xe6)),
        ('0xd9', chr(0xd9)),
        ('0x201e', chr(0x201e)),
    ]),
    ('స', [
        ('0xdc+e6', chr(0xdc) + chr(0xe6)),
        ('0xdc', chr(0xdc)),
        ('0xa8', chr(0xa8)),
        ('0xa8+e6', chr(0xa8) + chr(0xe6)),
    ]),
    ('హ', [
        ('0xe0', chr(0xe0)),
        ('0xdf+e6', chr(0xdf) + chr(0xe6)),
        ('0xe1+e6', chr(0xe1) + chr(0xe6)),
        ('0x2dc+e6', chr(0x2dc) + chr(0xe6)),
        ('0x2dc', chr(0x2dc)),
    ]),
]

rows = len(items_to_check)
img = Image.new("RGB", (1300, rows * 100 + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (uni_char, cand_list) in enumerate(items_to_check):
    y = 20 + idx * 100
    draw.line([(0, y - 5), (1300, y - 5)], fill=(220, 220, 220))
    
    # 1. Unicode reference
    draw.text((20, y + 10), uni_char, fill=(0, 140, 0), font=ref_font)
    draw.text((100, y + 25), f"Ref: {uni_char}", fill=(80, 80, 80), font=label_font)
    
    # 2. Candidate renderings
    x = 220
    for desc, s in cand_list:
        draw.text((x, y + 2), desc, fill=(180, 0, 0), font=label_font)
        draw.text((x, y + 15), s, fill=(0, 0, 0), font=shree_font)
        x += 160

img.save("scratch/deep_dive_problematic.png")
print("Saved scratch/deep_dive_problematic.png")
