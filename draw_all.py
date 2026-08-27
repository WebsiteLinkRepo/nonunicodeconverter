from PIL import Image, ImageDraw, ImageFont
import os
font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 100)
os.makedirs('glyphs', exist_ok=True)
for i in range(128, 256):
    img = Image.new('RGB', (120, 120), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), chr(61440 + i), font=font, fill=(0, 0, 0))
    img.save(f'glyphs/{i}.png')
