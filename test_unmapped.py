import json
import re

text = "अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह क्ष त्र ज्ञ श्र क का कि की कु कू कृ के कै को कौ कं कः भ भा भि भी भु भू भृ भे भै भो भौ भं भः ष षा षि षी षु षू षृ षे षै षो षौ षं षः ० १ २ ३ ४ ५ ६ ७ ८ ९ प्र क्र ग्र ब्र ट्र ड्र द्ध द्य द्व च्च त्त डॉक्टर आँख नमस्ते! हिंदी बहुत ही सुंदर और प्राचीन भाषा है। भारत एक महान देश है, जहाँ अनेक भाषाएँ बोली जाती हैं। विज्ञान और प्रौद्योगिकी ने हमारे जीवन को बदल दिया है। ज्ञान ही शक्ति है; इसे हमेशा बढ़ाते रहना चाहिए!"

# Read the mapping keys from generate_neo_final3.py
with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

keys = []
for line in lines:
    if "': '" in line:
        key = line.split("': '")[0].split("'")[-1]
        keys.append(key)

# Sort by length
keys.sort(key=len, reverse=True)

processed = text
for key in keys:
    processed = processed.replace(key, '')

# What is left?
leftover = re.sub(r'[ \!\,।\;]', '', processed)
print("Unmapped characters:", set(leftover))
for char in set(leftover):
    print(f"Char: {char}, Unicode: {hex(ord(char))}")
