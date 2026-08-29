import generate_neo_final3
for k, v in generate_neo_final3.map_dict.items():
    if k == '्':
        print(f"Key: {k}, Value: {v}, Hex: {hex(0xF000 + v)}")
