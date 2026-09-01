from PIL import Image, ImageDraw, ImageFont

font_path = "/home/samuelvictor/Downloads/Shreelipi_4642.TTF"
font = ImageFont.truetype(font_path, 80)

# The user might be talking about certain base letters + halant vs half letters.
# Let's render a few things to figure out what they mean by "for this letter the code is ~"
# Maybe they mean the "bridge" glyph is ~? 
# In Shree-Lipi, `~` is the halant (e.g. क् = H$~). Half-K is `H$`.
# Let's render `~` and `²` and see if `~` is an invisible bridge!
items = [
    ("g_ (sam)", "g_"),
    ("g~ (sa+tilde)", "g~"),
    ("g² (sa+halant?)", "g²"),
    ("g~_ (sa+tilde+ma)", "g~_"),
    ("g²_ (sa+sup2+ma)", "g²_"),
    ("X~_", "X~_"),
    ("X²_", "X²_"),
    ("b~", "b~"),
    ("b²", "b²"),
]

img = Image.new('RGB', (1000, len(items)*100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, txt in items:
    draw.text((20, y), label, fill=(150, 150, 150))
    draw.text((300, y), txt, font=font, fill=(0, 0, 0))
    y += 90

img.save("scratch/check_ligatures.png")
print("Saved scratch/check_ligatures.png")
