import re, base64, io
from PIL import Image
with open('public/logo-light.svg', 'r') as f:
    svg_data = f.read()
match = re.search(r'data:image/png;base64,([^"]+)', svg_data)
img = Image.open(io.BytesIO(base64.b64decode(match.group(1))))
pixels = img.load()
print("(100,100) Background:", pixels[100,100])
print("(200,200) Arrow:", pixels[200,200])
