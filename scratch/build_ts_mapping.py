import json

with open('scratch/shree_mapping_draft.json', 'r', encoding='utf-8') as f:
    mapping_dict = json.load(f)

# Sort by length of unicode key descending so greedy matching works
sorted_items = sorted(mapping_dict.items(), key=lambda x: len(x[0]), reverse=True)

with open('src/utils/mappings/shreeLipi.ts', 'w', encoding='utf-8') as f:
    f.write('// Comprehensive Shree-Lipi (Shree-Dev7) Devanagari Mapping Table\n')
    f.write('export interface MappingEntry {\n')
    f.write('  from: string;\n')
    f.write('  to: string;\n')
    f.write('}\n\n')
    f.write('export const SHREE_LIPI_MAPPINGS: MappingEntry[] = [\n')
    for k, v in sorted_items:
        # JSON serialize the strings to safely escape characters
        k_json = json.dumps(k, ensure_ascii=False)
        v_json = json.dumps(v, ensure_ascii=False)
        f.write(f'  {{ from: {k_json}, to: {v_json} }},\n')
    f.write('];\n')

print(f'Successfully wrote {len(sorted_items)} entries to src/utils/mappings/shreeLipi.ts')
