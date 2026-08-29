# Reading neo.ts and fixing ALL issues based on chart analysis

with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Issue 1: Reph (flying Ra)
# Currently line 55: 'र्': '\uF07C' (124 = half-Ra, WRONG for Reph)  
# And line 155: 'र्': '\uF07E' (126, also WRONG)
# The Reph glyph is at position 220 in the font chart = \uF0DC
# BUT we need half-Ra (124) for conjuncts like र् + म = र्म
# The reph handler in anuNeoConverter.ts already moves reph AFTER consonant
# So after reph swap, the text has: consonant + matras + र + ्
# The mapper will match 'र्' (2 chars) and should map to Reph (220)
# But this conflicts with half-Ra which is also 'र्'!
#
# SOLUTION: Remove the 'र्' entry from neoMap entirely.
# Instead, handle Reph in the converter by replacing the swapped र् 
# with a unique placeholder, then map that placeholder to byte 220.

# Issue 2: द्द
# Currently mapped to \uF0B7 (183) but 183 = द्र in the font!
# From the charts, I don't see a dedicated द्द glyph.
# It should be composed as द् (half-da) + द (da)
# द् is not in the map... wait, let me check.
# In the map_dict: there's no 'द्' entry! Only 'द': 116
# So द्द should work as: द + ् + द = half-form automatically
# But the neoMap has standalone 'द्द' → \uF0B7 which is WRONG (183 = द्र)
# SOLUTION: Remove the 'द्द' entry entirely, let it compose naturally

# Issue 3: प्र  
# Currently: 'प्र': '\uF09B\uF0E2' (155 + 226)
# But 155 = प् (half-Pa) and 226 = ̧ (some accent mark, NOT the र-line)
# From charts: '्र' already maps to \uF0DD (221) which is the ra-matra stroke
# So प्र should be: प् (155) + ्र (221)
# SOLUTION: Change प्र mapping to \uF09B\uF0DD

print("Fixing neo.ts...")

# Fix 1: Remove the duplicate/wrong 'र्' at line 155 (the appended one)
# and keep line 55's 'र्' → \uF07C (124) for half-Ra ONLY
# Then add reph handling in the converter instead

# Fix 2: Remove 'द्द' entry (let it compose as द् + द)  
content = content.replace("  'द्द': '\\uF0B7',\n", "")

# Fix 3: Fix प्र to use ्र (221 = \uF0DD) instead of 226 (\uF0E2)
content = content.replace("  'प्र': '\\uF09B\\uF0E2',\n", "  'प्र': '\\uF09B\\uF0DD',\n")

# Fix 4: Remove the WRONG second 'र्' entry (line 155) that overrides half-Ra
content = content.replace("  'र्': '\\uF07E',\n", "")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done fixing neo.ts!")
