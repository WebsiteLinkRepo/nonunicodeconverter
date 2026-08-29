import { convertText } from './src/utils/converter';

const input = "डॉक्टर विज्ञान प्रौद्योगिकी छुट्टी उद्देश्य धर्म कर्म क्षमा ज्ञान त्रिशूल श्रम द्रौपदी";

// Convert to Hindi (NeoGanesh) using anu7 encoding
const res = convertText(input, 'anu7', false, false, 'hindi');

console.log("Original:", input);
console.log("Converted (raw):", res.convertedText);

// Print the byte values of the converted string
const bytes = [];
for (let i = 0; i < res.convertedText.length; i++) {
    let code = res.convertedText.charCodeAt(i);
    // Print the mapped ANSI code (subtracting 0xF000 if it's in the PUA block)
    if (code >= 0xF000 && code <= 0xF0FF) {
        bytes.push(code - 0xF000);
    } else {
        bytes.push(code);
    }
}
console.log("Bytes:", bytes.join(", "));

