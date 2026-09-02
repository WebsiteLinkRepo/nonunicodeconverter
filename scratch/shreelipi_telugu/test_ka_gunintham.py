import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 24)
noto_font = ImageFont.truetype(ref_font_path, 24)
label_font = ImageFont.load_default()

# Let's test all vowel combinations (Gunintham) for 'క' (Ka)
# క కా కి కీ కు కూ కృ కౄ కె కే కై కొ కో కౌ కం కః క్

# Matras in Shree-Tel:
# Base: 'a'
# Talakattu (default a): '\xE6'
# ా (aa): '\xE9' or '\xEA' or '\xEB' or '\xFA'?
# ి (i): '\xEC'
# ీ (ii): '\xED'
# ు (u): '\xF0'
# ూ (uu): '\xF3'
# ృ (ru): '#'
# ె (e): '\xF6'
# ే (ee): '\xF7'
# ై (ai): '\xF8'
# ొ (o): '\xF9'
# ో (oo): '\xFA'
# ౌ (au): '\xFB' or 'a\xF6\x6F'
# ం (m): '\xC6'
# ః (h): 'O' or '@'
# క్ (halant): 'a\xA2' or 'a\xE6\xA2'

tests = [
    ('క (ka)', 'a\xE6'),
    ('కా (kaa)', 'a\xE9'),
    ('కి (ki)', 'a\xEC'),
    ('కీ (kii)', 'a\xED'),
    ('కు (ku)', 'a\xF0'),
    ('కూ (kuu)', 'a\xF3'),
    ('కృ (kru)', 'a#'),
    ('కె (ke)', 'a\xF6'),
    ('కే (kee)', 'a\xF7'),
    ('కై (kai)', 'a\xF8'),
    ('కొ (ko)', 'a\xF9'),
    ('కో (koo)', 'a\xFA'),
    ('కౌ (kau)', 'a\xFB'),
    ('కం (kam)', 'a\xE6\xC6'),
    ('కః (kah)', 'a\xE6:'),
    ('క్ (k)', 'a\xA2'),
    ('క్క (kka)', 'a\xE6Œ'),
    ('క్త్ర (ktra)', 'a\xE6‰'),
    ('క్ర (kra)', 'a\xE6–'),
    ('క్ల (kla)', 'a\xE6Ï'),
    ('క్వ (kva)', 'a\xE6Ó'),
    ('క్ష (ksha)', '„\xE6'),
    ('క్ష్మ (kshma)', '„\xE6š'),
]

img = Image.new('RGB', (800, len(tests) * 45 + 40), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (label, shree_str) in enumerate(tests):
    y = 20 + i * 45
    draw.text((20, y), label, fill=(0, 0, 150), font=noto_font)
    draw.text((250, y), f"Shree:", fill=(100, 100, 100), font=label_font)
    draw.text((320, y), shree_str, fill=(0, 0, 0), font=shree_font)

img.save('scratch/shreelipi_telugu/test_ka_gunintham.png')
print("Saved scratch/shreelipi_telugu/test_ka_gunintham.png")
