import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 32)
noto_font = ImageFont.truetype(noto_path, 24)
label_font = ImageFont.load_default()

# Let's test all characters from Dec 32 to 255 with 'a' (ka) or standalone
# We will create a grid of all glyphs from 32 to 255 and some common extended ones
# For each, we render:
# 1. Standalone chr(code)
# 2. 'a' + chr(code) (Ka + glyph)
# 3. '²' + chr(code) (Pa + glyph)

codes = list(range(32, 256)) + [338, 339, 352, 353, 376, 402, 710, 732, 8211, 8212, 8216, 8217, 8218, 8220, 8221, 8222, 8224, 8225, 8226, 8230, 8240, 8249, 8250, 8482]

cols = 8
rows = (len(codes) + cols - 1) // cols
cell_w, cell_h = 170, 120

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, code in enumerate(codes):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(220, 220, 220))
    draw.text((x + 4, y + 4), f"Dec: {code} (0x{code:02X})", fill=(100, 100, 100), font=label_font)

    # Standalone
    try:
        draw.text((x + 10, y + 25), chr(code), fill=(0, 0, 0), font=shree_font)
    except:
        pass

    # With 'a' (Ka)
    try:
        draw.text((x + 60, y + 25), 'a' + chr(code), fill=(150, 0, 0), font=shree_font)
    except:
        pass

    # With '²' (Pa)
    try:
        draw.text((x + 110, y + 25), '²' + chr(code), fill=(0, 0, 150), font=shree_font)
    except:
        pass

img.save('scratch/shree_telugu_all_combinations.png')
print("Saved scratch/shree_telugu_all_combinations.png")
