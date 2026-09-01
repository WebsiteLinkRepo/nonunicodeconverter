import re

with open("src/utils/mappings/index.ts", "r") as f:
    text = f.read()

# Add ANU_TAMIL_UNICODE_TO_NONUNICODE import
text = text.replace("import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from './baminiTamil';", "import { BAMINI_TAMIL_UNICODE_TO_NONUNICODE } from './baminiTamil';\nimport { ANU_TAMIL_UNICODE_TO_NONUNICODE } from './anuTamil';")

# Add anutamil to FontEncoding type
text = text.replace("export type FontEncoding = 'anu7' | 'anu6' | 'krutidev' | 'bamini' | 'ism' | 'nudi' | 'shreelipi';", "export type FontEncoding = 'anu7' | 'anu6' | 'krutidev' | 'bamini' | 'anutamil' | 'ism' | 'nudi' | 'shreelipi';")

# Add to AVAILABLE_FONTS array
new_option = """  {
    id: 'anutamil',
    name: 'Anu Script (Tamil)',
    family: 'AnuScript7',
    script: 'tamil',
    description: 'Anu Script font layout for Tamil',
    fallbackFontFamily: "'AnuScript7', sans-serif"
  },"""
text = text.replace("    fallbackFontFamily: \"'Bamini', sans-serif\"\n  },", f"    fallbackFontFamily: \"'Bamini', sans-serif\"\n  }},\n{new_option}")

# Add to getMapping
mapping_code = """  } else if (encoding === 'bamini') {
    mappingList = BAMINI_TAMIL_UNICODE_TO_NONUNICODE;
    script = 'tamil';
  } else if (encoding === 'anutamil') {
    mappingList = ANU_TAMIL_UNICODE_TO_NONUNICODE;
    script = 'tamil';"""

text = text.replace("""  } else if (encoding === 'bamini') {
    mappingList = BAMINI_TAMIL_UNICODE_TO_NONUNICODE;
    script = 'tamil';""", mapping_code)

with open("src/utils/mappings/index.ts", "w") as f:
    f.write(text)

print("Patched src/utils/mappings/index.ts")
