with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Change ई from 128 to 124
content = content.replace("get_char(70)}{get_char(128)}", "get_char(70)}{get_char(124)}")
# Change Reph from 128 to 124
content = content.replace("'र्': 128", "'र्': 124")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
