from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 32)
label_font = ImageFont.load_default()

bases = [
    ('ka', 'a'), ('kha', 'Q'), ('ga', 'V'), ('gha', 'R'), 
    ('ca', '^'), ('cha', 'b'), ('ja', '\\'), ('jha', 'm'), ('nya', 'p'),
    ('Ta', 'r'), ('Tha', 'u'), ('Da', 'y'), ('Dha', '|'), ('Na', '~'),
    ('ta', '™'), ('tha', '£'), ('da', '§'), ('dha', '®'), ('na', '¯'),
    ('pa', '²'), ('pha', '¸'), ('ba', 'º'), ('bha', '¿'), ('ma', 'Ä'),
    ('ya', 'Å'), ('ra', 'ˆ'), ('la', 'Ë'), ('va', 'Ð'),
    ('sha', 'Ô'), ('Sa', 'Ù'), ('sa', 'Ü'), ('ha', '˜'), ('La', 'Ã'),
    ('ksha', '„')
]

# matras as per MATRA_MAP
matras = {
    'aa': 'é', 
    'i': 'ì', 
    'ii': 'í', 
    'u': 'î', 
    'uu': 'ï', 
    'e': 'ð', 
    'ee': 'ñ', 
    'ai': 'ò', 
    'o': 'ö', 
    'oo': 'ø', 
    'au': 'ú', 
    'ru': '#'
}

img = Image.new('RGB', (1600, 2000), (255, 255, 255))
draw = ImageDraw.Draw(img)

# headers
x = 100
for name in matras.keys():
    draw.text((x, 10), name, fill=(0,0,200), font=label_font)
    x += 100

y = 40
for name, base_ch in bases:
    draw.text((10, y + 10), name, fill=(0,0,200), font=label_font)
    x = 100
    for m_name, m_ch in matras.items():
        # First try base + matra without talakattu
        # (Our current logic puts matra without talakattu for base characters)
        text = base_ch + m_ch
        draw.text((x, y), text, fill=(0,0,0), font=shree_font)
        x += 100
    y += 50

img.save('scratch/shree_telugu_vowel_matrix.png')
print("Saved scratch/shree_telugu_vowel_matrix.png")
