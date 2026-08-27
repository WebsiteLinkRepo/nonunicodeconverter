with open('generate_neo_final2.py', 'r') as f:
    text = f.read()
import re
text = re.sub(r'# PRA OVERRIDES.*?(?=for k, v in map_dict)', '', text, flags=re.DOTALL)
with open('generate_neo_final2.py', 'w') as f:
    f.write(text)
