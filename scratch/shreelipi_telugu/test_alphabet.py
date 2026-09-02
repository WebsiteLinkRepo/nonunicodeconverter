import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 40)
noto_font = ImageFont.truetype(ref_font_path, 30)
label_font = ImageFont.load_default()

tests = []
for i in range(65, 123):  # A-Z, a-z
    tests.append((chr(i), chr(i)))

# Adding some other interesting ones from 0xC0 to 0xFF
for i in range(192, 256):
    tests.append((hex(i), chr(i)))

cols = 6
rows = (len(tests) + cols - 1) // cols
cell_w = 160
cell_h = 100
img_w = cols * cell_w + 20
img_h = rows * cell_h + 20

img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (label, shree_str) in enumerate(tests):
    r = idx // cols
    c = idx % cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.text((x, y), label, fill=(100, 100, 100), font=label_font)
    try:
        draw.text((x+40, y+20), shree_str, fill=(0, 0, 0), font=shree_font)
    except:
        pass

img.save('scratch/shreelipi_telugu/test_alphabet.png')
print("Saved scratch/shreelipi_telugu/test_alphabet.png")
