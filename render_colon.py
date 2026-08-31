from PIL import Image, ImageDraw, ImageFont
import urllib.parse
from pathlib import Path

def draw_test():
    font_path = "public/AnuSM main/ttf/NEOGANBO.TTF"
    font = ImageFont.truetype(font_path, 60)
    
    img = Image.new('RGB', (400, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # Text 1: Just digits with standard colon
    text1 = chr(0xf030) + chr(0xf03a) + " " + chr(0xf031) + chr(0xf03a)  # 0: 1:
    
    # Text 2: Digits with A-matra + colon? Wait, A-matra is 0xf0e4 in PUA? No, 0xf0e4 is nukta, A-matra is 0xf0e3 or 0xf0e5?
    # Let's check how "dash and two dots" is made in Anu fonts.
    # What if the user meant: there is a shirorekha (dash) above the two dots?
    # There is a special character for colon-with-shirorekha, OR maybe colon (0xf03a) doesn't have shirorekha, but what does have shirorekha?
    
    draw.text((20, 20), text1, font=font, fill='black')
    
    img.save("test_colon_render.png")
    print("Saved test_colon_render.png")

draw_test()
