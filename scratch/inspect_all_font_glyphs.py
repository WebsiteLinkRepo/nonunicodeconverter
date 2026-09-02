import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = "public/SHREE-TEL.ttf"
ttfont = TTFont(font_path)
cmap = ttfont.getBestCmap()

font = ImageFont.truetype(font_path, 28)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 10)

# Create grid of all mapped characters
chars = sorted(cmap.keys())
cols = 16
rows = (len(chars) + cols - 1) // cols

cell_w = 70
cell_h = 70
img = Image.new('RGB', (cols * cell_w, rows * cell_h), 'white')
draw = ImageDraw.Draw(img)

for idx, code in enumerate(chars):
    r = idx // cols
    c = idx % cols
    x = c * cell_w
    y = r * cell_h
    
    # Draw border
    draw.rectangle([x, y, x + cell_w - 1, y + cell_h - 1], outline='#e0e0e0')
    
    # Draw label
    char_str = chr(code)
    hex_str = f"0x{code:02X}" if code <= 0xFF else f"0x{code:04X}"
    draw.text((x + 2, y + 2), f"{hex_str}\n({code})", fill='gray', font=label_font)
    
    # Draw glyph
    try:
        draw.text((x + 15, y + 28), char_str, fill='black', font=font)
    except Exception as e:
        pass

img.save("scratch/all_font_glyphs_grid.png")
print(f"Total glyphs in cmap: {len(chars)}. Saved grid to scratch/all_font_glyphs_grid.png")
