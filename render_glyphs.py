from PIL import Image, ImageDraw, ImageFont
import sys

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 32)
img = Image.new('RGB', (1600, 1600), color = (255, 255, 255))
draw = ImageDraw.Draw(img)

try:
    label_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
except:
    label_font = ImageFont.load_default()

for i in range(32, 256):
    row = (i - 32) // 16
    col = (i - 32) % 16
    x = col * 100
    y = row * 100
    
    draw.text((x + 5, y + 5), str(i), font=label_font, fill=(0, 0, 0))
    try:
        # PUA shift
        pua_char = chr(i + 61440)
        draw.text((x + 20, y + 40), pua_char, font=font, fill=(255, 0, 0))
    except Exception as e:
        pass
    draw.rectangle([x, y, x+100, y+100], outline=(200, 200, 200))

img.save('neo_glyphs.png')
print("Saved neo_glyphs.png")
