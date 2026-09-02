import os
from PIL import Image, ImageDraw, ImageFont
import fontTools.ttLib as ttLib

font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 48)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 16)

chars_to_test = [
    ('A', 0x41, 'అ'),
    ('B', 0x42, 'ఆ'),
    ('C', 0x43, 'ఇ'),
    ('D', 0x44, 'ఈ'),
    ('E', 0x45, 'ఉ'),
    ('F', 0x46, 'F?'),
    ('w', 0x77, 'ఋ (w)'),
    ('W', 0x57, 'W?'),
    ('G', 0x47, 'ఎ'),
    ('H', 0x48, 'ఏ'),
    ('I', 0x49, 'ఐ?'),
    ('J', 0x4A, 'ఒ'),
    ('K', 0x4B, 'ఓ'),
    ('L', 0x4C, 'ఔ'),
    ('+', 0x2B, '+ Anusvara?'),
    ('o', 0x6F, 'o?'),
    (':', 0x3A, ': Visarga?'),
    (';', 0x3B, ';?'),
    ('x', 0x78, 'x?'),
    ('v', 0x76, 'v?'),
    ('u', 0x75, 'u?'),
    ('t', 0x74, 't?')
]

img = Image.new('RGB', (1000, 600), 'white')
draw = ImageDraw.Draw(img)

for i, (ch, code, desc) in enumerate(chars_to_test):
    col = i % 5
    row = i // 5
    x = col * 200 + 20
    y = row * 110 + 20
    draw.text((x, y), f"{ch} (0x{code:02X}) - {desc}", fill='blue', font=label_font)
    draw.text((x + 20, y + 25), ch, fill='black', font=font)

img.save("scratch/vowels_exact.png")
print("Saved to scratch/vowels_exact.png")
