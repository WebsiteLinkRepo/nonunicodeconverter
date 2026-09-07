const syllableRegex = /(?:(?:[అ-ఔ]|(?:[క-హౘ-ౚ](?:్[క-హౘ-ౚ])*[ా-ౌ్]?))[ంః]?)/g;
let resultText = "ఋ";
let out = resultText.replace(syllableRegex, (syllable) => {
    return "X" + syllable;
});
console.log("syllableRegex test:", out);
