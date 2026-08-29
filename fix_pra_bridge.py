with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Change प्र to half-Pa (155) + ra-stroke (221) + bridge (254)
content = content.replace("'प्र': '\\uF09F'", "'प्र': '\\uF09B\\uF0DD\\uF0FE'")

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
