from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 50)
img = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
y = 20
x = 20
for i in range(32, 256):
    draw.text((x, y), chr(61440 + i), font=font, fill=(0, 0, 0))
    x += 60
    if x > 900:
        x = 20
        y += 60

img.save('all_chars.png')
