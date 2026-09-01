from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

# Render ~ (0x7e), b (0x62), ^ (0x5e), ~b, V~
items = [
    ("~ (tilde)", "~"),
    ("b (lower b)", "b"),
    ("B (upper B)", "B"),
    ("V~", "V~"),
    ("Vb", "Vb")
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y), label, fill=(150, 150, 150))
    draw.text((300, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save("scratch/verify_tilde.png")
print("Saved scratch/verify_tilde.png")
