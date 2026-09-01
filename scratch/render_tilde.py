from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

# Let's render '~', 'b', '~b', '~_', 'X~', 'X', 'Õ', 'Ù'
items = [
    ("~ (tilde)", "~"),
    ("b", "b"),
    ("~b", "~b"),
    ("~_", "~_"),
    ("X", "X"),
    ("X~", "X~"),
    ("X~X~_", "X~X~_"),
    ("~X", "~X"),
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y), label, fill=(150, 150, 150))
    draw.text((300, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save("scratch/render_tilde.png")
print("Saved scratch/render_tilde.png")
