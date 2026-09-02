from PIL import Image, ImageDraw, ImageFont
import os

font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 16)

# Test characters for UU (ఊ)
# Could it be E + something? E + 0x203A (›)? E + 0x02DC (˜)?
# Or maybe the actual UU is not F. Let's look through the 0x4x area.
# 0x47 (G) is ఎ
# 0x48 (H) is ఏ

def get_char(code):
    return chr(code)

tests = [
    ("Competitor match attempt UU:", "E" + chr(0x5E)), 
    ("Matches for UU?", "E~ E› E" + chr(0x2026) + " E" + chr(0x2122)),
    ("Maybe UU is mapped to...", "F f E" + chr(0xAD)),
    ("Anusvara tests (A + ...)", "A0 A" + chr(0x30) + " A" + chr(0xB7) + " A" + chr(0x75) + " A" + chr(0x78)),
    ("Visarga tests (A + ...)", "A: A; A" + chr(0x40)),
    ("R, RR tests", chr(0x76) + " " + chr(0x77))
]

img = Image.new('RGB', (800, 600), 'white')
draw = ImageDraw.Draw(img)

for i, (label, text) in enumerate(tests):
    y = i * 90 + 20
    draw.text((20, y), label, fill='blue', font=label_font)
    draw.text((20, y + 25), text, fill='black', font=font)

img.save("scratch/test_uu_am.png")
print("Saved to scratch/test_uu_am.png")
