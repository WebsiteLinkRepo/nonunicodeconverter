from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

BASE_CONSONANTS = {
  'క': 'a',
  'ఖ': 'Q',
  'గ': 'V',
  'ఘ': 'R',
  'ఙ': 'Z',
  'చ': '^',
  'ఛ': 'b',
  'జ': '\\',
  'ఝ': 'm',
  'ఞ': 'p',
  'ట': 'r',
  'ఠ': 'u',
  'డ': 'y',
  'ఢ': '|',
  'ణ': '~',
  'త': '™',
  'థ': '£',
  'ద': '§',
  'ధ': '®',
  'న': '¯',
  'ప': '²',
  'ఫ': '¸',
  'బ': 'º',
  'భ': '¿',
  'మ': 'Ä',
  'య': 'Å',
  'ర': 'ˆ',
  'ల': 'Ë',
  'వ': 'Ð',
  'శ': 'Ô',
  'ష': 'Ù',
  'స': 'Ü',
  'హ': '˜',
  'ళ': 'Ã',
  'క్ష': '„',
  'ఱ': '‚',
}

img = Image.new('RGB', (1200, 1400), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for uni, ch in BASE_CONSONANTS.items():
    draw.text((20, y), f"{uni} -> '{ch}' (ord {ord(ch)})", fill=(0, 0, 0), font=label_font)
    # standalone
    draw.text((300, y - 10), ch, fill=(0, 0, 0), font=shree_font)
    draw.text((300, y + 35), "alone", fill=(100, 100, 100), font=label_font)
    # with talakattu
    draw.text((500, y - 10), ch + 'æ', fill=(180, 0, 0), font=shree_font)
    draw.text((500, y + 35), "+ talakattu (æ)", fill=(100, 100, 100), font=label_font)
    
    y += 50

img.save('scratch/consonants_test.png')
print("Saved to scratch/consonants_test.png")
