import re

words = {
    'धर्म': 'dha-r-m',
    'कर्म': 'ka-r-m', 
    'उद्देश्य': 'u-dde-shy',
    'प्रौद्योगिकी': 'prau-dyo-gi-ki',
}

for word, desc in words.items():
    print(f"\n=== Tracing: {word} ({desc}) ===")
    print("Unicode codepoints:", ' '.join(f'U+{ord(c):04X}' for c in word))
    
    text = word
    clusterRegex = re.compile(r'((?:[\u0915-\u0939\u0958-\u095F]\u094D)*[\u0915-\u0939\u0958-\u095F])\u093F')
    text = clusterRegex.sub('\u093F\\1', text)
    if text != word:
        print(f"After i-swap: {text}")
        print("  Codepoints:", ' '.join(f'U+{ord(c):04X}' for c in text))
    
    text2 = text
    rephRegex = re.compile(r'\u0930\u094D([\u0915-\u0939\u0958-\u095F][\u093E-\u094C\u094E-\u094F]*)')
    def reph_replace(m):
        return m.group(1) + '\u0930\u094D'
    text2 = rephRegex.sub(reph_replace, text2)
    if text2 != text:
        print(f"After reph-swap: {text2}")
        print("  Codepoints:", ' '.join(f'U+{ord(c):04X}' for c in text2))
    
    print(f"Final text for mapping: {text2}")
    print("  Chars:", ' | '.join(f'{c} (U+{ord(c):04X})' for c in text2))
