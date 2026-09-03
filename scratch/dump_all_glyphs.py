from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

SHREE_PATH = "public/SHREE-TEL.ttf"
shree_font = ImageFont.truetype(SHREE_PATH, 32)
label_font = ImageFont.load_default()

cmap = TTFont(SHREE_PATH).getBestCmap()
all_codes = sorted(cmap.keys())

COLS = 16
ROWS = (len(all_codes) + COLS - 1) // COLS
CELL_W, CELL_H = 70, 70

img = Image.new("RGB", (COLS * CELL_W, ROWS * CELL_H), (255, 255, 255))
d = ImageDraw.Draw(img)

for idx, c in enumerate(all_codes):
    r = idx // COLS
    col = idx % COLS
    x = col * CELL_W
    y = r * CELL_H

    d.rectangle([x, y, x + CELL_W - 1, y + CELL_H - 1], outline=(220, 220, 220))
    d.text((x + 2, y + 2), f"{c:#04x}", font=label_font, fill=(100, 100, 100))

    try:
        d.text((x + 20, y + 20), chr(c), font=shree_font, fill=(0, 0, 0))
    except Exception as e:
        d.text((x + 20, y + 20), "err", font=label_font, fill=(255, 0, 0))

img.save("scratch/telugu_out/all_glyphs_grid.png")
print("Saved all_glyphs_grid.png")
