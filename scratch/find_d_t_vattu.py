from PIL import Image, ImageDraw, ImageFont
import json

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

# We need to find: da_vattu, ta_vattu, na_vattu, sa_vattu, ha_vattu, La_vattu
# Let's render ALL glyphs under 'a' and look for them
from fontTools.ttLib import TTFont
font = TTFont(font_path)
cmap = font.getBestCmap()
items = sorted(cmap.items())

cols = 10
rows = (len(items) + cols - 1) // cols
cell_w, cell_h = 130, 90

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (code, name) in enumerate(items):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 2, y + 2), f"0x{code:02X} {chr(code) if code < 256 or code > 8000 else '?'}", fill=(100, 100, 100), font=label_font)
    
    try:
        draw.text((x + 40, y + 28), 'a' + chr(code), fill=(0, 0, 0), font=shree_font)
    except:
        pass

img.save('scratch/all_subscripts_under_ka.png')
print("Saved scratch/all_subscripts_under_ka.png")
