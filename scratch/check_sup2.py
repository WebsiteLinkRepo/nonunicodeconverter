from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

# Render characters with ² (0xB2) vs ~ (0x7E)
items = [
    ("H$² (k+halant)", "H$²"),
    ("X² (d+halant)", "X²"),
    ("T² (dh+halant)", "T²>"),
    ("Q² (t+halant)", "Q²>"),
    ("h² (h+halant)", "h²"),
    ("H$~ (k+ba)", "H$~"),
    ("X~ (d+ba)", "X~"),
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y), label, fill=(150, 150, 150))
    draw.text((300, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save("scratch/check_sup2.png")
print("Saved scratch/check_sup2.png")
