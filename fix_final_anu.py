with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix ट्ट to 99 (\uF063)
# Currently it's 'ट्ट': '\uF0F2'
content = content.replace("'ट्ट': '\\uF0F2'", "'ट्ट': '\\uF063'")

# 2. Fix Reph
# We don't want \uF0DC. We want \uF07C (124).
with open('src/utils/anuNeoConverter.ts', 'r', encoding='utf-8') as f:
    converter = f.read()
converter = converter.replace("'$1\\uF0DC'", "'$1\\uF07C'")
with open('src/utils/anuNeoConverter.ts', 'w', encoding='utf-8') as f:
    f.write(converter)

# 3. Wait, is 'प्रौद्योगिकी' working now? 
# The user said they typed it without "प्रौद्योगिकी" because it's hard to type.
# But our current 'प्र' is \uF09B\uF0DD (half-Pa 155 + ra-matra 221). Let's keep it.

# Let's write the updated map back
with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)

