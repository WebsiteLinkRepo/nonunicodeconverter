import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

marks = [
    (chr(0xE6), "0xE6 talakattu"),
    (chr(0xE7), "0xE7 talakattu 2"),
    (chr(0xE8), "0xE8 talakattu 3"),
    (chr(0xFA), "0xFA aa matra"),
    (chr(0xEC), "0xEC i matra"),
    (chr(0xED), "0xED ii matra"),
    (chr(0xF0), "0xF0 u matra"),
    (chr(0xF3), "0xF3 uu matra"),
    (chr(0xE9), "0xE9 o matra/top?"),
    (chr(0xF3), "0xF3 (wait)"),
    (chr(0xF6), "0xF6 ai matra"),
    (chr(0x23), "0x23 vocalic R small"),
    (chr(0x24), "0x24 vocalic R"),
    (chr(0xCF), "0xCF 0xCF la-vattu?"),
    # Let's try compound e/ee/ai/o/oo/au
    (chr(0xF3)+chr(0xE9), "F3+E9"),
    (chr(0xF3)+chr(0x2A), "F3+2A"),
    (chr(0xF0)+chr(0x2A), "F0+2A"),
]

# We also need to find 'e' and 'ee' matras!
e_ee_marks = [
    (chr(0xF2), "0xF2"),
    (chr(0xF3), "0xF3"),
    (chr(0xF4), "0xF4"),
    (chr(0xF5), "0xF5"),
    (chr(0xF6), "0xF6"),
    (chr(0xF7), "0xF7"),
    (chr(0xF8), "0xF8"),
    (chr(0xF9), "0xF9"),
    (chr(0xFA), "0xFA"),
    (chr(0xFB), "0xFB"),
    (chr(0xFC), "0xFC"),
    (chr(0xFD), "0xFD"),
    (chr(0xFE), "0xFE"),
    (chr(0xFF), "0xFF"),
]

img = Image.new('RGB', (1000, len(e_ee_marks) * 60 + 20), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (m, desc) in enumerate(e_ee_marks):
    y = i * 60 + 10
    test_str = 'a' + m
    draw.text((20, y), desc, fill=(80, 80, 80), font=label_font)
    try:
        draw.text((300, y), test_str, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        pass

img.save('scratch/shreelipi_telugu/test_e_matras.png')
print("Rendered test_e_matras.png")
