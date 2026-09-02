import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

glyphs_list = []
for cp, name in sorted(cmap.items()):
    glyphs_list.append((cp, name, chr(cp)))

items_per_page = 60
cols = 6
rows = 10
cell_w = 200
cell_h = 100
img_w = cols * cell_w + 40
img_h = rows * cell_h + 40

shree_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

for page_idx in range((len(glyphs_list) + items_per_page - 1) // items_per_page):
    img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    sub_list = glyphs_list[page_idx * items_per_page : (page_idx + 1) * items_per_page]
    for idx, (cp, name, ch) in enumerate(sub_list):
        r = idx // cols
        c = idx % cols
        x = 20 + c * cell_w
        y = 20 + r * cell_h

        draw.rectangle([x, y, x + cell_w - 5, y + cell_h - 5], outline=(200, 200, 200), fill=(248, 248, 252))
        draw.text((x + 5, y + 5), f"0x{cp:04X} ({cp})", fill=(0, 0, 150), font=label_font)
        draw.text((x + 5, y + 20), f"{name}", fill=(80, 80, 80), font=label_font)

        # Draw glyph in red center dot
        draw.text((x + 100, y + 35), ch, fill=(0, 0, 0), font=shree_font)

    page_file = f'scratch/shreelipi_telugu/roster_page_{page_idx}.png'
    img.save(page_file)
    print(f"Saved {page_file}")
