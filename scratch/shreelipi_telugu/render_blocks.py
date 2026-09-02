import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

pil_font = ImageFont.truetype(font_path, 48)
label_font = ImageFont.load_default()

# We can render glyphs in blocks of 20 with large labels
codepoints = sorted(cmap.keys())

for block_idx in range(0, len(codepoints), 20):
    subset = codepoints[block_idx:block_idx+20]
    img = Image.new('RGB', (1200, 300), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    for i, code in enumerate(subset):
        x = (i % 10) * 120 + 10
        y = (i // 10) * 140 + 10

        draw.rectangle([x, y, x + 115, y + 135], outline=(200, 200, 200))

        # char representation
        char = chr(code)
        name = cmap[code]
        draw.text((x + 5, y + 5), f"{hex(code)} ({code})", fill=(100, 100, 100), font=label_font)
        draw.text((x + 5, y + 20), f"'{repr(char)[1:-1]}'", fill=(0, 0, 150), font=label_font)
        draw.text((x + 5, y + 35), name[:12], fill=(150, 0, 0), font=label_font)

        try:
            draw.text((x + 40, y + 55), char, fill=(0, 0, 0), font=pil_font)
        except:
            pass

    img.save(f'scratch/shreelipi_telugu/block_{block_idx//20}.png')

print("Saved all blocks")
