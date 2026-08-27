from PIL import Image
img = Image.open("test_output.png")
crop = img.crop((0, 80, 500, 150))
crop.save("crop.png")
