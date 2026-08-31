import fontTools.ttLib as ttLib
from PIL import Image, ImageDraw, ImageFont

font_path = 'public/AnuSM/ttf/NEOGANBO.TTF'
font = ttLib.TTFont(font_path)
cmap = font.getBestCmap()
img_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

# Let's inspect specific ranges
ranges = [
    (0xF040, 0xF05F),
    (0xF060, 0xF07F),
    (0xF080, 0xF09F),
    (0xF0A0, 0xF0BF),
    (0xF0C0, 0xF0DF),
    (0xF0E0, 0xF0FF)
]

for idx, (start, end) in enumerate(ranges):
    cps = [cp for cp in range(start, end + 1) if cp in cmap]
    cols = 8
    rows = (len(cps) + cols - 1) // cols
    img = Image.new('RGB', (cols * 100, rows * 80), 'white')
    draw = ImageDraw.Draw(img)
    
    for i, cp in enumerate(cps):
        c = i % cols
        r = i // cols
        x = c * 100
        y = r * 80
        draw.rectangle([x, y, x + 99, y + 79], outline='#ccc')
        draw.text((x + 5, y + 5), f"{hex(cp).upper()} ({cmap[cp]})", fill='#666', font=label_font)
        draw.text((x + 35, y + 25), chr(cp), fill='black', font=img_font)
    
    img.save(f'inspect_part_{idx+1}.png')

print("Saved inspect images!")
