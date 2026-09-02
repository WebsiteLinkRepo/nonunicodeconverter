from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

# Test a + each char from 0xE0 to 0xFF
matra_codes = list(range(0xE0, 0x100))

cols = 6
rows = (len(matra_codes) + cols - 1) // cols
cell_w, cell_h = 180, 100

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, code in enumerate(matra_codes):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 4, y + 4), f"0x{code:02X} ({code})", fill=(100, 100, 100), font=label_font)
    
    try:
        # Draw 'a' (ka) + the matra
        draw.text((x + 20, y + 25), 'a' + chr(code), fill=(0, 0, 0), font=shree_font)
        # Draw standalone
        draw.text((x + 100, y + 25), chr(code), fill=(150, 0, 0), font=shree_font)
    except Exception as e:
        pass

img.save('scratch/all_matras_rendered.png')
print("Saved scratch/all_matras_rendered.png")
