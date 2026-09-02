from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 32)
label_font = ImageFont.load_default()

# Get all base consonants
consonant_unicode = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ',
    'చ', 'ఛ', 'జ', 'ఝ', 'ఞ',
    'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
    'త', 'థ', 'ద', 'ధ', 'న',
    'ప', 'ఫ', 'బ', 'భ', 'మ',
    'య', 'ర', 'ల', 'వ',
    'శ', 'ష', 'స', 'హ', 'ళ', 'క్ష', 'ఱ'
]

# Get their shreelipi equivalents from the converter (I can just use the map)
BASE_CONSONANTS = {
  'క': 'a', 'ఖ': 'Q', 'గ': 'V', 'ఘ': 'R', 'ఙ': 'Z',
  'చ': '^', 'ఛ': 'b', 'జ': '\\', 'ఝ': 'm', 'ఞ': 'p',
  'ట': 'r', 'ఠ': 'u', 'డ': 'y', 'ఢ': '|', 'ణ': '~',
  'త': '™', 'థ': '£', 'ద': '§', 'ధ': '®', 'న': '¯',
  'ప': '²', 'ఫ': '¸', 'బ': 'º', 'భ': '¿', 'మ': 'Ä',
  'య': 'Å', 'ర': 'ˆ', 'ల': 'Ë', 'వ': 'Ð',
  'శ': 'Ô', 'ష': 'Ù', 'స': 'Ü', 'హ': '˜', 'ళ': 'Ã',
  'క్ష': '„', 'ఱ': '‚'
}

TALAKATTU = 'æ'

img = Image.new('RGB', (400, 2000), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for uni in consonant_unicode:
    if uni not in BASE_CONSONANTS: continue
    shree = BASE_CONSONANTS[uni]
    
    draw.text((10, y), uni, fill=(0,0,150), font=label_font)
    draw.text((50, y-5), shree + '(no talakattu)', fill=(0,0,0), font=shree_font)
    draw.text((250, y-5), shree + TALAKATTU + '(with talakattu)', fill=(0,0,0), font=shree_font)
    y += 50

img.save('scratch/talakattu_need_test.png')
print("Saved scratch/talakattu_need_test.png")
