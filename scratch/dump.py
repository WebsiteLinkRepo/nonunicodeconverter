from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 40)
img = Image.new('RGB', (1600, 1600), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i in range(256):
    x = (i % 16) * 100
    y = (i // 16) * 100
    text = chr(0xF000 + i)
    draw.text((x + 20, y + 20), text, font=font, fill=(0, 0, 0))
    draw.text((x, y), hex(i), font=ImageFont.load_default(), fill=(255, 0, 0))

img.save('all_chars.png')
