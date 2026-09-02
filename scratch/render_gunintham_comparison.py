from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 26)
noto_font = ImageFont.truetype(noto_path, 22)
label_font = ImageFont.load_default()

with open('scratch/gunintham_output.txt', 'r', encoding='utf-8') as f:
    lines = [l.strip().split('\t') for l in f if l.strip()]

# 612 items: 36 consonants * 17 vowel signs
# Let's arrange as 36 rows (one per consonant) and 17 columns (one per vowel sign)
consonants_count = 36
vowels_count = 17

cell_w = 110
cell_h = 75
grid_w = vowels_count * cell_w + 40
grid_h = consonants_count * cell_h + 60

img = Image.new('RGB', (grid_w, grid_h), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Vowel headers
vowel_names = ['a', 'aa', 'i', 'ii', 'u', 'uu', 'ru', 'ruu', 'e', 'ee', 'ai', 'o', 'oo', 'au', 'am', 'ah', 'virama']
for v_idx, v_name in enumerate(vowel_names):
    x = 20 + v_idx * cell_w
    draw.text((x + 10, 10), v_name, fill=(0, 0, 150), font=label_font)

for idx, (uni, converted) in enumerate(lines):
    row = idx // vowels_count
    col = idx % vowels_count
    x = 20 + col * cell_w
    y = 40 + row * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(230, 230, 230))
    # Unicode (Noto) in blue
    draw.text((x + 5, y + 4), uni, fill=(0, 50, 150), font=noto_font)
    # Shree-Tel in black
    try:
        draw.text((x + 5, y + 38), converted, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        draw.text((x + 5, y + 38), "ERR", fill=(255, 0, 0), font=label_font)

img.save('scratch/full_gunintham_verification.png')
print(f"Saved scratch/full_gunintham_verification.png ({grid_w}x{grid_h})")
