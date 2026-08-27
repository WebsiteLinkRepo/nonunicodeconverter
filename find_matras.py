from PIL import Image, ImageDraw, ImageFont
import sys

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 100)

for i in [65, 117, 118, 119, 120, 121, 122, 123, 124, 125, 64, 101, 102]:
    img = Image.new('RGB', (200, 200), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((50, 50), chr(61440 + i), font=font, fill=(0, 0, 0))
    img.save(f'matra_{i}.png')
print("Done")
