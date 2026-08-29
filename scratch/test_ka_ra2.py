from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 60)
img = Image.new('RGB', (400, 200), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# f04e (क) + f0dd (्र)
draw.text((20, 20), chr(0xF04E) + chr(0xF0DD), font=font, fill=(0, 0, 0))

# f0b2 (क्र)
draw.text((150, 20), chr(0xF0B2), font=font, fill=(0, 0, 0))

img.save('ka_ra_test2.png')
