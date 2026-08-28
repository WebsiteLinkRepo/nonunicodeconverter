with open('generate_neo_final3.py', 'r') as f:
    lines = f.readlines()

out = []
for line in lines:
    if "content +=" in line and "'ऐ'" in line:
        continue
    if "content +=" in line and "'़'" in line:
        continue
    if "content += \"};\\n\"" in line:
        continue
    if "with open('src/utils/mappings/neo.ts" in line:
        break
    out.append(line)

out.append("content += f\"  'ऐ': '{get_char(76)}{get_char(123)}',\\n\"\n")
out.append("content += f\"  '़': '',\\n\"\n")
out.append("content += \"};\\n\"\n")
out.append("with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:\n")
out.append("    f.write(content)\n")

with open('generate_neo_final3.py', 'w') as f:
    f.writelines(out)
