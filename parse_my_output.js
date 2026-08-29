const str = "          ";
const words = str.split(' ');

for (let i = 0; i < words.length; i++) {
    const word = words[i];
    console.log("Word " + i + ": " + word);
    for (let j = 0; j < word.length; j++) {
        let code = word.charCodeAt(j);
        if (code >= 0xF000) code -= 0xF000;
        console.log("  " + word[j] + " : " + code + " (Hex: " + code.toString(16) + ")");
    }
}
