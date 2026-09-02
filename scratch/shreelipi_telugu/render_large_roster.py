import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Let's render each glyph extra large with its hex code and decimal code
# 4 pages of 60 glyphs each, with font size 48 so we can read every curve perfectly.

items_per_page = 54
cols = 6
rows = 9
cell_w = 220
cell_h = 120
img_w = cols * cell_w + 40
img_h = rows * cell_h + 40

shree_font = ImageFont.truetype(font_path, 48)
label_font = ImageFont.load_default()

glyphs_list = sorted(cmap.items())

for page_idx in range((len(glyphs_list) + items_per_page - 1) // items_per_page):
    img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    sub_list = glyphs_list[page_idx * items_per_page : (page_idx + 1) * items_per_page]
    for idx, (cp, name) in enumerate(sub_list):
        r = idx // cols
        c = idx % cols
        x = 20 + c * cell_w
        y = 20 + r * cell_h

        draw.rectangle([x, y, x + cell_w - 6, y + cell_h - 6], outline=(180, 180, 200), fill=(245, 248, 255))
        draw.text((x + 6, y + 6), f"0x{cp:04X} ({cp})", fill=(0, 0, 160), font=label_font)
        draw.text((x + 6, y + 22), f"{name}", fill=(90, 90, 90), font=label_font)

        # Draw glyph in black
        try:
            ch = chr(cp)
            draw.text((x + 110, y + 40), ch, fill=(0, 0, 0), font=shree_font)
        except Exception as e:
            draw.text((x + 110, y + 40), "ERR", fill=(255, 0, 0), font=label_font)

    page_file = f'scratch/shreelipi_telugu/large_roster_{page_idx}.png'
    img.save(page_file)
    print(f"Saved {page_file}")
