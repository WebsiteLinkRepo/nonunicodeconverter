from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 60)
img = Image.new('RGB', (800, 400), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# f0a2 (फ), f0a7 (भ), f0a4 (ब), f067 (ड), f062 (ट)
chars = [0xF0A2, 0xF0A7, 0xF0A4, 0xF067, 0xF062]
for i, c in enumerate(chars):
    text = chr(c) + chr(0xF0DD)  # + ra stroke
    draw.text((20 + i*150, 20), text, font=font, fill=(0, 0, 0))
    
    # Try with halant + ra instead?
    # Actually just render the base character to see what it is
    draw.text((20 + i*150, 100), chr(c), font=font, fill=(0, 0, 0))

img.save('ligatures_test.png')
