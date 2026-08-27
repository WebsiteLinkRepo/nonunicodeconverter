from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 100)
for i in range(32, 256):
    img = Image.new('RGB', (100, 100), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), chr(61440 + i), font=font, fill=(0, 0, 0))
    img.save(f'char_{i}.png')
