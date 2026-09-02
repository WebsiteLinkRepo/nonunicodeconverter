from PIL import Image, ImageDraw, ImageFont
import os

font_path = "public/SHREE-TEL.ttf"
font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 16)

# Testing various combinations for ఋ, ౠ, and అం, అః
tests = [
    ("Option 1 (Current)", "A B C D E F ƒ ƒ G H I J K L AÆ A:"),
    ("Option 2 (With w / length)", "A B C D E F w w~ G H I J K L A+ A:"),
    ("Option 3 (With 0x0192 / florin)", "A B C D E F ƒ ƒ¨ G H I J K L AÆ A:"),
    ("Option 4 (Proper Anusvara)", "A B C D E F w w~ G H I J K L A¦ A:"),
]

img = Image.new('RGB', (1000, 500), 'white')
draw = ImageDraw.Draw(img)

for i, (label, text) in enumerate(tests):
    y = i * 110 + 20
    draw.text((20, y), label, fill='blue', font=label_font)
    draw.text((20, y + 25), text, fill='black', font=font)

img.save("scratch/step1_candidates.png")
print("Saved to scratch/step1_candidates.png")
