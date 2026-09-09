import re
import base64
from io import BytesIO
from PIL import Image

with open('public/logo-light.svg', 'r') as f:
    svg_data = f.read()

match = re.search(r'data:image/png;base64,([^"]+)', svg_data)
img_data = base64.b64decode(match.group(1))

img = Image.open(BytesIO(img_data)).convert("RGBA")
pixels = img.load()

# Let's count the frequency of colors to see what's really in there
from collections import Counter
counts = Counter()
for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        if a > 0:
            counts[(r,g,b)] += 1

print("Top 10 colors in logo-light:")
for color, count in counts.most_common(10):
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x} ({color}) : {count}")
