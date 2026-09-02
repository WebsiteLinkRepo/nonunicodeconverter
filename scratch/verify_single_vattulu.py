from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 36)
noto_font = ImageFont.truetype(noto_path, 30)
label_font = ImageFont.load_default()

# Vattulu mapping candidates to verify:
# (Telugu Unicode, Vattu char in Shree, Decimal, Hex)
vattu_candidates = [
    ('క్క', 'aŒ', 0x152), # ka-vattu
    ('క్ఖ', 'aU', 0x55),   # kha-vattu
    ('క్గ', 'aW', 0x57),   # ga-vattu
    ('క్ఘ', 'aœ', 0x153), # gha-vattu
    ('క్ఙ', 'aZ', 0x5A),   # nga-vattu
    ('క్చ', 'ae', 0x65),   # ca-vattu
    ('క్ఛ', 'ad', 0x64),   # cha-vattu
    ('క్జ', 'aj', 0x6A),   # ja-vattu
    ('క్ఝ', 'an', 0x6E),   # jha-vattu
    ('క్ఞ', 'aq', 0x71),   # nya-vattu
    ('క్ట', 'as', 0x73),   # Ta-vattu
    ('క్ఠ', 'ax', 0x78),   # Tha-vattu
    ('క్డ', 'az', 0x7A),   # Da-vattu
    ('క్ఢ', 'a{', 0x7B),   # Dha-vattu
    ('క్ణ', 'aŠ', 0x160), # Na-vattu
    ('క్త', 'aª', 0xAA),  # ta-vattu
    ('క్థ', 'a¦', 0xA6),  # tha-vattu
    ('క్ద', 'a§', 0xA7),  # da-vattu? Wait, da-vattu is it 0xAA or 0xA7 or something else?
    ('క్ధ', 'aÉ', 0xC9),  # dha-vattu
    ('క్న', 'aÝ', 0xDD),  # na-vattu
    ('క్ప', 'aµ', 0xB5),  # pa-vattu
    ('క్ఫ', 'a¹', 0xB9),  # pha-vattu
    ('క్బ', 'a¾', 0xBE),  # ba-vattu
    ('క్భ', 'aÂ', 0xC2),  # bha-vattu
    ('క్మ', 'aš', 0x161), # ma-vattu
    ('క్య', 'aŸ', 0x178), # ya-vattu
    ('క్ర', 'a–', 0x2013),# ra-vattu
    ('క్ల', 'aÏ', 0xCF),  # la-vattu
    ('క్వ', 'aÓ', 0xD3),  # va-vattu
    ('క్శ', 'aØ', 0xD8),  # sha-vattu
    ('క్ష', 'aÛ', 0xDB),  # Sa-vattu
    ('క్స', 'aÞ', 0xDE),  # sa-vattu
    ('క్హ', 'aå', 0xE5),  # ha-vattu
    ('క్ళ', 'aÃ', 0xC3),  # La-vattu
    ('క్క్ష', 'a<', 0x3C), # ksha-vattu
    ('క్ఱ', 'a‚', 0x201A),# rra-vattu
]

cols = 4
rows = (len(vattu_candidates) + cols - 1) // cols
cell_w, cell_h = 240, 100

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (uni, shree_str, code) in enumerate(vattu_candidates):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 6, y + 6), f"0x{code:02X} ({code})", fill=(100, 100, 100), font=label_font)
    draw.text((x + 10, y + 25), uni, fill=(0, 0, 150), font=noto_font)
    draw.text((x + 120, y + 20), shree_str, fill=(0, 0, 0), font=shree_font)

img.save('scratch/vattu_candidates_test.png')
print("Saved scratch/vattu_candidates_test.png")
