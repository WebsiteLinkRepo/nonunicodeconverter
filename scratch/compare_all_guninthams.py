from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 28)
noto_font = ImageFont.truetype(noto_path, 24)
label_font = ImageFont.load_default()

# Let's import our ts converter or write a test python equivalent to see what it generates
import subprocess
import json

# Let's test all consonants with all vowels in Telugu
consonants = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ',
    'చ', 'ఛ', 'జ', 'ఝ', 'ఞ',
    'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
    'త', 'థ', 'ద', 'ధ', 'న',
    'ప', 'ఫ', 'బ', 'భ', 'మ',
    'య', 'ర', 'ల', 'వ',
    'శ', 'ష', 'స', 'హ', 'ళ', 'క్ష', 'ఱ'
]

vowels = [
    ('', 'a'), ('ా', 'aa'), ('ి', 'i'), ('ీ', 'ii'),
    ('ు', 'u'), ('ూ', 'uu'), ('ృ', 'ru'), ('ౄ', 'ruu'),
    ('ె', 'e'), ('ే', 'ee'), ('ై', 'ai'),
    ('ొ', 'o'), ('ో', 'oo'), ('ౌ', 'au'),
    ('ం', 'am'), ('ః', 'ah'), ('్', 'halant')
]

# Let's generate the TS output for all these combinations
test_words = []
for c in consonants:
    for v_sign, v_name in vowels:
        test_words.append(c + v_sign)

# Write to a file
with open('scratch/gunintham_input.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(test_words))

print(f"Generated {len(test_words)} combinations in scratch/gunintham_input.txt")
