import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Extract all glyph names and codepoints
glyphs_list = []
for cp, name in sorted(cmap.items()):
    glyphs_list.append((cp, name, chr(cp)))

print(f"Total mapped characters in font: {len(glyphs_list)}")

# Render each single character with its hex, dec, char, and glyph name in a clear grid
# Let's create an image showing all 217 glyphs clearly numbered

cols = 8
rows = (len(glyphs_list) + cols - 1) // cols

cell_w = 160
cell_h = 100
img_w = cols * cell_w + 40
img_h = rows * cell_h + 40

img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

for idx, (cp, name, ch) in enumerate(glyphs_list):
    r = idx // cols
    c = idx % cols
    x = 20 + c * cell_w
    y = 20 + r * cell_h

    # Draw box
    draw.rectangle([x, y, x + cell_w - 5, y + cell_h - 5], outline=(220, 220, 220), fill=(250, 250, 250))

    # Draw labels
    draw.text((x + 5, y + 5), f"0x{cp:04X} ({cp})", fill=(0, 0, 150), font=label_font)
    draw.text((x + 5, y + 20), f"{name}", fill=(100, 100, 100), font=label_font)

    # Draw glyph
    try:
        draw.text((x + 60, y + 35), ch, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        draw.text((x + 60, y + 35), "ERR", fill=(255, 0, 0), font=label_font)

img.save('scratch/shreelipi_telugu/complete_glyph_roster.png')
print("Saved scratch/shreelipi_telugu/complete_glyph_roster.png")
