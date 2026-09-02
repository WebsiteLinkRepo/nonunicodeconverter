import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font_tt = TTFont(font_path)
cmap = font_tt.getBestCmap()

font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

# Get all valid codepoints
codepoints = sorted(cmap.keys())

# We will create multi-page or large grid image
# Let's make a grid of 10 columns, with large cells
cols = 10
rows = (len(codepoints) + cols - 1) // cols
cell_w, cell_h = 130, 110

img_w = cols * cell_w + 40
img_h = rows * cell_h + 60

img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, code in enumerate(codepoints):
    col = idx % cols
    row = idx // cols
    x = 20 + col * cell_w
    y = 30 + row * cell_h

    # Border
    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))

    # Label: Dec, Hex, Char repr
    draw.text((x + 5, y + 5), f"Dec: {code}", fill=(80, 80, 80), font=label_font)
    draw.text((x + 5, y + 20), f"Hex: 0x{code:02X}", fill=(0, 0, 150), font=label_font)

    # Draw the glyph
    try:
        draw.text((x + 40, y + 40), chr(code), fill=(0, 0, 0), font=font)
    except Exception as e:
        draw.text((x + 30, y + 45), "ERR", fill=(255, 0, 0), font=label_font)

img.save('scratch/shreelipi_telugu_complete_glyphs.png')
print(f"Rendered {len(codepoints)} glyphs to scratch/shreelipi_telugu_complete_glyphs.png")
