import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Check available Telugu system fonts
telugu_fonts = [
    '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf',
    '/usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf',
    '/usr/share/fonts/TTF/NotoSansTelugu-Regular.ttf',
    '/usr/share/fonts/google-noto/NotoSansTelugu-Regular.ttf',
]

ref_font_path = None
for p in telugu_fonts:
    if os.path.exists(p):
        ref_font_path = p
        break

print(f"Reference Telugu font: {ref_font_path}")

shree_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

# Let's dump all glyph details
print(f"Total codepoints: {len(cmap)}")
