import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 32)
label_font = ImageFont.load_default()

# We need to find the subscript (vattu) for every base consonant.
# We will draw a matrix: For each chr(i), we draw 'a' + chr(i) (Ka + ...)
# We only care about characters that render as a subscript UNDER the 'a'
chars = [chr(i) for i in range(32, 256)] + [chr(338), chr(339), chr(352), chr(353), chr(376), chr(402), chr(710), chr(732), chr(8211), chr(8212), chr(8216), chr(8217), chr(8218), chr(8220), chr(8221), chr(8222), chr(8224), chr(8225), chr(8226), chr(8230), chr(8240), chr(8249), chr(8250), chr(8482)]

cols = 10
rows = (len(chars) + cols - 1) // cols
cell_w, cell_h = 100, 80

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, ch in enumerate(chars):
    code = ord(ch)
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(220, 220, 220))
    draw.text((x + 4, y + 4), f"{code}", fill=(100, 100, 100), font=label_font)

    # Render 'a' (ka) + ch
    try:
        draw.text((x + 20, y + 20), 'a' + ch, fill=(0, 0, 180), font=shree_font)
    except:
        pass

img.save('scratch/all_vattulu.png')
print("Saved scratch/all_vattulu.png")
