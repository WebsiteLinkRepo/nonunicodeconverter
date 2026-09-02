import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Just render ALL glyphs, but now I will look for 'క' specifically.
# Since I cannot see the Telugu directly in my code easily if I don't know the mapping,
# I will output the glyphs in a single large sheet.

cols = 10
rows = (len(cmap) + cols - 1) // cols
cell_w = 120
cell_h = 70
img_w = cols * cell_w + 40
img_h = rows * cell_h + 40

img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

for idx, cp in enumerate(sorted(cmap.keys())):
    r = idx // cols
    c = idx % cols
    x = 20 + c * cell_w
    y = 20 + r * cell_h

    draw.text((x, y), f"{cp:04x}", fill=(0,0,0), font=label_font)
    try:
        draw.text((x+40, y), chr(cp), fill=(0,0,0), font=shree_font)
    except:
        pass

img.save('scratch/shreelipi_telugu/all_glyphs.png')
print("Saved scratch/shreelipi_telugu/all_glyphs.png")
