from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 80)
img = Image.new('RGB', (1000, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

chars = [0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7]
text = " ".join(chr(0xF000 + c) for c in chars)
draw.text((20, 20), text, font=font, fill=(0, 0, 0))

img.save('dump2.png')
