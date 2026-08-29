from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 80)
img = Image.new('RGB', (600, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# f075 + f054
text1 = chr(0xF075) + chr(0xF054)
draw.text((20, 20), text1, font=font, fill=(0, 0, 0))

# f054 + f075
text2 = chr(0xF054) + chr(0xF075)
draw.text((200, 20), text2, font=font, fill=(0, 0, 0))

img.save('matra_test_new.png')
