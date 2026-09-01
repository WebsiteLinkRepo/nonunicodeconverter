import json
import re

with open('scratch/shree_mapping_draft.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

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
}

for k, v in extra_mappings.items():
    if k not in mapping or mapping[k] is None:
        mapping[k] = v

sorted_map = sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True)

input_text = "आज कल का बच्चा कंप्यूटर सीखता है। कल के बड़े आदमी भी तकनीकी ज्ञान रखते हैं। यह समय की माँग है और हमें इसे स्वीकार करना चाहिए।"
expected_output = "AmO H$b H$m ~ƒm H§$ß`yQ>a grIVm h¡& H$b Ho$ ~‹So> AmX_r ^r VH$ZrH$r kmZ aIVo h¢& `h g_` H$r _m±J h¡ Am¡a h_o§ Bgo ñdrH$ma H$aZm Mm{hE&"

def convert(text):
    res = text

    # 1. Normalize Decomposed Nuktas (ड + ़ -> ड़)
    res = res.replace('ड़', 'ड़')
    res = res.replace('ढ़', 'ढ़')
    res = res.replace('क़', 'क़')
    res = res.replace('ख़', 'ख़')
    res = res.replace('ग़', 'ग़')
    res = res.replace('ज़', 'ज़')
    res = res.replace('फ़', 'फ़')

    # 2. Swap short 'i' matra (ि) to before consonant cluster
    res = re.sub(r'((?:[क-हक़-य़]्)*[क-हक़-य़])ि', r'{\1', res)

    # 3. Handle composite vowel matras
    res = res.replace('ो', 'mo')
    res = res.replace('ौ', 'm¡')
    res = res.replace('ॉ', 'm°')
    res = res.replace('ों', 'mo§')
    res = res.replace('ें', 'o§')
    res = res.replace('ैं', '¢')

    # 4. Handle nuktas for ‹S> and ‹T>
    res = res.replace('ड़', '‹S>')
    res = res.replace('ढ़', '‹T>')

    # 5. Apply sorted mappings
    for k, v in sorted_map:
        if k in res:
            res = res.replace(k, v)

    # 6. Fix top matras on right-bracket glyphs (like S>o -> So>)
    res = re.sub(r'([QTRNSL])>([o¡¢])', r'\1\2>', res)
    res = re.sub(r'‹([QTRNSL])>([o¡¢])', r'‹\1\2>', res)

    return res

actual = convert(input_text)
print("Actual  : ", actual)
print("Expected: ", expected_output)
print("100% Match?: ", actual == expected_output)
