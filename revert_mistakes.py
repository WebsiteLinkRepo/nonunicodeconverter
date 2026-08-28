with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Restore 254 bridge to की and फी
content = content.replace("  'की': '\uF04E\uF079',\n", "  'की': '\uF04E\uF0FE\uF079',\n")
content = content.replace("  'फी': '\uF0A2\uF079',\n", "  'फी': '\uF0A2\uF0FE\uF079',\n")

# Revert कू and फू to 238 (standard OO matra)
content = content.replace("  'कू': '\uF04E\uF0EF',\n", f"  'कू': '\uF04E{chr(0xF000 + 238)}',\n")
content = content.replace("  'फू': '\uF0A2\uF0EF',\n", f"  'फू': '\uF0A2{chr(0xF000 + 238)}',\n")

# Wait, what if की and फी are not in the .ts literal format?
# In generate_neo_final3.py, they are generated in a loop!
# Ah! I had modified the loop earlier: content += f"  '{char}ी': '{get_char(code)}{get_char(121)}',\n"
content = content.replace("'{get_char(code)}{get_char(121)}'", "'{get_char(code)}{get_char(254)}{get_char(121)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
