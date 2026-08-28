with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'ञ्': 95, 'ञ': 96", "'ञ्': 96, 'ञ': 97")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
