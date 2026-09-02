# Generate exhaustive Telugu test input

vowels = [
    'అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ౠ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ', 'అం', 'అః'
]

consonants = [
    'క', 'ఖ', 'గ', 'ఘ', 'ఙ',
    'చ', 'ఛ', 'జ', 'ఝ', 'ఞ',
    'ట', 'ఠ', 'డ', 'ఢ', 'ణ',
    'త', 'థ', 'ద', 'ధ', 'న',
    'ప', 'ఫ', 'బ', 'భ', 'మ',
    'య', 'ర', 'ఱ', 'ల', 'ళ', 'వ',
    'శ', 'ష', 'స', 'హ'
]

matras = [
    '', 'ా', 'ి', 'ీ', 'ు', 'ూ', 'ృ', 'ౄ', 'ె', 'ే', 'ై', 'ొ', 'ో', 'ౌ', 'ం', 'ః'
]

lines = []
lines.append("## Independent Vowels")
lines.append(" ".join(vowels))
lines.append("")

lines.append("## Base Consonants with Virama")
lines.append(" ".join([c + '్' for c in consonants]))
lines.append("")

lines.append("## Full Guninthalu for All Consonants")
for c in consonants:
    row = [c + m for m in matras]
    lines.append(f"{c}: " + " ".join(row))
lines.append("")

lines.append("## Common Conjuncts (Vatthulu / Ottulu)")
for c1 in consonants:
    vattu_row = []
    # Test with self vattu and key common vattus
    test_vattus = [c1, 'క', 'త', 'న', 'మ', 'య', 'ర', 'ల', 'వ', 'శ', 'ష', 'స', 'హ', 'ణ']
    for c2 in test_vattus:
        vattu_row.append(f"{c1}్{c2}")
        # also with basic matras like ా, ి, ీ, ు, ూ, ే, ో, ం
        if c2 in ['క', 'త', 'మ', 'య', 'ర', 'వ', 'ష']:
            vattu_row.append(f"{c1}్{c2}ా")
            vattu_row.append(f"{c1}్{c2}ి")
            vattu_row.append(f"{c1}్{c2}ీ")
            vattu_row.append(f"{c1}్{c2}ు")
            vattu_row.append(f"{c1}్{c2}ే")
            vattu_row.append(f"{c1}్{c2}ై")
            vattu_row.append(f"{c1}్{c2}ో")
            vattu_row.append(f"{c1}్{c2}ం")
    lines.append(f"{c1} vattus: " + " ".join(vattu_row))
lines.append("")

lines.append("## Special & Complex Clusters")
complex_clusters = [
    "క్ష్మ", "క్ష్మీ", "లక్ష్మి", "లక్ష్మీ", "క్ష్ర్య", "త్ర్య", "త్ర్యం", "త్రై", "స్త్రీ", "స్వాతంత్ర్యం",
    "రాష్ట్రం", "దృష్టి", "సృష్టి", "ప్రకృతి", "శ్రద్ధ", "ప్రశ్న", "ఆంధ్రప్రదేశ్", "తెలంగాణ",
    "హైదరాబాదు", "విజయవాడ", "విశాఖపట్నం", "తిరుపతి", "సాహిత్యం", "సంస్కృతి", "విజ్ఞానం",
    "నమస్కారము", "శుభాకాంక్షలు", "కృతజ్ఞతలు", "ప్రత్యేక", "మధ్యాహ్నం", "చిహ్నం", "బ్రహ్మ", "జిహ్వ",
    "ఉత్సాహం", "ఆధ్యాత్మికం", "విశ్వవిద్యాలయం", "ప్రజాస్వామ్యం", "రాజ్యాంగం", "న్యాయస్థానం",
    "అంతర్జాతీయ", "సాంకేతిక", "పరిశోధన", "అభివృద్ధి", "పరిశ్రమలు", "పర్యావరణం", "కార్యక్రమం"
]
lines.append(" ".join(complex_clusters))
lines.append("")

lines.append("## Numbers and Punctuations")
lines.append("౦ ౧ ౨ ౩ ౪ ౫ ౬ ౭ ౮ ౯")
lines.append("0 1 2 3 4 5 6 7 8 9")
lines.append("! @ # $ % ^ & * ( ) _ + - = [ ] { } ; : ' \" , . < > / ?")
lines.append("")

lines.append("## Telugu Sample Paragraphs")
paras = """తెలుగు భాష భారతదేశంలోని ప్రాచీన, విశిష్ట ద్రావిడ భాషలలో ఒకటి. ఆంధ్రప్రదేశ్, తెలంగాణ రాష్ట్రాలలో తెలుగు అధికార భాషగా గుర్తింపు పొందింది. అంతేకాకుండా యానాం కేంద్రపాలిత ప్రాంతంలో కూడా ఇది అధికారిక భాష. ప్రపంచవ్యాప్తంగా అత్యధిక ప్రజలు మాట్లాడే భాషలలో తెలుగు ఒకటి. ఇటాలియన్ ఆఫ్ ది ఈస్ట్ అని ప్రసిద్ధి చెందిన తెలుగు భాషలో పదాలు అచ్చుతో అంతమవుతాయి (అజంత భాష).

శ్రీకృష్ణదేవరాయలు 'దేశభాషలందు తెలుగు లెస్స' అని కొనియాడారు. తెలుగు సాహిత్యం నన్నయ, తిక్కన, ఎర్రన అను కవిత్రయం రచించిన ఆంధ్ర మహాభారతంతో ప్రారంభమై నేటివరకు ఎన్నో ప్రక్రియలలో విస్తరించింది. ఆధునిక యుగంలో పత్రికలు, టీవీ మాధ్యమాలు, ఇంటర్నెట్ రంగాలలో తెలుగు వినియోగం ఎంతగానో పెరిగింది.

సాంకేతిక రంగంలో కంప్యూటర్లు, మొబైల్ ఫోన్లు వచ్చిన తర్వాత డిజిటల్ మాధ్యమంలో యూనికోడ్ ప్రామాణికంగా మారింది. అయినప్పటికీ ప్రచురణ, డిటిపి, గ్రాఫిక్ డిజైనింగ్ రంగాలలో శ్రీలిపి, అను స్క్రిప్ట్ వంటి లెగసీ నాన్-యూనికోడ్ ఫాంట్లకు విశేష ఆదరణ ఉంది. ఈ ఫాంట్ల కొరకు యూనికోడ్ నుండి నాన్-యూనికోడ్ కు సమర్థవంతమైన మార్పిడి అవసరం ఎంతైనా ఉంది."""
lines.append(paras)

content = "\n".join(lines)
with open('/home/samuelvictor/unicode2nonunicode.com/scratch/TELUGU_ALL_IN_ONE_INPUT.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated /home/samuelvictor/unicode2nonunicode.com/scratch/TELUGU_ALL_IN_ONE_INPUT.txt")
