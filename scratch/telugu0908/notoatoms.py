#!/usr/bin/env python3
"""
Decode Noto Serif Telugu glyph names into (Telugu string, role).

Noto names every atom the script needs, which is what makes it usable as a *labelled*
reference set rather than just another typeface to eyeball:

    katelu               full letter                క
    kasubscripttelu      subscript (vattu)          ్క
    kivoweltelu          precomposed C + ి          కి
    kahalanttelu         C + virama                 క్
    karasubscripttelu    C + ra-subscript as one    క్ర
    ailengthmarktelu     the mark that turns ె into ై
    tailengthmarkwide…   ... width-matched to త

Names are parsed standalone-table-first, then <consonant><role>, longest consonant stem
first, because `sa`/`ssa`, `ta`/`tta`, `la`/`lla`/`llla`, `ra`/`rra`/`rrra` and `ka`/`kassa`
are all prefixes of each other. Anything unrecognised comes back as role 'other' so it
still participates in scoring without being trusted as a label.
"""
CONS = {
    'kassa': 'క్ష',
    'kha': 'ఖ', 'gha': 'ఘ', 'nga': 'ఙ', 'cha': 'ఛ', 'jha': 'ఝ', 'nya': 'ఞ',
    'ttha': 'ఠ', 'ddha': 'ఢ', 'tta': 'ట', 'dda': 'డ', 'nna': 'ణ',
    'tha': 'థ', 'dha': 'ధ', 'pha': 'ఫ', 'bha': 'భ', 'sha': 'శ', 'ssa': 'ష',
    'llla': 'ఴ', 'lla': 'ళ', 'rrra': 'ౚ', 'rra': 'ఱ',
    'ka': 'క', 'ga': 'గ', 'ca': 'చ', 'ja': 'జ', 'ta': 'త', 'da': 'ద', 'na': 'న',
    'pa': 'ప', 'ba': 'బ', 'ma': 'మ', 'ya': 'య', 'ra': 'ర', 'la': 'ల', 'va': 'వ',
    'sa': 'స', 'ha': 'హ', 'tsa': 'ౘ', 'dza': 'ౙ',
}
STEMS = sorted(CONS, key=len, reverse=True)

MATRA_ROLE = {
    'aavowel': 'ా', 'ivowel': 'ి', 'iivowel': 'ీ', 'uvowel': 'ు', 'uuvowel': 'ూ',
    'evowel': 'ె', 'eevowel': 'ే', 'aivowel': 'ై', 'ovowel': 'ొ', 'oovowel': 'ో',
    'auvowel': 'ౌ',
}
SUBSCRIPT_ROLES = {'subscript', 'subscriptlow', 'subscriptnarrow', 'subscriptwide'}

STANDALONE = {
    'a': ('అ', 'vowel'), 'aa': ('ఆ', 'vowel'), 'i': ('ఇ', 'vowel'), 'ii': ('ఈ', 'vowel'),
    'u': ('ఉ', 'vowel'), 'uu': ('ఊ', 'vowel'), 'e': ('ఎ', 'vowel'), 'ee': ('ఏ', 'vowel'),
    'ai': ('ఐ', 'vowel'), 'o': ('ఒ', 'vowel'), 'oo': ('ఓ', 'vowel'), 'au': ('ఔ', 'vowel'),
    'rvocalic': ('ఋ', 'vowel'), 'rrvocalic': ('ౠ', 'vowel'),
    'lvocalic': ('ఌ', 'vowel'), 'llvocalic': ('ౡ', 'vowel'),

    'aavowelsign': ('ా', 'matra'), 'ivowelsign': ('ి', 'matra'),
    'iivowelsign': ('ీ', 'matra'), 'uvowelsign': ('ు', 'matra'),
    'uuvowelsign': ('ూ', 'matra'), 'evowelsign': ('ె', 'matra'),
    'eevowelsign': ('ే', 'matra'), 'aivowelsign': ('ై', 'matra'),
    'ovowelsign': ('ొ', 'matra'), 'oovowelsign': ('ో', 'matra'),
    'auvowelsign': ('ౌ', 'matra'), 'auvowelsign6': ('ౌ', 'matra'),
    'rvocalicvowelsign': ('ృ', 'matra'), 'rrvocalicvowelsign': ('ౄ', 'matra'),
    'lvocalicvowelsign': ('ౢ', 'matra'), 'llvocalicvowelsign': ('ౣ', 'matra'),

    'anusvara': ('ం', 'mark'), 'visarga': ('ః', 'mark'), 'candrabindu': ('ఁ', 'mark'),
    'virama': ('్', 'mark'), 'avagraha': ('ఽ', 'mark'), 'nukta': ('', 'mark'),
    'reph': ('ర్', 'mark'), 'nakaarapollu': ('న్', 'mark'),
    'lengthmark': ('', 'lengthmark'), 'ailengthmark': ('', 'ailengthmark'),
    'danda': ('।', 'punct'), 'dbldanda': ('॥', 'punct'),
}
for i, w in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                       'eight', 'nine']):
    STANDALONE[w] = (chr(0x0C66 + i), 'digit')


def decode(gname):
    """Noto glyph name -> (text, role, variant). role is one of:
    vowel matra mark digit punct lengthmark ailengthmark
    full subscript halant precomposed rasubscript postscript other

    Noto elides the consonant's trailing `a` before a vowel-initial role, so `ka` + `ivowel`
    is spelled `kivowel` and `ta` + `ailengthmark` is spelled `tailengthmark`. Which stem
    form to use is therefore decided by the role's first letter, not guessed - that keeps
    `saivowel` (స + ై) and `sivowel` (స + ి) distinct."""
    base = gname.split('.')[0]
    variant = gname.split('.')[1] if '.' in gname else ''
    if not base.endswith('telu'):
        return None
    stem = base[:-4]
    if stem in STANDALONE:
        text, role = STANDALONE[stem]
        return text, role, variant

    for c in STEMS:
        ch = CONS[c]
        # consonant-initial roles keep the stem's trailing 'a'
        if stem.startswith(c):
            rest = stem[len(c):]
            if rest == '':
                return ch, 'full', variant
            if rest in SUBSCRIPT_ROLES:
                return '్' + ch, 'subscript', variant or rest[9:]
            if rest == 'halant':
                return ch + '్', 'halant', variant
            if rest in ('rasubscript', 'rasubscriptlig'):
                return ch + '్ర', 'rasubscript', variant
            if rest == 'postscript':
                return ch, 'postscript', variant
        # vowel-initial roles absorb it
        if c.endswith('a') and stem.startswith(c[:-1]):
            rest = stem[len(c) - 1:]
            if rest in MATRA_ROLE:
                return ch + MATRA_ROLE[rest], 'precomposed', variant
            for tail in ('ailengthmark', 'ilengthmark'):
                if rest == tail or rest.startswith(tail):
                    role = 'ailengthmark' if tail == 'ailengthmark' else 'lengthmark'
                    suffix = rest[len(tail):]
                    return '', role, c + ('/' + suffix if suffix else '')
    return stem, 'other', variant
