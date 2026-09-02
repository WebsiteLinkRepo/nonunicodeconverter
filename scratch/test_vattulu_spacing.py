from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 32)
label_font = ImageFont.load_default()

test_cases = [
    # Various consonants + vattulu
    ("k + ka_vattu", 'aŒ'),
    ("k + ta_vattu", 'aª'),
    ("k + ma_vattu", 'aš'),
    ("v + va_vattu", 'ÐÓ'),
    ("m + ya_vattu", 'ÄŸ'),
    ("t + ra_vattu", '™–'),
    ("s + th_vattu", 'ÜÛ'),
    # combinations without talakattu
    ("k + æ + ka_vattu", 'aæŒ'),
    ("k + ka_vattu + æ", 'aŒæ'),
]

img = Image.new('RGB', (600, 400), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, text in test_cases:
    draw.text((20, y), label, fill=(100, 100, 100), font=label_font)
    try:
        draw.text((200, y - 5), text, fill=(0, 0, 0), font=shree_font)
    except:
        pass
    y += 40

img.save('scratch/test_vattu_spacing.png')
print("Saved scratch/test_vattu_spacing.png")
