function fixReph(text: string) {
    let modified_substring = text;
    let position_of_half_R = modified_substring.indexOf("र्");
    const set_of_matras = "ािीुूृेैोौं:ँॅ";
    
    while (position_of_half_R > 0) {
        let probable_position_of_Z = position_of_half_R + 1; // index of the character after 'र्' (which is 'र' + '्', so + 2. Wait, 'र्' is length 2. 
        // position_of_half_R is index of 'र'. '्' is at position_of_half_R + 1.
        // The first char of the next syllable is position_of_half_R + 2.
        probable_position_of_Z = position_of_half_R + 2;
        
        while (probable_position_of_Z < modified_substring.length) {
            let next_char = modified_substring.charAt(probable_position_of_Z + 1);
            if (next_char === '्') {
                probable_position_of_Z += 2; // skip halant and the next consonant
            } else if (set_of_matras.includes(next_char)) {
                probable_position_of_Z += 1; // skip matra
            } else {
                break;
            }
        }
        
        const string_to_be_replaced = modified_substring.substring(
            position_of_half_R + 2,
            probable_position_of_Z + 1
        );
        modified_substring = modified_substring.replace(
            "र्" + string_to_be_replaced,
            string_to_be_replaced + "Z"
        );
        
        position_of_half_R = modified_substring.indexOf("र्");
    }
    return modified_substring;
}

console.log(fixReph("अर्द्धवर्णों"));
console.log(fixReph("मार्मिक"));
