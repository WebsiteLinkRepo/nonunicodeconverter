from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 80)
img = Image.new('RGB', (800, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# f09b f0dd f0fe f0e7 f07b f08d f0e7 f07a f075 f054 f04e f0fe f079
text = "".join(chr(c) for c in [0xf09b, 0xf0dd, 0xf0fe, 0xf0e7, 0xf07b, 0xf08d, 0xf0e7, 0xf07a, 0xf075, 0xf054, 0xf04e, 0xf0fe, 0xf079])
draw.text((20, 20), text, font=font, fill=(0, 0, 0))

img.save('full_test.png')
