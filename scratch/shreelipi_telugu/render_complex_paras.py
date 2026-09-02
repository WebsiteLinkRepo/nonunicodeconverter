import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
ref_font_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 22)
noto_font = ImageFont.truetype(ref_font_path, 18)
label_font = ImageFont.load_default()

with open('scratch/TELUGU_COMPLEX_PARAS_INPUT.txt', 'r', encoding='utf-8') as f:
    u_lines = [line.strip() for line in f if line.strip()]

with open('scratch/TELUGU_COMPLEX_PARAS_OUTPUT.txt', 'r', encoding='utf-8') as f:
    s_lines = [line.strip() for line in f if line.strip()]

img = Image.new('RGB', (1400, len(u_lines) * 200 + 40), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

for i, (u_line, s_line) in enumerate(zip(u_lines, s_lines)):
    y = i * 200 + 20
    draw.text((20, y), f"Paragraph {i+1} [Unicode Reference]:", fill=(100, 100, 100), font=label_font)

    # Word wrap roughly or draw
    # Let's draw first 100 chars
    draw.text((20, y + 25), u_line[:120], fill=(0, 0, 150), font=noto_font)
    if len(u_line) > 120:
        draw.text((20, y + 55), u_line[120:240], fill=(0, 0, 150), font=noto_font)

    draw.text((20, y + 95), f"Paragraph {i+1} [Shree-Tel Converted Rendering]:", fill=(100, 100, 100), font=label_font)

    # We use a special mapping for rendering to handle the font specific encoding
    # This assumes s_line contains the already converted Shree-Lipi ANSI codes
    # We need to manually convert the string to the correct glyphs if necessary

    rendered_text = s_line
    # For Shree-Lipi fonts, chr(code) in PIL often doesn't work if
    # the font has custom mapping. We need to check if
    # we need to transform the string to lookups or if
    # standard string drawing works with fontTools mapping...
    # Actually, the roster script worked, so this should work if
    # the encoding in s_line matches the font layout.

    draw.text((20, y + 120), rendered_text[:120], fill=(0, 0, 0), font=shree_font)
    if len(rendered_text) > 120:
        draw.text((20, y + 150), rendered_text[120:240], fill=(0, 0, 0), font=shree_font)

img.save('scratch/shreelipi_telugu/complex_paras_render.png')
print("Rendered complex_paras_render.png")
