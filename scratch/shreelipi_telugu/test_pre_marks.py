import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

# In Telugu Shree-Lipi fonts, 'e' and 'ee' matras often go BEFORE the base consonant!
# Let's test prepending marks!
pre_marks = [
    (chr(0xE6), "0xE6 + a"),
    (chr(0xE7), "0xE7 + a"),
    (chr(0xE8), "0xE8 + a"),
    (chr(0xE9), "0xE9 + a"),
    (chr(0xEA), "0xEA + a"),
    (chr(0xEB), "0xEB + a"),
    (chr(0xEC), "0xEC + a"),
    (chr(0xED), "0xED + a"),
    (chr(0xEE), "0xEE + a"),
    (chr(0xEF), "0xEF + a"),
    (chr(0xF0), "0xF0 + a"),
    (chr(0xF3), "0xF3 + a"),
    (chr(0xF4), "0xF4 + a"),
    (chr(0xF6), "0xF6 + a"),
    (chr(0xF7), "0xF7 + a"),
    (chr(0xFA), "0xFA + a"),
    (chr(0xFB), "0xFB + a"),
]

img = Image.new('RGB', (1000, len(pre_marks) * 60 + 20), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (m, desc) in enumerate(pre_marks):
    y = i * 60 + 10
    test_str = m + 'a'
    draw.text((20, y), desc, fill=(80, 80, 80), font=label_font)
    try:
        draw.text((300, y), test_str, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        pass

img.save('scratch/shreelipi_telugu/test_pre_marks.png')
print("Rendered test_pre_marks.png")
