from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 80)
img = Image.new('RGB', (200, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

draw.text((20, 20), chr(0xF0FC), font=font, fill=(0, 0, 0))

img.save('dump3.png')
