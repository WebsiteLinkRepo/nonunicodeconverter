from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)
font_label = ImageFont.load_default()

items = [
    ("¸ (0xB8)", "¸"),
    ("¸$ (0xB8 + $)", "¸$"),
    ("¹ (0xB9)", "¹"),
    ("¹$ (0xB9 + $)", "¹$"),
    ("H«$ (H + « + $)", "H«$"),
    ("Šd (Š + d)", "Šd"),
    ("Šdm§Q>_ (Š + d + m + § + Q + > + _)", "Šdm§Q>_"),
    ("Šdma (Š + d + m + a)", "Šdma"),
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y+25), label, fill=(100, 100, 100))
    draw.text((450, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save('scratch/test_kka_kra_kva.png')
print('Saved scratch/test_kka_kra_kva.png')
