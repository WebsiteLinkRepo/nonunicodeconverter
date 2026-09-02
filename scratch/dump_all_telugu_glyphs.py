from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import math

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font = TTFont(font_path)
cmap = font.getBestCmap()

# Let's create an image showing every single glyph in the font, along with its code, hex, char, and glyph name!
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

items = sorted(cmap.items())
cols = 8
rows = math.ceil(len(items) / cols)

cell_w = 160
cell_h = 100
img_w = cols * cell_w + 40
img_h = rows * cell_h + 60

img = Image.new('RGB', (img_w, img_h), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (code, gname) in enumerate(items):
    c = idx % cols
    r = idx // cols
    x = 20 + c * cell_w
    y = 30 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 4, y + 4), f"{code} (0x{code:02X})", fill=(100, 100, 100), font=label_font)
    draw.text((x + 4, y + 18), gname[:15], fill=(0, 0, 150), font=label_font)

    try:
        char = chr(code)
        draw.text((x + 80, y + 30), char, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        draw.text((x + 80, y + 30), "ERR", fill=(255, 0, 0), font=label_font)

img.save('scratch/all_telugu_glyphs_identified.png')
print(f"Saved {len(items)} glyphs to scratch/all_telugu_glyphs_identified.png")
