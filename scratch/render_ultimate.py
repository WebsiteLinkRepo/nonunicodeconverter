import json
from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 28)

with open("scratch/ULTIMATE_OUTPUT.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Create image
img = Image.new('RGB', (1600, 1000), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Draw text
y = 40
for para in text.split('\n\n'):
    words = para.split()
    line = ""
    for w in words:
        test_line = (line + " " + w).strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] > 1500:
            draw.text((40, y), line, font=font, fill=(0, 0, 0))
            y += 45
            line = w
        else:
            line = test_line
    if line:
        draw.text((40, y), line, font=font, fill=(0, 0, 0))
        y += 65

img.save("scratch/shree_ultimate_render.png")
print("Rendered scratch/shree_ultimate_render.png successfully!")
