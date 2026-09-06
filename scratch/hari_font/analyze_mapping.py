uni_vowels = "અ આ ઇ ઈ ઉ ઊ ઋ એ ઐ ઓ ઔ અં અઃ".split(" ")
har_vowels = "a ai e E u U ä a[ a] ai[ ai] a> a:".split(" ")
print("VOWELS:")
for u, h in zip(uni_vowels, har_vowels):
    print(f"{u} (U+{ord(u[0]):04X}) -> {h}")

uni_cons = "ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન પ ફ બ ભ મ ય ર લ વ શ ષ સ હ ળ ક્ષ જ્ઞ".split(" ")
har_cons = "k K g G ઙ c C j z ઞ T q D Q N t Y d F n p f b B m y r l v S P s h L x X".split(" ")
print("\nCONSONANTS:")
for u, h in zip(uni_cons, har_cons):
    print(f"{u} (U+{ord(u[0]):04X}) -> {h}")

uni_ka = "ક કા કિ કી કુ કૂ કૃ કે કૈ કો કૌ કં કઃ ક્ ક્ય ક્ર".split(" ")
har_ka = "k ki (k k) k& k* kZ k[ k] ki[ ki] k> k: k` ±y k|".split(" ")
print("\nKA FAMILY:")
for u, h in zip(uni_ka, har_ka):
    print(f"{u} -> {h}")

uni_sp = "દ્ય દ્વ દ્દ દ્ધ દ્મ સ્ત્ર શ્ર ટ્ર ડ્ર રુ રૂ દ્ર પ્ર ર્ય ર્ક ર્ગ ર્ચ ર્જ ર્ટ ર્ડ ર્ત ર્દ ર્પ ર્બ ર્મ ર્વ ર્શ ર્ષ ર્સ ર્હ".split(" ")
har_sp = ['w', 'o', 'Ñ', 'Ü', 'Þ', 'à', '~', 'T^', 'D^', '@', '$', 'W', 'p\\', 'y<', 'k<', 'g<', 'c<', 'j<', 'T<', 'D<', 't<', 'd<', 'p<', 'b<', 'm<', 'v<', 'S<', 'P<', 's<', 'h<']
print("\nSPECIAL conjuncts:")
for u, h in zip(uni_sp, har_sp):
    print(f"{u} -> {h}")
