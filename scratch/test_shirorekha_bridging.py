from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

ext = chr(0x9D) # The bridge

# Problematic cases mentioned: म+म (underscore+underscore), स (g), ह (h), द (X)
# Let's test gaps between them
pairs = [
    ("म_म", "_ _"),
    ("म_ext_म", "_" + ext + "_"),
    ("स_स", "g g"),
    ("स_ext_स", "g" + ext + "g"),
    ("ह_ह", "h h"),
    ("ह_ext_ह", "h" + ext + "h"),
    ("द_द", "X X"),
    ("द_ext_द", "X" + ext + "X"),
]

img = Image.new('RGB', (1000, 300), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

x = 20
for label, txt in pairs:
    draw.text((x, 50), label, font=font, fill=(150, 150, 150))
    draw.text((x, 150), txt, font=font, fill=(0, 0, 0))
    x += 200

img.save("scratch/shirorekha_bridging_test.png")
print("Saved scratch/shirorekha_bridging_test.png")
