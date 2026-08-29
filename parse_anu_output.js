const str = "gç}Mbº uÄrçŒ Zìcy GñÅ® ‡ª|| Nþª| qªç rçŒ uÞÆîÂ Èª üç{œty";
const words = str.split(' ');

for (let i = 0; i < words.length; i++) {
    const word = words[i];
    console.log("Word " + i + ": " + word);
    for (let j = 0; j < word.length; j++) {
        console.log("  " + word[j] + " : " + word.charCodeAt(j) + " (Hex: " + word.charCodeAt(j).toString(16) + ")");
    }
}
