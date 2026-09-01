import re

# Correct precomposed half-consonant mappings
new_mappings = {
    "क्": "Š", "ख्": "»", "ग्": "½", "घ्": "¿", "ङ्": "L²>",
    "च्": "À", "छ्": "N²>", "ज्": "Á", "झ्": "Â", "ञ्": "Ã",
    "ट्": "Q²>", "ठ्": "R²>", "ड्": "S²>", "ढ्": "T²>", "ण्": "Ê",
    "त्": "Ë", "थ्": "Ï", "द्": "X²", "ध्": "Ü", "न्": "Ý",
    "प्": "ß", "फ्": "â", "ब्": "ã", "भ्": "ä", "म्": "å",
    "य्": "æ", "ल्": "ë", "व्": "ì", "श्": "í",
    "ष्": "î", "स्": "ñ", "ह्": "ô", "ळ्": "ù", "क्ष्": "ú",
    "त्र्": "Í", "ज्ञ्": "k²", "श्र्": "l²", "्": "²",
    "क़्": "µH$²", "ख़्": "˜²", "ग़्": "µJ²",
    "ज़्": "µO²", "ड़्": "‹S²>", "ढ़्": "‹T²>",
    "फ़्": "µ\\$²"
}

with open('src/utils/mappings/shreeLipi.ts', 'r', encoding='utf-8') as f:
    text = f.read()

for from_k, to_v in new_mappings.items():
    # Match the mapping entry carefully
    pattern = rf'{{ from: "{from_k}", to: ".*?" }}'
    replacement = f'{{ from: "{from_k}", to: "{to_v}" }}'
    text = re.sub(pattern, replacement, text)

with open('src/utils/mappings/shreeLipi.ts', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated mappings')
