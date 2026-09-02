import json

# Consonants
consonants = [
    ('க', 'க்'), ('ங', 'ங்'), ('ச', 'ச்'), ('ஞ', 'ஞ்'), ('ட', 'ட்'), ('ண', 'ண்'),
    ('த', 'த்'), ('ந', 'ந்'), ('ப', 'ப்'), ('ம', 'ம்'), ('ய', 'ய்'), ('ர', 'ர்'),
    ('ல', 'ல்'), ('வ', 'வ்'), ('ழ', 'ழ்'), ('ள', 'ள்'), ('ற', 'ற்'), ('ன', 'ன்'),
    ('ஜ', 'ஜ்'), ('ஷ', 'ஷ்'), ('ஸ', 'ஸ்'), ('ஹ', 'ஹ்'), ('க்ஷ', 'க்ஷ்')
]

# Vowels (independent and combining)
vowels = [
    ('', 'அ'), ('ா', 'ஆ'), ('ி', 'இ'), ('ீ', 'ஈ'), ('ு', 'உ'), ('ூ', 'ஊ'),
    ('ெ', 'எ'), ('ே', 'ஏ'), ('ை', 'ஐ'), ('ொ', 'ஒ'), ('ோ', 'ஓ'), ('ௌ', 'ஔ')
]

# Load our mapping
with open('scratch/shree_tamil_mapping.json') as f:
    mappings = json.load(f)

mapping_dict = {m['from']: m['to'] for m in mappings}

missing = []
present = []

for base, pulli in consonants:
    # Check pulli form
    if pulli in mapping_dict:
        present.append((pulli, mapping_dict[pulli]))
    else:
        missing.append(pulli)
        
    for v_sign, v_name in vowels:
        comb = base + v_sign
        if comb in mapping_dict:
            present.append((comb, mapping_dict[comb]))
        else:
            missing.append(comb)

# Check independent vowels
ind_vowels = ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ', 'ஃ', 'ஸ்ரீ']
for iv in ind_vowels:
    if iv in mapping_dict:
        present.append((iv, mapping_dict[iv]))
    else:
        missing.append(iv)

print(f"Total standard combinations checked: {len(present) + len(missing)}")
print(f"Present in mapping: {len(present)}")
print(f"Missing from mapping: {len(missing)}")

if missing:
    print("\nMissing items:")
    for m in missing:
        print(f"  {m}")
else:
    print("\nALL 100% of standard Tamil combinations + Grantha are accounted for in our mapping!")
