from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import sys

FONT_PATH = "/home/samuelvictor/Downloads/hari.ttf"
try:
    tt_font = TTFont(FONT_PATH)
    cmap = tt_font.getBestCmap()
    all_codes = sorted(cmap.keys())
    print(f"Font has {len(all_codes)} glyphs mapped in cmap.")
except Exception as e:
    print(f"FontTools error: {e}")
    sys.exit(1)

try:
    font = ImageFont.truetype(FONT_PATH, 32)
except Exception as e:
    print(f"PIL ImageFont error: {e}")
    sys.exit(1)

label_font = ImageFont.load_default()

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
    # Write hex code in top left
    d.text((x + 2, y + 2), f"0x{c:02x}" if c < 256 else f"{c:#04x}", font=label_font, fill=(100, 100, 100))
    # Write character code in bottom right
    d.text((x + 50, y + 55), str(c), font=label_font, fill=(180, 180, 180))

    try:
        d.text((x + 20, y + 25), chr(c), font=font, fill=(0, 0, 0))
    except Exception as e:
        d.text((x + 20, y + 20), "err", font=label_font, fill=(255, 0, 0))

img.save("scratch/hari_font/all_glyphs_grid.png")
print("Saved scratch/hari_font/all_glyphs_grid.png")
