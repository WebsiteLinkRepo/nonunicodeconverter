from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 180)
img = Image.new('RGB', (400, 400), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

text = chr(0xF08D)
draw.text((100, 100), text, font=font, fill=(0, 0, 0))

img.save('dya_test.png')
