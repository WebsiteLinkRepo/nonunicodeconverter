import re
import base64
from io import BytesIO

# Read the SVG
with open('public/logo_original.svg', 'r') as f:
    svg_data = f.read()

# Extract base64
match = re.search(r'data:image/png;base64,([^"]+)', svg_data)
if not match:
    print("No base64 found")
    exit(1)

b64_str = match.group(1)
img_data = base64.b64decode(b64_str)

with open('public/original.png', 'wb') as f:
    f.write(img_data)
