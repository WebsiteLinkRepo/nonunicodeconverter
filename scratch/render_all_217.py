from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

font_path = "public/SHREE-TEL.ttf"
font = TTFont(font_path)
cmap = font.getBestCmap()
shree_font = ImageFont.truetype(font_path, 48)
label_font = ImageFont.load_default()

items = sorted(cmap.items())
cols = 8
rows = (len(items) + cols - 1) // cols
cell_w, cell_h = 160, 110

img = Image.new("RGB", (cols * cell_w + 40, rows * cell_h + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (code, name) in enumerate(items):
    c = idx % cols
    r = idx // cols
    x = 20 + c * cell_w
    y = 20 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 4, y + 4), f"0x{code:02X} ({code})", fill=(0, 0, 150), font=label_font)
    draw.text((x + 4, y + 18), f"{name[:15]}", fill=(100, 100, 100), font=label_font)

    # 1. Bare glyph
    draw.text((x + 15, y + 35), chr(code), fill=(0, 0, 0), font=shree_font)
    # 2. With talakattu (0xE6)
    draw.text((x + 85, y + 35), chr(code) + chr(0xE6), fill=(200, 0, 0), font=shree_font)

img.save("scratch/all_217_glyphs.png")

# Also save 4 vertical chunks for detailed inspection
h = img.size[1]
chunk_h = h // 4
for i in range(4):
    top = i * chunk_h
    bottom = (i + 1) * chunk_h if i < 3 else h
    img.crop((0, top, img.size[0], bottom)).save(f"scratch/all_217_chunk_{i}.png")
print("Saved all_217_glyphs.png and chunks 0-3")
