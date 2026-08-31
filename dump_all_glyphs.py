import fontTools.ttLib as ttLib
from PIL import Image, ImageDraw, ImageFont

font_path = 'public/AnuSM/ttf/NEOGANBO.TTF'
font = ttLib.TTFont(font_path)
cmap = font.getBestCmap()
img_font = ImageFont.truetype(font_path, 28)
label_font = ImageFont.load_default()

# Let's sort codepoints
codepoints = sorted(list(cmap.keys()))

# Create a grid of glyphs
cols = 16
rows = (len(codepoints) + cols - 1) // cols

cell_w = 80
cell_h = 60

img = Image.new('RGB', (cols * cell_w, rows * cell_h), 'white')
draw = ImageDraw.Draw(img)

for i, cp in enumerate(codepoints):
    c = i % cols
    r = i // cols
    x = c * cell_w
    y = r * cell_h
    
    # draw box
    draw.rectangle([x, y, x + cell_w - 1, y + cell_h - 1], outline='#eee')
    
    # draw hex
    draw.text((x + 2, y + 2), f"{hex(cp)[2:].upper()}", fill='#888', font=label_font)
    
    # draw glyph
    char = chr(cp)
    try:
        draw.text((x + 20, y + 18), char, fill='black', font=img_font)
    except Exception as e:
        pass

img.save('all_glyphs_neo_ganesh.png')
print("Saved all_glyphs_neo_ganesh.png, total glyphs:", len(codepoints))
