import json

with open('scratch/shree_tamil_mapping.json') as f:
    mapping_list = json.load(f)

# Sort longest first, then alphabetically
mapping_list.sort(key=lambda x: (-len(x['from']), x['from']))

ts_content = """// mapping for Tamil Unicode to Shree Lipi Tamil (e.g. SHREE-TAM7-0803)

export const SHREELIPI_TAMIL_UNICODE_TO_NONUNICODE: Array<{from: string, to: string}> = [
"""

for m in mapping_list:
    from_json = json.dumps(m['from'])
    to_json = json.dumps(m['to'])
    ts_content += f'  {{ from: {from_json}, to: {to_json} }},\n'

ts_content += "];\n"

with open('src/utils/mappings/shreeLipiTamil.ts', 'w') as f:
    f.write(ts_content)

print(f"Generated TS mapping with {len(mapping_list)} entries.")
