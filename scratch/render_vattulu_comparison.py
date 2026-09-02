from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 26)
noto_font = ImageFont.truetype(noto_path, 22)
label_font = ImageFont.load_default()

with open('scratch/vattulu_output.txt', 'r', encoding='utf-8') as f:
    lines = [l.strip().split('\t') for l in f if l.strip()]

# 1296 items: 36 consonants * 36 vattulu
consonants_count = 36
vattulu_count = 36

cell_w = 110
cell_h = 75
grid_w = vattulu_count * cell_w + 40
grid_h = consonants_count * cell_h + 60

img = Image.new('RGB', (grid_w, grid_h), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (uni, converted) in enumerate(lines):
    row = idx // vattulu_count
    col = idx % vattulu_count
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

img.save('scratch/full_vattulu_verification.png')
print(f"Saved scratch/full_vattulu_verification.png ({grid_w}x{grid_h})")
