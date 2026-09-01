from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import math

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
tt = TTFont(font_path)
cmap = tt['cmap'].getBestCmap()
font = ImageFont.truetype(font_path, 40)

# We will render every glyph mapped in the font in a big grid
valid_chars = list(cmap.keys())
cols = 16
rows = math.ceil(len(valid_chars) / cols)

img = Image.new('RGB', (cols * 80, rows * 80), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, code in enumerate(valid_chars):
    x = (i % cols) * 80
    y = (i // cols) * 80

    # Draw a thin box
    draw.rectangle([x, y, x+80, y+80], outline=(200, 200, 200))

    # Render the character
    char = chr(code)
    draw.text((x + 20, y + 20), char, font=font, fill=(0, 0, 0))

    # Write the hex code small as text using default font
    # default PIL font gives tiny text
    draw.text((x + 2, y + 2), f"{code:02x}", fill=(255, 0, 0))

img.save('scratch/all_glyphs.png')
print(f"Rendered {len(valid_chars)} glyphs to scratch/all_glyphs.png")
