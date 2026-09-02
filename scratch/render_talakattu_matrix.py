import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 32)
label_font = ImageFont.load_default()

# Let's test all characters from Dec 32 to 255 with 'æ' (talakattu) and standalone
# to find ALL BASE CONSONANTS
chars = [chr(i) for i in range(32, 256)] + [chr(338), chr(339), chr(352), chr(353), chr(376), chr(402), chr(710), chr(732), chr(8211), chr(8212), chr(8216), chr(8217), chr(8218), chr(8220), chr(8221), chr(8222), chr(8224), chr(8225), chr(8226), chr(8230), chr(8240), chr(8249), chr(8250), chr(8482)]

cols = 10
rows = (len(chars) + cols - 1) // cols
cell_w, cell_h = 130, 90

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, ch in enumerate(chars):
    code = ord(ch)
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(220, 220, 220))
    draw.text((x + 4, y + 4), f"{code} (0x{code:02X})", fill=(100, 100, 100), font=label_font)

    # Standalone
    try:
        draw.text((x + 10, y + 25), ch, fill=(0, 0, 0), font=shree_font)
    except:
        pass

    # With talakattu 'æ' (0xE6)
    try:
        draw.text((x + 60, y + 25), ch + 'æ', fill=(180, 0, 0), font=shree_font)
    except:
        pass

img.save('scratch/all_with_talakattu.png')
print("Saved scratch/all_with_talakattu.png")
