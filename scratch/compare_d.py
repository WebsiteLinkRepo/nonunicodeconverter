from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

items = [
    ("Ligature Ù (द्म)", "XÙ"),
    ("Halant X²_ (दद्म)", "XX²_"),
    ("विद्वत्ता {dÛÎmm", "{dÛÎmm"),
    ("विद्वत्ता {dÛÎm", "{dÛÎm"),
    ("विद्वत्ता with Îm", "Îm vs Îmm"),
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y), label, fill=(150, 150, 150))
    draw.text((400, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save("scratch/compare_d.png")
print("Saved scratch/compare_d.png")
