from PIL import Image, ImageChops

img = Image.open('original.png').convert('RGB')
# I'll just save it to view
img.save('original_RGB.png')
