import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 40)
noto_font = ImageFont.truetype(ref_font_path, 40)
label_font = ImageFont.load_default()

words = [
    ("తెలుగు", chr(0x2122) + chr(0xE9) + chr(0xCB) + chr(0xF0) + chr(0x56) + chr(0xF0)),
    ("భాష", chr(0xBF) + chr(0xFA) + chr(153) + chr(0xE6)),
    ("దేశం", chr(0xA7) + chr(0xEA) + chr(0xD4) + chr(0xE6) + chr(0xC6)),
    ("పుస్తకం", chr(0xB2) + chr(0xF0) + chr(0xDC) + chr(0xE6) + chr(0x2122) + 'a' + chr(0xE6) + chr(0xC6)),
    ("కవిత", 'a' + chr(0xE6) + chr(0xD0) + chr(0xEC) + chr(0x2122) + chr(0xE6)),
]

img = Image.new('RGB', (1000, len(words) * 100 + 40), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (u_word, s_word) in enumerate(words):
    y = i * 100 + 20
    draw.text((30, y), f"Telugu Unicode:", fill=(100, 100, 100), font=label_font)
    draw.text((30, y + 25), u_word, fill=(0, 0, 180), font=noto_font)

    draw.text((450, y), f"Shree-Tel Converted:", fill=(100, 100, 100), font=label_font)
    try:
        draw.text((450, y + 25), s_word, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        draw.text((450, y + 25), f"Err: {e}", fill=(255, 0, 0), font=label_font)

img.save('scratch/shreelipi_telugu/test_postmatra_words.png')
print("Rendered test_postmatra_words.png")
