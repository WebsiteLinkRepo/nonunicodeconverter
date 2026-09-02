import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 32)
noto_font = ImageFont.truetype(ref_font_path, 32)
label_font = ImageFont.load_default()

# Based on analyze_components.py & font mapping

img = Image.new('RGB', (800, 1000), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# mapping from shreeLipiTeluguConverter.ts

mapping = {
  'క': 'a',
  'ఖా': 'Q' + 'ú',
  'కా': 'a' + 'ú',
  'కి': 'a' + 'ì',
  'కీ': 'a' + 'í',
  'కు': 'a' + 'ð',
  'కూ': 'a' + 'ó'
}

for i, (text, glyphs) in enumerate(mapping.items()):
    y = i * 50 + 20
    draw.text((30, y), f"{text}", fill=(0, 0, 0), font=noto_font)
    draw.text((200, y), f"{glyphs}", fill=(0, 0, 0), font=shree_font)

img.save('scratch/shreelipi_telugu/test_systematic_guninthalu.png')
print("Rendered test_systematic_guninthalu.png")
