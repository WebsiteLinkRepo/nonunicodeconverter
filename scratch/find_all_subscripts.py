from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font = TTFont(font_path)
cmap = font.getBestCmap()
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

# Let's render 'a' (ka) + every character in cmap to see which ones are subscripts (vattulu)!
subscripts = []

cols = 10
items = sorted(cmap.items())
rows = (len(items) + cols - 1) // cols
cell_w, cell_h = 130, 90

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (code, name) in enumerate(items):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 2, y + 2), f"0x{code:02X} ({code})", fill=(100, 100, 100), font=label_font)
    draw.text((x + 2, y + 14), f"{name[:12]}", fill=(130, 130, 130), font=label_font)

    try:
        # Render 'a' (ka) + the character
        draw.text((x + 40, y + 28), 'a' + chr(code), fill=(0, 0, 0), font=shree_font)
    except:
        pass

img.save('scratch/all_with_ka_prefix.png')
print("Saved scratch/all_with_ka_prefix.png")
