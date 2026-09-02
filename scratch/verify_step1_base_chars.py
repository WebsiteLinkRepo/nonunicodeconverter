import os
from PIL import Image, ImageDraw, ImageFont

font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 32)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf" if os.path.exists("/usr/share/fonts/TTF/DejaVuSans.ttf") else "/usr/share/fonts/dejavu/DejaVuSans.ttf", 16)

# Test independent vowels
vowels = [
    ("అ", "A"), ("ఆ", "B"), ("ఇ", "C"), ("ఈ", "D"),
    ("ఉ", "E"), ("ఊ", "F"), ("ఋ", "ƒ"), ("ౠ", "ƒ"),
    ("ఎ", "G"), ("ఏ", "H"), ("ఐ", "I"), ("ఒ", "J"),
    ("ఓ", "K"), ("ఔ", "L"), ("అం", "Aý"), ("అః", "A¦")
]

# Test base consonants with talakattu / standalone
consonants = [
    ("క", "a`"), ("ఖ", "Q"), ("గ", "V`"), ("ఘ", "R`"),
    ("ఙ", "Z"), ("చ", "^`"), ("ఛ", "b"), ("జ", "\\`"),
    ("ఝ", "m"), ("ఞ", "p"), ("ట", "r"), ("ఠ", "u"),
    ("డ", "y`"), ("ఢ", "|"), ("ణ", "~`"), ("త", "™`"),
    ("థ", "£`"), ("ద", "§`"), ("ధ", "®`"), ("న", "¯`"),
    ("ప", "²`"), ("ఫ", "¸"), ("బ", "º`"), ("భ", "¿`"),
    ("మ", "Ä`"), ("య", "Å`"), ("ర", "ˆ`"), ("ఱ", "‚"),
    ("ల", "Ë`"), ("ళ", "Ã`"), ("వ", "Ð`"), ("శ", "Ô`"),
    ("ష", "Ù`"), ("స", "Ü`"), ("హ", "˜`"), ("క్ష", "„`")
]

# Create image
img = Image.new('RGB', (1000, 800), color='white')
draw = ImageDraw.Draw(img)

draw.text((20, 20), "Step 1 Verification: Independent Vowels & Base Consonants (Shree-Tel)", fill='black', font=label_font)

y = 60
draw.text((20, y), "Independent Vowels:", fill='blue', font=label_font)
y += 30

col = 0
row_y = y
for uni, shree in vowels:
    x = 30 + (col % 8) * 120
    if col > 0 and col % 8 == 0:
        row_y += 70
    draw.text((x, row_y), f"{uni} ({shree})", fill='gray', font=label_font)
    draw.text((x, row_y + 20), shree, fill='black', font=font)
    col += 1

y = row_y + 90
draw.text((20, y), "Base Consonants:", fill='blue', font=label_font)
y += 30

col = 0
row_y = y
for uni, shree in consonants:
    x = 30 + (col % 8) * 120
    if col > 0 and col % 8 == 0:
        row_y += 70
    draw.text((x, row_y), f"{uni} ({shree})", fill='gray', font=label_font)
    draw.text((x, row_y + 20), shree, fill='black', font=font)
    col += 1

img.save("scratch/step1_base_chars_render.png")
print("Saved render to scratch/step1_base_chars_render.png")
