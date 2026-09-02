import os
import math
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Create a detailed visual catalog
pil_font = ImageFont.truetype(font_path, 42)
label_font = ImageFont.load_default()

codepoints = sorted(cmap.keys())
print(f"Total codepoints: {len(codepoints)}")

cols = 10
rows = math.ceil(len(codepoints) / cols)
cell_w, cell_h = 120, 120
img_w = cols * cell_w + 40
img_h = rows * cell_h + 60

img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

draw.text((20, 15), f"Shree-Tel-0908 Detailed Glyph Catalog ({len(codepoints)} glyphs)", fill=(0, 0, 0), font=label_font)

for idx, code in enumerate(codepoints):
    col = idx % cols
    row = idx // cols
    x = 20 + col * cell_w
    y = 50 + row * cell_h

    # Cell border
    draw.rectangle([x, y, x + cell_w - 2, y + cell_h - 2], outline=(200, 200, 200))

    # Hex & Dec
    char_repr = repr(chr(code)) if code < 128 else f"\\x{code:02x}"
    header = f"0x{code:02X} ({code})\n{char_repr}"
    draw.text((x + 4, y + 4), header, fill=(80, 80, 80), font=label_font)

    # Glyph
    try:
        draw.text((x + 40, y + 45), chr(code), fill=(0, 0, 0), font=pil_font)
    except Exception as e:
        draw.text((x + 40, y + 45), "ERR", fill=(255, 0, 0), font=label_font)

os.makedirs('scratch/shreelipi_telugu', exist_ok=True)
img.save('scratch/shreelipi_telugu/detailed_glyph_catalog.png')
print("Saved scratch/shreelipi_telugu/detailed_glyph_catalog.png")
