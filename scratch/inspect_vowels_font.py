import os
from PIL import Image, ImageDraw, ImageFont
import fontTools.ttLib as ttLib

font_path = "public/SHREE-TEL.ttf"
tt = ttLib.TTFont(font_path)
cmap = tt['cmap'].getBestCmap()

font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf" if os.path.exists("/usr/share/fonts/TTF/DejaVuSans.ttf") else "/usr/share/fonts/dejavu/DejaVuSans.ttf", 14)

print(f"Total mapped characters in cmap: {len(cmap)}")

# Render characters from 0x20 to 0xFF and any others in cmap
items = sorted(cmap.keys())

# Let's inspect specific ASCII ranges and high codes
img_w = 1200
img_h = 2400
img = Image.new('RGB', (img_w, img_h), 'white')
draw = ImageDraw.Draw(img)

cols = 10
col_w = img_w // cols
row_h = 70

for idx, code in enumerate(items):
    char = chr(code)
    gname = cmap[code]
    row = idx // cols
    col = idx % cols
    x = col * col_w + 10
    y = row * row_h + 10
    
    draw.text((x, y), f"{code:04X} ({code})", fill='gray', font=label_font)
    draw.text((x, y + 16), f"{gname[:8]}", fill='blue', font=label_font)
    try:
        draw.text((x + 20, y + 32), char, fill='black', font=font)
    except Exception as e:
        draw.text((x + 20, y + 32), "?", fill='red', font=label_font)

img.save("scratch/all_font_glyphs_vowels.png")
print("Saved to scratch/all_font_glyphs_vowels.png")
