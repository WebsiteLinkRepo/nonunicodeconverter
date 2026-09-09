import re
import base64
from io import BytesIO
from PIL import Image

# Read the SVG
with open('public/logo.svg', 'r') as f:
    svg_data = f.read()

# Extract base64
match = re.search(r'data:image/png;base64,([^"]+)', svg_data)
if not match:
    print("No base64 found")
    exit(1)

b64_str = match.group(1)
img_data = base64.b64decode(b64_str)

# Open image
img = Image.open(BytesIO(img_data)).convert("RGBA")
pixels = img.load()

# Target color: #0b172a (11, 23, 42)
target_r, target_g, target_b = 11, 23, 42

# Recolor all pixels, preserving alpha
width, height = img.size
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 0:
            # Simple tinting - assuming the original is mostly solid color
            # Just set it to the target color, keeping original alpha
            pixels[x, y] = (target_r, target_g, target_b, a)

# Save back to base64
out_buffer = BytesIO()
img.save(out_buffer, format="PNG")
new_b64 = base64.b64encode(out_buffer.getvalue()).decode('utf-8')

# Replace in SVG
new_svg_data = svg_data.replace(b64_str, new_b64)
with open('public/logo.svg', 'w') as f:
    f.write(new_svg_data)

print("Logo recolored successfully.")
