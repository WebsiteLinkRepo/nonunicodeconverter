import os
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 40)
label_font = ImageFont.load_default()

# Let's test combinations of 'a' (ka) with different marks
marks = [
    ("", "bare 'a'"),
    (chr(0xE6), "a + 0xE6 (talakattu?)"),
    (chr(0xFA), "a + 0xFA (aa matra)"),
    (chr(0x4E), "a + 0x4E (aa matra)"),
    (chr(0xEC), "a + 0xEC (i matra)"),
    (chr(0xED), "a + 0xED (ii matra)"),
    (chr(0xF0), "a + 0xF0 (u matra)"),
    (chr(0xF3), "a + 0xF3 (uu matra)"),
    (chr(0xE9), "a + 0xE9 (e/o matra)"),
    (chr(0xF6), "a + 0xF6 (ai matra)"),
    (chr(0x61), "a + a (ka-vattu?)"),
    (chr(0x7B), "a + 0x7B (u-matra tall)"),
]

img = Image.new('RGB', (1000, len(marks) * 60 + 20), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (m, desc) in enumerate(marks):
    y = i * 60 + 10
    test_str = 'a' + m
    draw.text((20, y), desc, fill=(80, 80, 80), font=label_font)
    draw.text((300, y), f"repr: {repr(test_str)}", fill=(120, 120, 120), font=label_font)
    try:
        draw.text((600, y), test_str, fill=(0, 0, 0), font=shree_font)
    except Exception as e:
        draw.text((600, y), str(e), fill=(255, 0, 0), font=label_font)

img.save('scratch/shreelipi_telugu/test_ka_combinations.png')
print("Rendered test_ka_combinations.png")
