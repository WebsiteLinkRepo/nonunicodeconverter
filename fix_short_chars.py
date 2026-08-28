with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Add short chars logic
short_chars_code = """
# Characters with short top lines need the 254 bridge before the A-matra!
short_chars = {'क': 78, 'फ': 162}
for char, code in short_chars.items():
    content += f"  '{char}ा': '{get_char(code)}{get_char(254)}{get_char(231)}',\\n"
    content += f"  '{char}ो': '{get_char(code)}{get_char(254)}{get_char(231)}{get_char(122)}',\\n"
    content += f"  '{char}ौ': '{get_char(code)}{get_char(254)}{get_char(231)}{get_char(123)}',\\n"
    content += f"  '{char}ॉ': '{get_char(code)}{get_char(254)}{get_char(231)}{get_char(125)}',\\n"
    
    # Also need bridge for right-side matras like 'ी' (121)
    # Wait, does 'की' need the bridge? Yes, I'll add 'की' manually.
    content += f"  '{char}ी': '{get_char(code)}{get_char(254)}{get_char(121)}',\\n"

"""
content = content.replace("content += \"};\\n\"", short_chars_code + "content += \"};\\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
