with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'क्र': 139, 'प्र': 159,", "")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
