from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

# Inspect some suspicious vattulu mappings
vattu_chars = [
    ('tha_vattu ¦', 'a¦'),
    ('da_vattu ª', 'aª'),
    ('ta_vattu ª', 'aª'),
    ('dha_vattu É', 'aÉ'),
    ('na_vattu Ý', 'aÝ'),
    ('sa_vattu Þ', 'aÞ'),
    ('ha_vattu å', 'aå'),
    ('la_vattu å', 'aå'),
    ('La_vattu Ã', 'aÃ'),
    ('ksha_vattu <', 'a<'),
    ('rra_vattu ‚', 'a‚')
]

img = Image.new('RGB', (400, 600), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, text in vattu_chars:
    draw.text((10, y), label, fill=(0,0,150), font=label_font)
    draw.text((150, y-5), text, fill=(0,0,0), font=shree_font)
    y += 50

img.save('scratch/vattu_inspect_test.png')
print("Saved scratch/vattu_inspect_test.png")
