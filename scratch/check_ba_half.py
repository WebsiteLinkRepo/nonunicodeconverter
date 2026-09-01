from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

items = [
    ("~ (full ba)", "~"),
    ("ã (half ba)", "ã"),
    ("ã_ (ba+ma)", "ã_"),
    ("~² (ba+halant)", "~²"),
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y), label, fill=(150, 150, 150))
    draw.text((300, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save("scratch/check_ba_half.png")
print("Saved scratch/check_ba_half.png")
