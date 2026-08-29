from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 100)
img = Image.new('RGB', (800, 400), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

chars = range(0xD0, 0xDC)
for i, c in enumerate(chars):
    draw.text((i * 60 + 20, 20), chr(0xF000 + c), font=font, fill=(0, 0, 0))
    draw.text((i * 60 + 20, 150), hex(c)[2:], font=ImageFont.load_default(), fill=(255, 0, 0))

img.save('ha_ligatures.png')
