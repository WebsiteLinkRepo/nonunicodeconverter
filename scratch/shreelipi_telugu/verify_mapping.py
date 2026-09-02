import json
import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 40)
noto_font = ImageFont.truetype(ref_font_path, 40)
label_font = ImageFont.load_default()

map_dict = {
    "అ": "A", "ఆ": "B", "ఇ": "C", "ఈ": "D", "ఉ": "E", "ఊ": "F",
    "ఎ": "G", "ఏ": "H", "ఐ": "I", "ఒ": "J", "ఓ": "K", "ఔ": "L",
    "క": "a", "ఖ": "Q", "గ": "V", "ఘ": chr(402), "ఙ": "Z",
    "చ": "^", "ఛ": "b", "జ": "\\", "ఝ": "m", "ఞ": "n",
    "ట": "r", "ఠ": "t", "డ": "y", "ఢ": "|", "ణ": "~",
    "త": chr(8482), "థ": chr(163), "ద": chr(167), "ధ": chr(170), "న": chr(175),
    "ప": chr(178), "ఫ": chr(184), "బ": chr(186), "భ": chr(191), "మ": chr(169),
    "య": chr(196), "ర": chr(208), "ల": chr(203), "వ": chr(211), "శ": chr(212),
    "ష": chr(339), "స": chr(220), "హ": chr(732), "ళ": chr(202), "క్ష": "<", "ఱ": chr(352)
}

img = Image.new('RGB', (1200, ((len(map_dict)+9)//10) * 120 + 50), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (u_char, s_char) in enumerate(map_dict.items()):
    r = i // 10
    c = i % 10
    x = c * 110 + 20
    y = r * 120 + 20

    draw.text((x, y), u_char, fill=(0, 0, 180), font=noto_font)
    try:
        draw.text((x + 50, y), s_char, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        draw.text((x + 50, y), "?", fill=(255, 0, 0), font=label_font)
    draw.text((x, y + 60), repr(s_char), fill=(100, 100, 100), font=label_font)

img.save('scratch/shreelipi_telugu/map_verification.png')
print("Rendered map_verification.png")
