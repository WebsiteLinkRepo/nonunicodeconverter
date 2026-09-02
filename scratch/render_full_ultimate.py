import json
from PIL import Image, ImageDraw, ImageFont
import subprocess

# Remove subprocess runner since we run it manually
with open('scratch/converted_ultimate.json', 'r', encoding='utf-8') as f:
    converted_paras = json.load(f)

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 36)

# Calculate image height
img_h = 1400
img = Image.new('RGB', (1600, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 40
for conv in converted_paras:
    words = conv.split(' ')
    curr_line = ""
    lines = []
    for w in words:
        if len(curr_line) + len(w) > 55:
            lines.append(curr_line)
            curr_line = w
        else:
            curr_line = (curr_line + " " + w).strip()
    if curr_line:
        lines.append(curr_line)

    for l in lines:
        draw.text((40, y), l, font=font, fill=(0, 0, 0))
        y += 50
    y += 40

img.save('scratch/full_render_ultimate.png')
print('Saved scratch/full_render_ultimate.png')
