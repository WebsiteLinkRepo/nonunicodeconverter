from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 28)
noto_font = ImageFont.truetype(noto_path, 24)
label_font = ImageFont.load_default()

# Let's test all consonants with all vattulu in Telugu
consonants = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ',
    'చ', 'ఛ', 'జ', 'ఝ', 'ఞ',
    'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
    'త', 'థ', 'ద', 'ధ', 'న',
    'ప', 'ఫ', 'బ', 'భ', 'మ',
    'య', 'ర', 'ల', 'వ',
    'శ', 'ష', 'స', 'హ', 'ళ', 'క్ష', 'ఱ'
]

vattulu = [
    '్క', '్ఖ', '్గ', '్ఘ', '్ఙ',
    '్చ', '్ఛ', '్జ', '్ఝ', '్ఞ',
    '్ట', '్ఠ', '్డ', '్ఢ', '్ణ',
    '్త', '్థ', '్ద', '్ధ', '్న',
    '్ప', '్ఫ', '్బ', '్భ', '్మ',
    '్య', '్ర', '్ల', '్వ',
    '్శ', '్ష', '్స', '్హ', '్ళ', '్క్ష', '్ఱ'
]

# Let's generate the TS output for combinations: base consonant + talakattu + vattu
# In telugu, base consonant followed by virama + consonant is a conjunct.
test_words = []
for c in consonants:
    for v_sign in vattulu:
        test_words.append(c + v_sign)

# Write to a file
with open('scratch/vattulu_input.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(test_words))

print(f"Generated {len(test_words)} combinations in scratch/vattulu_input.txt")
