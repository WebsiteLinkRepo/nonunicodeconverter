with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'ँ': '{get_char(125)}{get_char(88)}',", "")
content = content.replace("'ॅ': 125,", "")

# Add them to the bottom string appending
new_str = """
content += f"  'ॅ': '{get_char(125)}',\\n"
content += f"  'ँ': '{get_char(125)}{get_char(88)}',\\n"
content += "};\\n"
"""
content = content.replace("content += \"};\\n\"", new_str)

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
