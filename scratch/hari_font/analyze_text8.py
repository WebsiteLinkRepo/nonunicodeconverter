# pyi<vrN = p y i < v r N => પર્યાવરણ
# y + ા(i) + < + v
# My text: py<ivrN => p y < i v r N
# Wait, my logic output `<` before `i`. 
# In `src/utils/hariGujaratiConverter.ts`:
# const rephaRegex = new RegExp(`ર${halant}(${consonantCluster})`, 'g');
# converted = converted.replace(rephaRegex, '$1<');

# In 'પર્યાવરણ' (p a r y a v a r a n), Unicode is: પ ર ્ ય ા વ ર ણ.
# So 'ર' + halant + 'ય' ('ય' is the consonant cluster).
# So my regex replaces it with 'ય' + '<'. 
# Then later 'ા' is converted to 'i'. So we get 'y<i'.
# Expected is 'yi<'. So repha suffix ('<') comes AFTER the matras (like 'ા') attached to that character!
# Ah! In Hari font, repha comes after the full syllable (consonant + matra).
# Let's fix the converter logic!
