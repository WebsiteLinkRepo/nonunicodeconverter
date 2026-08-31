import sys
from PIL import Image, ImageDraw, ImageFont

def render(text, filename):
    font = ImageFont.truetype('public/AnuSM/ttf/NEOGANBO.TTF', 64)
    # create a small image
    img = Image.new('RGB', (800, 100), color = 'white')
    d = ImageDraw.Draw(img)
    d.text((10,10), text, font=font, fill='black')
    img.save(filename)

render(chr(0xF04D) + chr(0xF04E) + chr(0xF0FE) + chr(0xF04E) + chr(0xF0FE), 'test_ka.png')
render(chr(0xF0E2) + chr(0xF07E), 'test_halant.png')
render(''.join(chr(i) for i in range(0xF04D, 0xF05A)), 'test_range.png')

