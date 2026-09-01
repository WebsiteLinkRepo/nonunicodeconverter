import subprocess
import json
from PIL import Image, ImageDraw, ImageFont

# 1. Words to test
test_words = [
    "पश्चात्",
    "भस्म",
    "विद्वत्ता",
    "महामृत्युंजय",
    "युद्ध",
    "युग",
    "हमारे",
    "कुरुक्षेत्र",
    "त्र्यंबकेश्वर",
    "श्रद्धालु",
    "स्वास्थ्य",
    "अद्वितीय",
    "ब्रह्मज्ञान",
    "उद्घाटित",
    "कर्मण्येवाधिकारस्ते"
]

# 2. Convert using our TS engine
js_script = f"""
import {{ unicodeToShreeLipi }} from '../src/utils/shreeLipiConverter';
const words = {json.dumps(test_words)};
const converted = words.map(w => ({{ unicode: w, legacy: unicodeToShreeLipi(w) }}));
console.log(JSON.stringify(converted));
"""

with open('scratch/temp_runner.ts', 'w') as f:
    f.write(js_script)

res = subprocess.run(['npx', 'tsx', 'scratch/temp_runner.ts'], capture_output=True, text=True, check=True)
converted_data = json.loads(res.stdout)

# 3. Render with PIL
font = ImageFont.truetype('/home/samuelvictor/Downloads/Shreelipi_4642.TTF', 32)
label_font = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSans.ttf', 18)

img = Image.new('RGB', (1100, 680), 'white')
draw = ImageDraw.Draw(img)

# Title
draw.text((30, 20), "Shree-Dev7 Production Engine Visual Verification", fill=(20, 20, 20), font=label_font)

y = 70
for i, item in enumerate(converted_data):
    uni = item['unicode']
    leg = item['legacy']
    col = 30 if i < 8 else 560
    row_y = y + (i % 8) * 72
    
    # Render encoded legacy string
    draw.text((col, row_y + 6), f"{i+1}. {uni}:", fill=(80, 80, 80), font=label_font)
    draw.text((col + 240, row_y), leg, fill=(0, 20, 140), font=font)

img.save('scratch/final_verification_card.png')
print("Saved scratch/final_verification_card.png")
