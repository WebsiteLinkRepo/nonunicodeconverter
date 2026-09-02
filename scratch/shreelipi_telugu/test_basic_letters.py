import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'

pil_font = ImageFont.truetype(font_path, 60)
label_font = ImageFont.load_default()

text_to_render = "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz"

img = Image.new('RGB', (1800, 300), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

x = 10
y = 10
for i, char in enumerate(text_to_render):
    draw.text((x, y), char, fill=(0, 0, 0), font=pil_font)
    draw.text((x, y + 80), char, fill=(255, 0, 0), font=label_font)
    x += 60
    if x > 1700:
        x = 10
        y += 120

img.save('scratch/shreelipi_telugu/basic_map.png')
print("Saved scratch/shreelipi_telugu/basic_map.png")
