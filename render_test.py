from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('public/AnuSM/ttf/NEOGANBO.TTF', 32)
text = """    
    
     
     
    
    
"""

img = Image.new('RGB', (800, 400), color = 'white')
d = ImageDraw.Draw(img)
d.text((10,10), text, font=font, fill='black', spacing=10)
img.save('output_rendered.png')
