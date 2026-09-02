from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

unknown_codes = [
    0xAB, 0xAC, 0xCA, 0xCC, 0xD2, 0xD7, 0xDA, 0xDB, 0xDF, 0xE4, 0xEB,
    0x192, 0x2018, 0x2019, 0x201C, 0x201D, 0x2021, 0x2022, 0x2026, 0x2039, 0x203A
]

cols = 5
rows = (len(unknown_codes) + cols - 1) // cols
cell_w, cell_h = 200, 100

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, code in enumerate(unknown_codes):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 4, y + 4), f"0x{code:04X} ({code})", fill=(100, 100, 100), font=label_font)
    
    try:
        # Standalone
        draw.text((x + 20, y + 25), chr(code), fill=(0, 0, 0), font=shree_font)
        # With 'a' prefix
        draw.text((x + 100, y + 25), 'a' + chr(code), fill=(150, 0, 0), font=shree_font)
    except Exception as e:
        pass

img.save('scratch/unknown_glyphs_rendered.png')
print("Saved scratch/unknown_glyphs_rendered.png")
