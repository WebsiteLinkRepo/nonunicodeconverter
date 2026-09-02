import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

font_tt = TTFont(font_path)
cmap = font_tt.getBestCmap()
codepoints = sorted(cmap.keys())

shree_font = ImageFont.truetype(font_path, 48)
label_font = ImageFont.load_default()

# We will generate cards in chunks of 30 glyphs, large size (100x100)
chunk_size = 30
for chunk_idx in range(0, len(codepoints), chunk_size):
    chunk = codepoints[chunk_idx:chunk_idx + chunk_size]
    cols = 6
    rows = (len(chunk) + cols - 1) // cols
    cell_w, cell_h = 160, 140
    img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    for idx, code in enumerate(chunk):
        c = idx % cols
        r = idx // cols
        x = 10 + c * cell_w
        y = 10 + r * cell_h

        draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(180, 180, 180))
        draw.text((x + 6, y + 6), f"Dec: {code}", fill=(50, 50, 50), font=label_font)
        draw.text((x + 6, y + 22), f"0x{code:02X} ('{chr(code) if 32 <= code <= 126 else ''}')", fill=(0, 0, 180), font=label_font)

        try:
            draw.text((x + 50, y + 50), chr(code), fill=(0, 0, 0), font=shree_font)
        except Exception as e:
            draw.text((x + 30, y + 50), "ERR", fill=(255, 0, 0), font=label_font)

    img.save(f'scratch/shreelipi_telugu/chunk_{chunk_idx//chunk_size}.png')

print("Saved all chunks!")
