import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Let's render every single glyph at large size (100x100) with its codepoint, char, postscript name
os.makedirs('scratch/shreelipi_telugu/catalog', exist_ok=True)

pil_font = ImageFont.truetype(font_path, 60)
small_font = ImageFont.load_default()

items = sorted(cmap.items())
# Create composite images of 25 glyphs each (5x5 grid)
for page_idx in range(0, len(items), 25):
    page_items = items[page_idx:page_idx+25]
    img = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    for idx, (code, name) in enumerate(page_items):
        r = idx // 5
        c = idx % 5
        x = c * 200
        y = r * 200

        draw.rectangle([x+5, y+5, x+195, y+195], outline=(220, 220, 220), width=1)

        # Header info
        char = chr(code)
        info_text = f"0x{code:02X} ({code})\nrepr: {repr(char)}\nname: {name}"
        draw.text((x+10, y+10), info_text, fill=(80, 80, 80), font=small_font)

        # Render glyph
        try:
            draw.text((x+70, y+80), char, fill=(0, 0, 0), font=pil_font)
        except Exception as e:
            draw.text((x+70, y+80), "ERR", fill=(255, 0, 0), font=small_font)

    img.save(f'scratch/shreelipi_telugu/catalog/page_{page_idx//25}.png')

print(f"Rendered {len(items)} glyphs across {(len(items)+24)//25} pages.")
