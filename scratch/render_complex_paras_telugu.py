import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 26)
noto_font = ImageFont.truetype(noto_path, 22)
title_font = ImageFont.truetype(noto_path, 26)
label_font = ImageFont.load_default()

with open('scratch/TELUGU_COMPLEX_PARAS_INPUT.txt', 'r', encoding='utf-8') as f:
    input_text = f.read()

with open('scratch/TELUGU_COMPLEX_PARAS_OUTPUT.txt', 'r', encoding='utf-8') as f:
    output_text = f.read()

input_paras = [p.strip() for p in input_text.split('\n\n') if p.strip()]
output_paras = [p.strip() for p in output_text.split('\n\n') if p.strip()]

img_w = 1400
img_h = 2400
img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

draw.text((30, 20), "Unicode vs Shree-Lipi Telugu Side-by-Side Visual Verification", fill=(0, 0, 128), font=title_font)

y = 80
for idx, (in_p, out_p) in enumerate(zip(input_paras, output_paras)):
    draw.line([(30, y - 10), (img_w - 30, y - 10)], fill=(200, 200, 200), width=2)
    draw.text((30, y), f"Paragraph {idx + 1} (Unicode Reference):", fill=(150, 0, 0), font=label_font)
    y += 25

    # Render Unicode wrapped lines
    lines = in_p.split('\n')
    for line in lines:
        draw.text((40, y), line, fill=(0, 0, 0), font=noto_font)
        y += 35

    y += 10
    draw.text((30, y), f"Paragraph {idx + 1} (Shree-Tel-0908 Converted Output):", fill=(0, 100, 0), font=label_font)
    y += 25

    # Render Shree-Tel lines
    lines = out_p.split('\n')
    for line in lines:
        draw.text((40, y), line, fill=(0, 0, 0), font=shree_font)
        y += 45

    y += 30

img = img.crop((0, 0, img_w, min(img_h, y + 50)))
img.save('scratch/complex_paras_telugu_render.png')
print("Saved verification render to scratch/complex_paras_telugu_render.png")
