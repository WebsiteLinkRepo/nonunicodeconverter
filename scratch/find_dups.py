from PIL import Image, ImageChops

def img_diff(img1_path, img2_path):
    img1 = Image.open(img1_path).convert('L')
    img2 = Image.open(img2_path).convert('L')
    if img1.size != img2.size:
        return False
    diff = ImageChops.difference(img1, img2)
    return diff.getbbox() is None

print("Checking duplicates for 0x60 (ya) and 0x67 (sa) in all renderings...")
# Actually, I can just use FontTools to get glyph names and check if the glyphs are identical!
