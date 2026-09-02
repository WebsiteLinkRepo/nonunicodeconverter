import re

with open('src/utils/shreeLipiTeluguConverter.ts', 'r', encoding='utf-8') as f:
    code = f.read()

has_talakattu = {
    'క': True,
    'ఖ': False,
    'గ': True,
    'ఘ': True,
    'ఙ': False,
    'చ': True,
    'ఛ': False,
    'జ': True,
    'ఝ': False,
    'ఞ': False,
    'ట': False,
    'ఠ': False,
    'డ': True,
    'ఢ': False,
    'ణ': True,
    'త': True,
    'థ': True,
    'ద': True,
    'ధ': True,
    'న': True,
    'ప': True,
    'ఫ': False,
    'బ': True,
    'భ': True,
    'మ': True,
    'య': True,
    'ర': True,
    'ల': True,
    'వ': True,
    'శ': True,
    'ష': True,
    'స': True,
    'హ': True,
    'ళ': True,
    'క్ష': True,
    'ఱ': False
}

map_code = "const HAS_TALAKATTU: Record<string, boolean> = {\n"
for k, v in has_talakattu.items():
    map_code += f"  '{k}': {'true' if v else 'false'},\n"
map_code += "};\n"

code = code.replace("const SPECIAL_COMBOS", map_code + "\n// Pre-composed Consonant + Vowel combinations for irregulars\nconst SPECIAL_COMBOS")

# Now modify the logic
old_logic = """        } else if (matraUni && MATRA_MAP[matraUni]) {
          result += MATRA_MAP[matraUni];
        } else {
          result += TALAKATTU;
        }"""

new_logic = """        } else if (matraUni && MATRA_MAP[matraUni]) {
          result += MATRA_MAP[matraUni];
        } else if (HAS_TALAKATTU[consonantUni]) {
          result += TALAKATTU;
        }"""

code = code.replace(old_logic, new_logic)

with open('src/utils/shreeLipiTeluguConverter.ts', 'w', encoding='utf-8') as f:
    f.write(code)

