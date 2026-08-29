from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 60)
img = Image.new('RGB', (1000, 800), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

ranges = [
    range(0x80, 0x90),
    range(0x90, 0xA0),
    range(0xA0, 0xB0),
    range(0xB0, 0xC0),
    range(0xC0, 0xD0),
    range(0xD0, 0xE0),
    range(0xE0, 0xF0),
    range(0xF0, 0x100)
]

for row, r in enumerate(ranges):
    for col, val in enumerate(r):
        text = chr(0xF000 + val)
        draw.text((col * 60 + 20, row * 100 + 20), text, font=font, fill=(0, 0, 0))
        draw.text((col * 60 + 20, row * 100 + 70), hex(val)[2:], font=ImageFont.load_default(), fill=(255, 0, 0))

img.save('dya_all.png')
