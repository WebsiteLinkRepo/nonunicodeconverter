import re
import base64
from io import BytesIO
from PIL import Image

# Read original
with open('public/logo_original.svg', 'r') as f:
    svg_data = f.read()

match = re.search(r'data:image/png;base64,([^"]+)', svg_data)
b64_str = match.group(1)
img_data = base64.b64decode(b64_str)

def recolor(bg_color, fg_color):
    img = Image.open(BytesIO(img_data)).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a > 0:
                # The original icon has a dark background (~rgb(15,10,15)) and white arrows (~255,255,255)
                # Let's use brightness to interpolate
                brightness = (r + g + b) / (3.0 * 255.0)
                # If it's bright (arrow), use fg_color. If dark (bg), use bg_color.
                # We can do a simple blend:
                new_r = int(bg_color[0] * (1 - brightness) + fg_color[0] * brightness)
                new_g = int(bg_color[1] * (1 - brightness) + fg_color[1] * brightness)
                new_b = int(bg_color[2] * (1 - brightness) + fg_color[2] * brightness)
                pixels[x, y] = (new_r, new_g, new_b, a)
    
    out_buffer = BytesIO()
    img.save(out_buffer, format="PNG")
    return base64.b64encode(out_buffer.getvalue()).decode('utf-8')

# Light mode: bg is #0b172a (11, 23, 42), fg is #e6f0fa (230, 240, 250)
light_b64 = recolor((11, 23, 42), (230, 240, 250))
with open('public/logo-light.svg', 'w') as f:
    f.write(svg_data.replace(b64_str, light_b64))

# Dark mode: bg is #f5f5f5 (245, 245, 245), fg is #08090b (8, 9, 11)
dark_b64 = recolor((245, 245, 245), (8, 9, 11))
with open('public/logo-dark.svg', 'w') as f:
    f.write(svg_data.replace(b64_str, dark_b64))

print("Generated logo-light.svg and logo-dark.svg")
