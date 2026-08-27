from PIL import Image, ImageDraw, ImageFont
import sys

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 60)
img = Image.new('RGB', (1600, 3200), color = (255, 255, 255))
draw = ImageDraw.Draw(img)

try:
    label_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)
except:
    label_font = ImageFont.load_default()

for i in range(32, 256):
    row = (i - 32) // 8
    col = (i - 32) % 8
    x = col * 200
    y = row * 100
    
    draw.text((x + 5, y + 5), str(i) + " (" + chr(i) + ")", font=label_font, fill=(0, 0, 255))
    try:
        # PUA shift
        pua_char = chr(i + 61440)
        draw.text((x + 80, y + 20), pua_char, font=font, fill=(0, 0, 0))
    except Exception as e:
        pass
    draw.rectangle([x, y, x+200, y+100], outline=(200, 200, 200))

img.save('big_grid.png')
print("Saved big_grid.png")
