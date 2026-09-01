from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

# glyph00122 is at 0x9d - it's a short horizontal shirorekha extension!
# Let's see what it looks like and how it pairs with various Devanagari chars

img = Image.new('RGB', (700, 250), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

ext = chr(0x9d)

# Draw: isolated, then paired with various chars
samples = [
    (10, "ext alone", ext),
    (80, "sa+ext", "g" + ext),
    (200, "ma+ext", "_" + ext),
    (320, "ha+ext", "h" + ext),
    (440, "ya+ext", "`" + ext),
    (560, "da+ext", "X" + ext),
]

for x, label, txt in samples:
    draw.text((x, 80), txt, font=font, fill=(0,0,0))

img.save("scratch/shirorekha_ext_test.png")
print("Saved shirorekha_ext_test.png")
