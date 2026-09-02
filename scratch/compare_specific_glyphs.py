from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)
font_label = ImageFont.load_default()

items = [
    ("¹ (0xB9)", "¹"),
    ("¹$ (0xB9 + 0x24)", "¹$"),
    ("Š (0x8A - half ka)", "Š"),
    ("Šd (half ka + va)", "Šd"),
    ("Šdm (half ka + va + aa)", "Šdm"),
    ("Šdm§ (half ka + va + aa + anusvara)", "Šdm§"),
    ("` (0x60 - ya)", "`"),
    ("w (0x77 - u-matra)", "w"),
    ("`w (0x60 + 0x77)", "`w"),
    ("¶ (0xB6 - alt ya)", "¶"),
    ("¶w (0xB6 + 0x77)", "¶w"),
    ("· (0xB7 - alt ya)", "·"),
    ("·w (0xB7 + 0x77)", "·w"),
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y+25), label, fill=(100, 100, 100))
    draw.text((400, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save('scratch/compare_specific_glyphs.png')
print('Saved scratch/compare_specific_glyphs.png')
