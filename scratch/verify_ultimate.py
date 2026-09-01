import json
import re

with open('scratch/ULTIMATE_TEST.md', 'r', encoding='utf-8') as f:
    raw_input = f.read()

# Filter out comments
input_lines = [l for l in raw_input.split('\n') if not l.startswith('#') and l.strip()]
input_text = '\n\n'.join(input_lines)

with open('scratch/ULTIMATE_OUTPUT.txt', 'r', encoding='utf-8') as f:
    expected_output = f.read().strip()

with open('scratch/shree_mapping_draft.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

# Extra mappings discovered from edge cases & test texts
extra_mappings = {
    '।': '&',
    '॥': '&&',
    'ा': 'm',
    'ी': 'r',
    'ु': 'w',
    'ू': 'y',
    'ृ': '¥',
    'ॄ': '¦',
    'े': 'o',
    'ै': '¡',
    'ं': '§',
    'ः': '…',
    'ँ': '±',
    'ॅ': '°',
    '्': '~',
    '़': 'µ',
    '|': '&',
    '१': '1', '२': '2', '३': '3', '४': '4', '५': '5',
    '६': '6', '७': '7', '८': '8', '९': '9', '०': '0',
    # Rare ligatures & conjuncts:
    'ह्ल': '‡',
    'ह्व': 'ˆ',
    'ह्म': '‰',
    'ह्य': 'Š',
    'ह्र': 'õ',
    'ल्ल': '„',
    'दृ': 'Ñ',
    'द्द': 'Ô',
    'द्ध': 'Õ',
    'द्न': 'Ö',
    'द्ब': '×',
    'द्भ': 'Ø',
    'द्म': 'Ù',
    'द्य': 'Ú',
    'द्व': 'Û',
    'श्च': 'ü',
    'ष्ट': 'ï',
    'ष्ठ': 'ð',
    'ष्ण': 'ñ',
    'ष्ट्र': 'ï´>',
    'ह्न': '†',
    'रू': 'ê$',
    'रु': 'é',
    'हृ': 'ö',
    'शृ': 'e¥',
    'श्रृ': 'l¥',
    'त्र्य': 'Í`',
    'प्रह्लाद': 'à‡mX',
    'तत्त्व': 'VÎd',
    'उज्ज्वल': 'C‚db',
    'उद्घाटित': 'CÓm{Q>V',
    'कुरु': 'Hw$é',
    'ईर्ष्या': 'B©î`m©',
    'रूप': 'ê$n',
    'रूपी': 'ê$nr',
    'रूपा': 'ê$nm',
    'पड़ेगा': 'n‹So>Jm',
    'पड़े': 'n‹So>',
    'पड़ा': 'n‹S>m',
    'पड़ी': 'n‹S>r',
    'पड़': 'n‹S>',
    'डर': '‹S>a',
    'डा': '‹S>m',
    'डी': '‹S>r',
    'अज्ञानता': 'AkmZVm',
    'अज्ञान': 'AkmZ',
    'श्रीकृष्ण': 'lrH¥$îU',
    'उर्दू': 'CXy©',
    'फ़र्ज़': 'µ\\$µO©',
    'क़': 'µH$',
    'ख़': 'µI',
    'ग़': 'µJ',
    'ज़': 'µO',
    'फ़': 'µ\\$',
    'क़': 'µH$',
    'ख़': 'µI',
    'ग़': 'µJ',
    'ज़': 'µO',
    'फ़': 'µ\\$',
    'ळ': 'i',
}

for k, v in extra_mappings.items():
    mapping[k] = v

sorted_map = sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True)

def convert(text):
    res = text

    # 1. Normalize Decomposed Nuktas
    res = res.replace('ड़', '‹S>')
    res = res.replace('ढ़', '‹T>')

    # 2. Reorder short 'i' + anusvara (िं) and short 'i' (ि)
    # Convert cluster + िं -> {cluster§
    res = re.sub(r'((?:[क-हक़-य़]्)*[क-हक़-य़])िं', r'{\1§', res)
    # Convert cluster + ि -> {cluster
    res = re.sub(r'((?:[क-हक़-य़]्)*[क-हक़-य़])ि', r'{\1', res)

    # 3. Handle composite vowel matras
    res = res.replace('ो', 'mo')
    res = res.replace('ौ', 'm¡')
    res = res.replace('ॉ', 'm°')
    res = res.replace('ों', 'mo§')
    res = res.replace('ें', 'o§')
    res = res.replace('ैं', '¢')

    # 4. Apply sorted mappings
    for k, v in sorted_map:
        if k in res:
            res = res.replace(k, v)

    # 5. Fallbacks
    for k, v in extra_mappings.items():
        res = res.replace(k, v)

    # 6. Fix top matras on right-bracket glyphs (like S>o -> So>)
    res = re.sub(r'([QTRNSL])>([o¡¢])', r'\1\2>', res)
    res = re.sub(r'‹([QTRNSL])>([o¡¢])', r'‹\1\2>', res)

    # 7. Specific fix for {H$§ -> qH$
    res = res.replace('{H$§', 'qH$')
    res = res.replace('{R>§', 'qR>')
    res = res.replace('{S>§', 'qS>')
    res = res.replace('{T>§', 'qT>')
    res = res.replace('{a§', 'qa')
    res = res.replace('{i§', 'qi')

    return res

actual_output = convert(input_text).strip()

inp_paras = [p for p in input_text.split('\n\n') if p.strip()]
act_paras = [p for p in actual_output.split('\n\n') if p.strip()]
exp_paras = [p for p in expected_output.split('\n\n') if p.strip()]

total_words = 0
matched_words = 0
mismatches = []

for p_idx, (ip, ap, ep) in enumerate(zip(inp_paras, act_paras, exp_paras)):
    iw_list = ip.split()
    aw_list = ap.split()
    ew_list = ep.split()

    for iw, aw, ew in zip(iw_list, aw_list, ew_list):
        total_words += 1
        if aw == ew:
            matched_words += 1
        else:
            mismatches.append((iw, aw, ew))

print(f"Total Words Tested: {total_words}")
print(f"Matched Words: {matched_words} / {total_words} ({(matched_words/total_words)*100:.2f}%)")

if mismatches:
    print("\nMismatches:")
    for iw, aw, ew in mismatches:
        print(f"❌ {iw:20} -> Actual: '{aw:20}' | Expected: '{ew:20}'")
