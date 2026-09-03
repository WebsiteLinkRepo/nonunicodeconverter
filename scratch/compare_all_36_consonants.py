from PIL import Image, ImageDraw, ImageFont

SHREE_PATH = "public/SHREE-TEL.ttf"
REF_PATH = "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"

shree_font = ImageFont.truetype(SHREE_PATH, 44)
ref_font = ImageFont.truetype(REF_PATH, 44)
label_font = ImageFont.load_default()

# All 36 Telugu consonants in Step 2:
consonants = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ', 'చ', 'ఛ', 'జ', 'ఝ', 'ఞ', 'ట', 'ఠ',
    'డ', 'ఢ', 'ణ', 'త', 'థ', 'ద', 'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ',
    'మ', 'య', 'ర', 'ఱ', 'ల', 'ళ', 'వ', 'శ', 'ష', 'స', 'హ', 'క్ష'
]

# We will test various candidates for each consonant in Shree-Tel font
# Format: uni_char: [(description, shree_string)]
candidates = {
    'క': [('0x4d+e6', chr(0x4d) + chr(0xe6))],
    'ఖ': [('0x51', chr(0x51)), ('0x52', chr(0x52))],
    'గ': [('0x56+e6', chr(0x56) + chr(0xe6))],
    'ఘ': [
        ('0x50+e6', chr(0x50) + chr(0xe6)),
        ('0x50+e9', chr(0x50) + chr(0xe9)),
        ('0xb4+e6', chr(0xb4) + chr(0xe6)),
        ('0xb5+e6', chr(0xb5) + chr(0xe6)),
        ('0x52+e6', chr(0x52) + chr(0xe6)),
        ('0x62+e6', chr(0x62) + chr(0xe6)),
        ('0x51+24', chr(0x51) + chr(0x24)),
    ],
    'ఙ': [
        ('0x5a', chr(0x5a)),
        ('0x5a+e6', chr(0x5a) + chr(0xe6)),
        ('0x66', chr(0x66)),
        ('0x5c', chr(0x5c)),
        ('0x49', chr(0x49)),
        ('0x4a', chr(0x4a)),
    ],
    'చ': [('0x5e+e6', chr(0x5e) + chr(0xe6)), ('0x61+e6', chr(0x61) + chr(0xe6))],
    'ఛ': [('0x62', chr(0x62)), ('0x62+e6', chr(0x62) + chr(0xe6))],
    'జ': [('0x66', chr(0x66)), ('0x5c+e6', chr(0x5c) + chr(0xe6))],
    'ఝ': [('0x6d', chr(0x6d)), ('0x6d+e6', chr(0x6d) + chr(0xe6))],
    'ఞ': [('0x70', chr(0x70)), ('0x70+e6', chr(0x70) + chr(0xe6))],
    'ట': [('0x72', chr(0x72)), ('0x73', chr(0x73))],
    'ఠ': [('0x75+e6', chr(0x75) + chr(0xe6))],
    'డ': [('0x79+e6', chr(0x79) + chr(0xe6))],
    'ఢ': [('0xc9+e6', chr(0xc9) + chr(0xe6))],
    'ణ': [('0xd7', chr(0xd7)), ('0xd8+e6', chr(0xd8) + chr(0xe6)), ('0x7e', chr(0x7e))],
    'త': [('0x2122+e6', chr(0x2122) + chr(0xe6)), ('0x2020+e6', chr(0x2020) + chr(0xe6))],
    'థ': [('0xa3+e6', chr(0xa3) + chr(0xe6))],
    'ద': [('0xa7+e6', chr(0xa7) + chr(0xe6)), ('0xa8', chr(0xa8))],
    'ధ': [
        ('0xa3+24', chr(0xa3) + chr(0x24)),
        ('0xa3+e6+24', chr(0xa3) + chr(0xe6) + chr(0x24)),
        ('0xa3+e6+bottom', chr(0xa3) + chr(0xe6) + chr(0x2f)),
        ('0xa3+e6+a2', chr(0xa3) + chr(0xe6) + chr(0xa2)),
        ('0xa3+e6+2c', chr(0xa3) + chr(0xe6) + chr(0x2c)),
        ('0xa3+e6+ad', chr(0xa3) + chr(0xe6) + chr(0xad)),
        ('0xa3+e6+b7', chr(0xa3) + chr(0xe6) + chr(0xb7)),
        ('0xbf+e6', chr(0xbf) + chr(0xe6)),
        ('0xae', chr(0xae)),
    ],
    'న': [('0xaf+e6', chr(0xaf) + chr(0xe6))],
    'ప': [('0xb2+e6', chr(0xb2) + chr(0xe6)), ('0xb3+e6', chr(0xb3) + chr(0xe6)), ('0xb4+e6', chr(0xb4) + chr(0xe6))],
    'ఫ': [('0xb8', chr(0xb8)), ('0xb9+e6', chr(0xb9) + chr(0xe6))],
    'బ': [('0xbb+e6', chr(0xbb) + chr(0xe6)), ('0xba', chr(0xba))],
    'భ': [('0xbf+e6', chr(0xbf) + chr(0xe6)), ('0xc0', chr(0xc0))],
    'మ': [
        ('0x47+e6', chr(0x47) + chr(0xe6)),
        ('0x48+e6', chr(0x48) + chr(0xe6)),
        ('0xb2+e6', chr(0xb2) + chr(0xe6)),
        ('0xb3+e6', chr(0xb3) + chr(0xe6)),
        ('0xb4+e6', chr(0xb4) + chr(0xe6)),
        ('0xb5+e6', chr(0xb5) + chr(0xe6)),
        ('0xc4+e6', chr(0xc4) + chr(0xe6)),
        ('0x46', chr(0x46)),
    ],
    'య': [('0xc5+e6', chr(0xc5) + chr(0xe6)), ('0xc4+e6', chr(0xc4) + chr(0xe6))],
    'ర': [('0xc6+e6', chr(0xc6) + chr(0xe6))],
    'ఱ': [('0x201a', chr(0x201a))],
    'ల': [('0xcc', chr(0xcc)), ('0xcb+e6', chr(0xcb) + chr(0xe6))],
    'ళ': [('0xe2+e6', chr(0xe2) + chr(0xe6))],
    'వ': [('0xd0+e6', chr(0xd0) + chr(0xe6))],
    'శ': [('0xd4+e6', chr(0xd4) + chr(0xe6))],
    'ష': [('0xd9+e6', chr(0xd9) + chr(0xe6)), ('0x201e', chr(0x201e))],
    'స': [('0xdc+e6', chr(0xdc) + chr(0xe6))],
    'హ': [
        ('0xdf+e6', chr(0xdf) + chr(0xe6)),
        ('0xe0', chr(0xe0)),
        ('0xe1+e6', chr(0xe1) + chr(0xe6)),
        ('0x2dc+e6', chr(0x2dc) + chr(0xe6)),
        ('0x2dc', chr(0x2dc)),
    ],
    'క్ష': [('0x201e+e6', chr(0x201e) + chr(0xe6)), ('0x22+e6', chr(0x22) + chr(0xe6))],
}

rows = len(consonants)
img = Image.new("RGB", (1400, rows * 60 + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, c in enumerate(consonants):
    y = 20 + idx * 60
    draw.line([(0, y - 5), (1400, y - 5)], fill=(230, 230, 230))
    
    # 1. Unicode Reference
    draw.text((20, y), c, fill=(0, 120, 0), font=ref_font)
    draw.text((80, y + 15), f"Uni: {c}", fill=(100, 100, 100), font=label_font)
    
    # 2. Candidates in Shree-Lipi
    x = 180
    c_list = candidates.get(c, [])
    for desc, s in c_list:
        draw.text((x, y - 2), desc, fill=(150, 0, 0), font=label_font)
        try:
            draw.text((x, y + 10), s, fill=(0, 0, 0), font=shree_font)
        except Exception as e:
            draw.text((x, y + 10), "ERR", fill=(255, 0, 0), font=label_font)
        x += 130

img.save("scratch/consonants_comparison_full.png")

# Slice into 2 halves for easy reading
h = img.size[1]
img.crop((0, 0, img.size[0], h // 2)).save("scratch/cons_comp_top.png")
img.crop((0, h // 2, img.size[0], h)).save("scratch/cons_comp_bot.png")
print("Saved consonants_comparison_full.png, cons_comp_top.png, cons_comp_bot.png")
