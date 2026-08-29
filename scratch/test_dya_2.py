from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 180)
img = Image.new('RGB', (600, 400), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

draw.text((50, 100), chr(0xF08D), font=font, fill=(0, 0, 0))
draw.text((350, 100), chr(0xF0F9), font=font, fill=(0, 0, 0))

img.save('dya_test_2.png')
