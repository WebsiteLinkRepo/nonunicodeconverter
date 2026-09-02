import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 28)
noto_font = ImageFont.truetype(ref_font_path, 28)
label_font = ImageFont.load_default()

# Let's define the candidate base consonants in Shree-Lipi:
# Consonant bases:
# క -> a
# ఖ -> Q
# గ -> V
# ఘ -> \x83 (0x192 / ƒ)
# ఙ -> Z
# చ -> ^
# ఛ -> b
# జ -> \x5C (\) or f
# ఝ -> m
# ఞ -> p
# ట -> r
# ఠ -> u
# డ -> y
# ఢ -> |
# ణ -> ~
# త -> ™ (™)
# థ -> \xa3 (£)
# ద -> \xa7 (§)
# ధ -> \xae (®)
# న -> \xaf (¯)
# ప -> \xb2 (²)
# ఫ -> \xb8 (¸)
# బ -> \xba (º)
# భ -> \xbf (¿)
# మ -> \xc4 (Ä)
# య -> \xc4 / \xc5 (Å)
# ర -> \xc7 (Ç)
# ల -> \xcb (Ë)
# వ -> \xd0 (Ð)
# శ -> \xd4 (Ô)
# ష -> \x9c (0x153 / œ)
# స -> \xdc (Ü)
# హ -> ˜ (˜)
# ళ -> \xc3 (Ã)
# క్ష -> <
# ఱ -> Š (Š)

consonants = [
    ('క', 'a\xE6'),
    ('ఖ', 'Q\xE6'),
    ('గ', 'V\xE6'),
    ('ఘ', 'ƒ\xE6'),
    ('చ', '^\xE6'),
    ('ఛ', 'b\xE6'),
    ('జ', '\\\xE6'),
    ('ఝ', 'm\xE6'),
    ('ట', 'r\xE6'),
    ('ఠ', 'u\xE6'),
    ('డ', 'y\xE6'),
    ('ఢ', '|\xE6'),
    ('ణ', '~\xE6'),
    ('త', '™\xE6'),
    ('థ', '\xA3\xE6'),
    ('ద', '\xA7\xE6'),
    ('ధ', '\xAE\xE6'),
    ('న', '\xAF\xE6'),
    ('ప', '\xB2\xE6'),
    ('ఫ', '\xB8\xE6'),
    ('బ', '\xBA\xE6'),
    ('భ', '\xBF\xE6'),
    ('మ', '\xC4\xE6'),
    ('య', '\xC5\xE6'),
    ('ర', '\xC7\xE6'),
    ('ల', '\xCB\xE6'),
    ('వ', '\xD0\xE6'),
    ('శ', '\xD4\xE6'),
    ('ష', 'œ\xE6'),
    ('స', '\xDC\xE6'),
    ('హ', '˜\xE6'),
    ('ళ', '\xC3\xE6'),
    ('క్ష', '<\xE6'),
    ('ఱ', 'Š\xE6'),
]

cols = 4
rows = (len(consonants) + cols - 1) // cols
cell_w = 280
cell_h = 70
img = Image.new('RGB', (cols * cell_w + 40, rows * cell_h + 40), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (u_char, shree_str) in enumerate(consonants):
    r = idx // cols
    c = idx % cols
    x = 20 + c * cell_w
    y = 20 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 5, y + cell_h - 5], outline=(200, 200, 200), fill=(250, 250, 252))
    draw.text((x + 10, y + 10), f"Uni: {u_char}", fill=(0, 0, 150), font=noto_font)
    draw.text((x + 140, y + 10), f"Shree:", fill=(100, 100, 100), font=label_font)
    draw.text((x + 190, y + 5), shree_str, fill=(0, 0, 0), font=shree_font)

img.save('scratch/shreelipi_telugu/test_consonants.png')
print("Saved scratch/shreelipi_telugu/test_consonants.png")
