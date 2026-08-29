with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

if "  'ट्ट':" not in content:
    content = content.replace("  'त्त': '\\uF0F0',\\n", "  'त्त': '\\uF0F0',\\n  'ट्ट': '\\uF063',\\n")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
