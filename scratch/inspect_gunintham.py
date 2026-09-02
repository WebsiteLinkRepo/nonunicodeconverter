from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 30)
label_font = ImageFont.load_default()

# Matras to test:
# aa: 'é', i: 'ì', ii: 'í', u: 'î', uu: 'ï', e: 'ð', ee: 'ñ', ai: 'ò', o: 'ö', oo: 'ø', au: 'ú', ru: '#'
matras = [
    ('none', ''),
    ('talakattu', 'æ'),
    ('aa (é)', 'é'),
    ('i (ì)', 'ì'),
    ('ii (í)', 'í'),
    ('u (î)', 'î'),
    ('uu (ï)', 'ï'),
    ('e (ð)', 'ð'),
    ('ee (ñ)', 'ñ'),
    ('ai (ò)', 'ò'),
    ('o (ö)', 'ö'),
    ('oo (ø)', 'ø'),
    ('au (ú)', 'ú'),
    ('ru (#)', '#'),
]

consonants = [
    ('క', 'a'),
    ('గ', 'V'),
    ('చ', '^'),
    ('త', '™'),
    ('ద', '§'),
    ('న', '¯'),
    ('ప', '²'),
    ('మ', 'Ä'),
    ('య', 'Å'),
    ('ర', 'ˆ'),
    ('ల', 'Ë'),
    ('వ', 'Ð'),
    ('స', 'Ü'),
    ('హ', '˜'),
]

cell_w = 90
cell_h = 70
cols = len(matras) + 1
rows = len(consonants) + 1

img = Image.new('RGB', (cols * cell_w + 40, rows * cell_h + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Headers
for c_idx, (m_label, m_char) in enumerate(matras):
    x = 100 + c_idx * cell_w
    draw.text((x + 5, 10), m_label, fill=(0, 0, 150), font=label_font)

for r_idx, (c_label, c_char) in enumerate(consonants):
    y = 40 + r_idx * cell_h
    draw.text((10, y + 20), f"{c_label} ({c_char})", fill=(150, 0, 0), font=label_font)
    
    for c_idx, (m_label, m_char) in enumerate(matras):
        x = 100 + c_idx * cell_w
        draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(230, 230, 230))
        
        # render c_char + m_char
        text_to_draw = c_char + m_char
        try:
            draw.text((x + 25, y + 15), text_to_draw, fill=(0, 0, 0), font=shree_font)
        except Exception as e:
            draw.text((x + 5, y + 20), "ERR", fill=(255, 0, 0), font=label_font)

img.save('scratch/gunintham_grid.png')
print("Saved gunintham grid to scratch/gunintham_grid.png")
