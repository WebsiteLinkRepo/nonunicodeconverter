import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font = TTFont(font_path)
cmap = font.getBestCmap()
shree_font = ImageFont.truetype(font_path, 28)
label_font = ImageFont.load_default()

# Let's dump all characters and their unicode hex, dec, char, and glyphname
glyphs = []
for code, name in sorted(cmap.items()):
    try:
        ch = chr(code)
    except:
        ch = '?'
    glyphs.append((code, name, ch))

print(f"Total glyphs in cmap: {len(glyphs)}")

# Let's render a comprehensive grid of all glyphs with code, hex, char
cols = 12
rows = (len(glyphs) + cols - 1) // cols
cell_w, cell_h = 100, 70

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (code, name, ch) in enumerate(glyphs):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(220, 220, 220))
    draw.text((x + 2, y + 2), f"{code:04X} {code}", fill=(100, 100, 100), font=label_font)
    draw.text((x + 2, y + 14), f"{name[:12]}", fill=(120, 120, 120), font=label_font)

    try:
        draw.text((x + 35, y + 25), ch, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        pass

img.save('scratch/shree_telugu_all_glyphs_detailed.png')
print("Saved scratch/shree_telugu_all_glyphs_detailed.png")
