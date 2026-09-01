import json
import re

input_text = """१. श्रवणकुमार की पितृभक्ति अद्वितीय थी। उन्होंने अपने वृद्ध माता-पिता को काँवर में बिठाकर तीर्थयात्रा कराई। मार्ग में दशरथ के बाण से उनकी मृत्यु के पश्चात्, राम का जन्म हुआ।
२. राष्ट्रनिर्माण में स्त्रियों का योगदान अत्यंत महत्त्वपूर्ण है। प्रबुद्ध महिलाएँ विज्ञान, कृत्रिम बुद्धिमत्ता, वाणिज्य और रक्षा-क्षेत्र में भी अपने कर्तव्यों का निर्वहन कर रही हैं।
३. महाराष्ट्र के सुदूर गाँवों में वर्षा ऋतु में मिट्टी के घर ढह जाते हैं। कृषकों की स्थिति अत्यंत दयनीय हो जाती है, परंतु वे मिट्टी से जुड़कर पुनः खड़ी फसल उगाने में प्रवृत्त रहते हैं।
४. क्षत्रिय धर्म का निर्वाह करते हुए, कृष्ण ने कुरुक्षेत्र में अर्जुन को ब्रह्मज्ञान का उपदेश दिया। "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन" - यह श्लोक अद्वैत वेदांत का सार है।
५. त्र्यंबकेश्वर के दर्शनार्थी श्रृद्धालु श्रावण मास में भस्म और रुद्राक्ष धारण करते हैं। ओमकार की ध्वनि से संपूर्ण वायुमंडल गूंज उठता है एवं शांति और शक्ति का संचार होता है।"""

expected_output = """1. ldUHw$_ma H$r {nV¥^{º$ A{ÛVr` Wr& CÝhmo§Zo AnZo d¥Õ _mVm-{nVm H$mo H$m±da _o§ {~R>mH$a VrW©`mÌm H$amB©& _mJ© _o§ XeaW Ho$ ~mU go CZH$r _¥Ë`w Ho$ nümV~, am_ H$m OÝ_ hwAm&
2. amï´>{Z_m©U _o§ pñÌ`mo§ H$m `moJXmZ AË`§V _hÎdnyU© h¡& à~wÕ _{hbmE± {dkmZ, H¥${Ì_ ~w{Õ_Îmm, dm{UÁ` Am¡a ajm-joÌ _o§ ^r AnZo H$V©ì`mo§ H$m {Zd©hZ H$a ahr h¢&
3. _hmamï´> Ho$ gwXya Jm±dmo§ _o§ dfm© F$Vw _o§ {_Å>r Ho$ Ka T>h OmVo h¢& H¥$fH$mo§ H$r pñW{V AË`§V X`Zr` hmo OmVr h¡, na§Vw do {_Å>r go Ow‹S>H$a nwZ… I‹S>r \$gb CJmZo _o§ àd¥Îm ahVo h¢&
4. j{Ì` Y_© H$m {Zdm©h H$aVo hwE, H¥$îU Zo Hw$éjoÌ _o§ AOw©Z H$mo ~«÷kmZ H$m CnXoe {X`m& "H$_©Ê`odm{YH$mañVo _m \$bofw H$XmMZ" - `h íbmoH$ AÛ¡V doXm§V H$m gma h¡&
5. Í`§~Ho$œa Ho$ Xe©ZmWu l¥Õmbw lmdU _mg _o§ ^ñ_ Am¡a éÐmj YmaU H$aVo h¢& Amo_H$ma H$r Üd{Z go g§nyU© dm`w_§S>b Jy§O CR>Vm h¡ Ed§ em§{V Am¡a e{º$ H$m g§Mma hmoVm h¡&"""

with open('scratch/shree_mapping_draft.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)

# Essential standalone characters, matras, punctuations
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
}

for k, v in extra_mappings.items():
    if k not in mapping or mapping[k] is None:
        mapping[k] = v

sorted_map = sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True)

def convert(text):
    res = text

    # 1. Normalize Numbers
    dev_nums = {'१':'1', '२':'2', '३':'3', '४':'4', '५':'5', '६':'6', '७':'7', '८':'8', '९':'9', '०':'0'}
    for d, a in dev_nums.items():
        res = res.replace(d, a)

    # 2. Normalize Decomposed Nuktas
    res = res.replace('ड़', 'ड़')
    res = res.replace('ढ़', 'ढ़')
    res = res.replace('क़', 'क़')
    res = res.replace('ख़', 'ख़')
    res = res.replace('ग़', 'ग़')
    res = res.replace('ज़', 'ज़')
    res = res.replace('फ़', 'फ़')

    # 3. Swap short 'i' matra (ि) to before consonant cluster
    # cluster regex: any sequence of (consonant+virama)* + consonant
    res = re.sub(r'((?:[क-हक़-य़]्)*[क-हक़-य़])ि', r'{\1', res)

    # 4. Handle composite vowel matras
    res = res.replace('ो', 'mo')
    res = res.replace('ौ', 'm¡')
    res = res.replace('ॉ', 'm°')
    res = res.replace('ों', 'mo§')
    res = res.replace('ें', 'o§')
    res = res.replace('ैं', '¢')

    # 5. Handle nuktas for ‹S> and ‹T>
    res = res.replace('ड़', '‹S>')
    res = res.replace('ढ़', '‹T>')

    # 6. Apply sorted mappings
    for k, v in sorted_map:
        if k in res:
            res = res.replace(k, v)

    # 7. Fallbacks
    for k, v in extra_mappings.items():
        res = res.replace(k, v)

    # 8. Fix top matras on right-bracket glyphs (like S>o -> So>)
    res = re.sub(r'([QTRNSL])>([o¡¢])', r'\1\2>', res)
    res = re.sub(r'‹([QTRNSL])>([o¡¢])', r'‹\1\2>', res)

    return res

actual_output = convert(input_text)
print("=== COMPARISON BY LINE ===")
act_lines = actual_output.strip().split('\n')
exp_lines = expected_output.strip().split('\n')
inp_lines = input_text.strip().split('\n')

for line_idx, (inp_l, act_l, exp_l) in enumerate(zip(inp_lines, act_lines, exp_lines)):
    print(f"\n--- Line {line_idx + 1} ---")
    act_words = act_l.split()
    exp_words = exp_l.split()
    inp_words = inp_l.split()
    for w_idx, (iw, aw, ew) in enumerate(zip(inp_words, act_words, exp_words)):
        if aw == ew:
            pass # print(f"✅ {iw} -> {aw}")
        else:
            print(f"❌ {iw:20} -> Actual: '{aw:20}' | Expected: '{ew:20}'")
