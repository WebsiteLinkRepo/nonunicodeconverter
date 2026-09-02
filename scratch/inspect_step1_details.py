import os
from PIL import Image, ImageDraw, ImageFont

font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 16)

# Test converting the exact string from Step 1:
# అ ఆ ఇ ఈ ఉ ఊ ఋ ౠ ఎ ఏ ఐ ఒ ఓ ఔ అం అః
