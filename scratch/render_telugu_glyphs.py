import os
import math
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font_tt = TTFont(font_path)
cmap = font_tt.getBestCmap()

# Load font with Pillow
pil_font = ImageFont.truetype(font_path, 32)
label_font = ImageFont.load_default()

# Get all valid codepoints
codepoints = sorted(cmap.keys())
print(f"Total mapped characters: {len(codepoints)}")

# Grid layout: 16 columns
cols = 16
rows = math.ceil(len(codepoints) / cols)
cell_w, cell_h = 90, 90
img_w = cols * cell_w + 40
img_h = rows * cell_h + 60

img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

draw.text((20, 15), f"Shree-Tel-0908 Regular.ttf Glyph Map ({len(codepoints)} characters)", fill=(0, 0, 0), font=label_font)

for idx, code in enumerate(codepoints):
    col = idx % cols
    row = idx // cols
    x = 20 + col * cell_w
    y = 50 + row * cell_h

    # Draw cell border
    draw.rectangle([x, y, x + cell_w - 2, y + cell_h - 2], outline=(220, 220, 220))

    # Draw header with hex code
    hex_str = f"U+{code:04X}"
    draw.text((x + 4, y + 4), hex_str, fill=(100, 100, 100), font=label_font)

    # Draw glyph
    char_str = chr(code)
    try:
        draw.text((x + cell_w // 2 - 12, y + 26), char_str, fill=(0, 0, 0), font=pil_font)
    except Exception as e:
        draw.text((x + 10, y + 35), "ERR", fill=(255, 0, 0), font=label_font)

img.save('scratch/shree_telugu_glyph_chart.png')
print("Saved glyph chart to scratch/shree_telugu_glyph_chart.png")
