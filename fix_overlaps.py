with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "'की':" in line or "'फी':" in line:
        # Remove bridge 254
        line = line.replace("{get_char(254)}", "")
    new_lines.append(line)

content = "".join(new_lines)

# Add overrides for shifted U and OO matras for K and F
content = content.replace("};\n", "")
content += "  'कु': '{get_char(78)}{get_char(237)}',\n"
content += "  'कू': '{get_char(78)}{get_char(239)}',\n"
content += "  'फु': '{get_char(162)}{get_char(237)}',\n"
content += "  'फू': '{get_char(162)}{get_char(239)}',\n"
content += "};\n"

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
