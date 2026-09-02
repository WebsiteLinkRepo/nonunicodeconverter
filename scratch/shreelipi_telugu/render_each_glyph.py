import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

pil_font = ImageFont.truetype(font_path, 48)
label_font = ImageFont.load_default()

os.makedirs('scratch/shreelipi_telugu/glyphs', exist_ok=True)

for code, name in sorted(cmap.items()):
    char_str = chr(code)
    img = Image.new('RGB', (160, 160), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Border
    draw.rectangle([0, 0, 159, 159], outline=(180, 180, 180))

    # Label: hex, dec, char, glyph name
    draw.text((6, 6), f"0x{code:02X} ({code})", fill=(0, 0, 0), font=label_font)
    draw.text((6, 20), f"'{repr(char_str)[1:-1]}'", fill=(100, 100, 100), font=label_font)
    draw.text((6, 34), name[:18], fill=(0, 0, 150), font=label_font)

    # Draw character
    try:
        draw.text((60, 60), char_str, fill=(0, 0, 0), font=pil_font)
    except Exception as e:
        draw.text((40, 60), "ERR", fill=(255, 0, 0), font=label_font)

    filename = f"scratch/shreelipi_telugu/glyphs/{code:04X}_{name}.png"
    img.save(filename)

print("Saved individual glyph cards in scratch/shreelipi_telugu/glyphs/")
