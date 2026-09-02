import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 32)
noto_font = ImageFont.truetype(ref_font_path, 32)
label_font = ImageFont.load_default()

# Telugu consonants to test
uni_consonants = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ',
    'చ', 'ఛ', 'జ', 'ఝ', 'ఞ',
    'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
    'త', 'థ', 'ద', 'ధ', 'న',
    'ప', 'ఫ', 'బ', 'భ', 'మ',
    'య', 'ర', 'ల', 'వ', 'శ',
    'ష', 'స', 'హ', 'ళ', 'క్ష', 'ఱ'
]

# Create an image to visually map them side-by-side
cols = 4
rows = (len(uni_consonants) + cols - 1) // cols
cell_w = 200
cell_h = 60

img_w = cols * cell_w + 20
img_h = rows * cell_h + 20

img = Image.new('RGB', (img_w, img_h), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, ch in enumerate(uni_consonants):
    r = idx // cols
    c = idx % cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.text((x, y), ch, fill=(0,0,0), font=noto_font)
    draw.text((x+50, y+10), f"{idx}", fill=(100,100,100), font=label_font)

img.save('scratch/shreelipi_telugu/noto_consonants.png')

# Now let's try mapping manually from the large rosters:
# M = క
# Q = ఖ
# V = గ
# I see £ (\xA3) or ƒ (\x92 = \x192) in previous attempts.
# Let's write down the mapping for all base bodies without talakattu:

map_dict = {
    'క': 'M',
    # We will fill the rest here by looking at roto pages.
}

print("Saved noto consonants guide!")
