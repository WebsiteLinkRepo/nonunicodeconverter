"""
Apply all fixes to neo.ts AFTER regeneration + fix_neo.py
Based on deep analysis of chart images and converter logic.
"""

with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Remove wrong द्द entry (183 = द्र, NOT द्द)
content = content.replace("  'द्द': '\\uF0B7',\n", "")

# Fix 2: Add half-Da (द्) at byte 241 = \uF0F1
# This allows द्द to compose as द्(241) + द(116) naturally
# Insert it right before the closing brace
content = content.replace("  'प्र': '\\uF09F',\n};", 
    "  'द्': '\\uF0F1',\n  'प्र': '\\uF09B\\uF0DD',\n};")

# Fix 3: Fix प्र → half-Pa(155=\uF09B) + ra-matra(221=\uF0DD)
# Already done above by replacing the line

# Fix 4: Remove the wrong second र् override
# The appended 'र्': '\uF07C' at the end conflicts with the one from map_dict
# Actually, 'र्': '\uF07C' is byte 124 which IS half-Ra from map_dict
# That's correct - keep it. The Reph is handled in anuNeoConverter.ts directly.

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixes applied!")

# Verify key entries
with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        for check in ["'द':", "'द्':", "'र्':", "'प्र':", "'द्द':", "'्':", "'्र':"]:
            if check in line:
                print(f"  {line}")
