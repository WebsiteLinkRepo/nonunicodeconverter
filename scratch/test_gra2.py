from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 80)
img = Image.new('RGB', (400, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

text = chr(0xF054) + chr(0xF0DD)
draw.text((20, 20), text, font=font, fill=(0, 0, 0))

img.save('gra_test2.png')
