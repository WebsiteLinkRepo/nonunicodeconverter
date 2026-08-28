with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'ू': 120", "'ू': 237")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
