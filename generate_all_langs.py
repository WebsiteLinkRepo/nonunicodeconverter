import os

langs = {
    'hindi': {
        'ind_vowels': 'अ आ इ ई उ ऊ ऋ ॠ ऌ ॡ ऍ ऎ ए ऐ ऑ ऒ ओ औ'.split(),
        'consonants': 'क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह'.split(),
        'vowel_signs': 'ा ि ी ु ू ृ ॄ ॅ ॆ े ै ॉ ॊ ो ौ ঁ ं ः'.split(),
        'virama': '्',
        'conjuncts': ['क्ष', 'त्र', 'ज्ञ', 'श्र', 'द्या', 'द्व', 'क्त', 'द्भ', 'ष्ट', 'श्च']
    },
    'tamil': {
        'ind_vowels': 'அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ'.split(),
        'consonants': 'க ங ச ஞ ட ண த ந ப ம ய ர ல வ ழ ள ற ன ஜ ஷ ஸ ஹ க்ஷ ஸ்ரீ'.split(),
        'vowel_signs': 'ா ி ீ ு ூ ெ ே ை ொ ோ ௌ ்'.split(), # ் is pulli
        'virama': '்',
        'conjuncts': []
    },
    'kannada': {
        'ind_vowels': 'ಅ ಆ ಇ ಈ ಉ ಊ ಋ ೠ ಎ ಏ ಐ ಒ ಓ ಔ'.split(),
        'consonants': 'ಕ ಖ ಗ ಘ ಙ ಚ ಛ ಜ ಝ ಞ ಟ ಠ ಡ ಢ ಣ ತ ಥ ದ ಧ ನ ಪ ಫ ಬ ಭ ಮ ಯ ರ ಱ ಲ ವ ಶ ಷ ಸ ಹ ಳ ೞ'.split(),
        'vowel_signs': 'ಾ ಿ ೀ ು ೂ ೃ ೄ ೆ ೇ ೈ ೊ ೋ ೌ ಂ ಃ'.split(),
        'virama': '್',
        'conjuncts': ['ಕ್ಷ', 'ಜ್ಞ']
    }
}

for lang, chars in langs.items():
    lines = []
    # 1. Independent Vowels
    lines.extend(chars['ind_vowels'])
    # 2. Base Consonants
    lines.extend(chars['consonants'])
    # 3. Base Consonant + Vowel Signs
    base_c = chars['consonants'][0] # e.g. 'क'
    for vs in chars['vowel_signs']:
        lines.append(base_c + vs)
    # 4. Consonant Vatthus (Half-forms)
    for c in chars['consonants']:
        lines.append(c + chars['virama'] + base_c) # e.g. क्क, ख्क
    # 5. Conjuncts
    lines.extend(chars['conjuncts'])
    
    with open(f'{lang}_anu_test.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'Generated {len(lines)} lines for {lang}')

