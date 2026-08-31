from PIL import Image, ImageDraw, ImageFont

font_path = "public/AnuSM main/ttf/NEOGANBO.TTF"
font = ImageFont.truetype(font_path, 40)

# Let's test all characters in PUA range that could be colon, visarga, dash+dots, etc.
import fontTools.ttLib as ttLib

tt = ttLib.TTFont(font_path)
cmap = tt.getBestCmap()

# Let's render all chars in cmap around 0xf020 to 0xf0ff
for start in range(0xf020, 0xf100, 32):
    img = Image.new('RGB', (1000, 80), color='white')
    draw = ImageDraw.Draw(img)
    x = 10
    for cp in range(start, min(start + 32, 0xf100)):
        if cp in cmap:
            name = cmap[cp]
            ch = chr(cp)
            draw.text((x, 10), f"{hex(cp)[2:]}", font=ImageFont.load_default(), fill='gray')
            draw.text((x, 25), ch, font=font, fill='black')
        x += 30
    img.save(f"glyphs_{hex(start)}.png")

