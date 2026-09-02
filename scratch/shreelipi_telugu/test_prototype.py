import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 48)
noto_font = ImageFont.truetype(ref_font_path, 48)
label_font = ImageFont.load_default()

# Let's test some standard Telugu words
# 1. తెలుగు (Telugu)
# 2. భాష (Bhasha)
# 3. శ్రీ (Shree)
# 4. ఆంధ్రప్రదేశ్ (Andhra Pradesh)
# 5. నమస్కారం (Namaskaram)

# Let's build a prototype mapping dictionary
# In Shree-Tel:
# శ్రీ = '}' (0x7D)
# ం = chr(0xC6) or chr(0x2026) or '0'
# త = chr(0x2122) (or chr(0xa1))
# etc.

test_cases = [
    # (Unicode, Shree-Tel encoded string)
    ("శ్రీ", "}"),
    ("తెలుగు", f"{chr(0x2122)}ó{chr(0xcc)}{chr(0x7b)}{chr(0x56)}{chr(0x7b)}"), # త + ె + ల + ు + గ + ు
    ("భాష", f"{chr(0xbf)}{chr(0x4e)}{chr(0xd9)}"), # భ + ా + ష
    ("నమస్కారం", f"{chr(0xaf)}{chr(0xc4)}{chr(0xdc)}{chr(0x61)}{chr(0x4e)}{chr(0xc7)}{chr(0xc6)}"), # న + మ + స + క-వత్తు + ా + ర + ం
]

img = Image.new('RGB', (1000, len(test_cases) * 120 + 50), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (u_text, s_text) in enumerate(test_cases):
    y = i * 120 + 20
    draw.text((30, y), f"Unicode: {u_text}", fill=(100, 100, 100), font=label_font)
    draw.text((30, y + 25), u_text, fill=(0, 0, 180), font=noto_font)

    draw.text((500, y), f"Shree-Tel string: {repr(s_text)}", fill=(100, 100, 100), font=label_font)
    try:
        draw.text((500, y + 25), s_text, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        draw.text((500, y + 25), f"Error: {e}", fill=(255, 0, 0), font=label_font)

img.save('scratch/shreelipi_telugu/test_sample_rendering.png')
print("Rendered test_sample_rendering.png")
