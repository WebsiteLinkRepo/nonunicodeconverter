from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

pairs = [
    ("ma-hi-ma", "_h_"),
    ("sa-m-ha", "g_h"),
    ("da-ma-ha", "X_h"),
    ("sa-sa-sa", "ggg")
]

img = Image.new('RGB', (800, 300), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

x = 20
for label, txt in pairs:
    draw.text((x, 50), label, fill=(150, 150, 150))
    draw.text((x, 150), txt, font=font, fill=(0, 0, 0))
    x += 180

img.save("scratch/test_gaps.png")
print("Saved scratch/test_gaps.png")
