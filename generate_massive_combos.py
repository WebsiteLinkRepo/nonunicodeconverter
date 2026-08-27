import os

langs = {
    'hindi': {
        'ind_vowels': 'अ आ इ ई उ ऊ ऋ ॠ ऌ ॡ ऍ ऎ ए ऐ ऑ ऒ ओ औ'.split(),
        'consonants': 'क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह'.split(),
        'vowel_signs': 'ा ि ी ु ू ृ ॄ ॅ ॆ े ै ॉ ॊ ो ौ ঁ ं ः'.split(),
        'virama': '्'
    },
    'tamil': {
        'ind_vowels': 'அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ'.split(),
        'consonants': 'க ங ச ஞ ட ண த ந ப ம ய ர ல வ ழ ள ற ன ஜ ஷ ஸ ஹ க்ஷ ஸ்ரீ'.split(),
        'vowel_signs': 'ா ி ீ ு ூ ெ ே ை ொ ோ ௌ ்'.split(),
        'virama': '்'
    },
    'kannada': {
        'ind_vowels': 'ಅ ಆ ಇ ಈ ಉ ಊ ಋ ೠ ಎ ಏ ಐ ಒ ಓ ಔ'.split(),
        'consonants': 'ಕ ಖ ಗ ಘ ಙ ಚ ಛ ಜ ಝ ಞ ಟ ಠ ಡ ಢ ಣ ತ ಥ ದ ಧ ನ ಪ ಫ ಬ ಭ ಮ ಯ ರ ಱ ಲ ವ ಶ ಷ ಸ ಹ ಳ ೞ'.split(),
        'vowel_signs': 'ಾ ಿ ೀ ು ೂ ೃ ೄ ೆ ೇ ೈ ೊ ೋ ೌ ಂ ಃ'.split(),
        'virama': '್'
    }
}

for lang, chars in langs.items():
    lines = []
    
    # 1. Independent Vowels
    lines.extend(chars['ind_vowels'])
    
    # 2. Base Consonants
    lines.extend(chars['consonants'])
    
    # 3. Base Consonant + Vowel Signs
    for c in chars['consonants']:
        for vs in chars['vowel_signs']:
            lines.append(c + vs)
            
    # 4. Consonant + Vatthu (Half-forms)
    for c1 in chars['consonants']:
        for c2 in chars['consonants']:
            lines.append(c1 + chars['virama'] + c2)
            
    # 5. Consonant + Vatthu + Vowel Sign (The ultimate complex shape!)
    for c1 in chars['consonants']:
        for c2 in chars['consonants']:
            for vs in chars['vowel_signs']:
                lines.append(c1 + chars['virama'] + c2 + vs)
                
    with open(f'{lang}_all_combinations.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'Generated {len(lines)} lines for {lang}')

