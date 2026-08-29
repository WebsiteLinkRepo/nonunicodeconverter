import subprocess, json

# Test script that runs both converters
code = """
import { unicodeToKrutidev } from './src/utils/krutiDevConverter';
import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';

const input = "डॉक्टर विज्ञान प्रौद्योगिकी छुट्टी उद्देश्य धर्म कर्म क्षमा ज्ञान त्रिशूल श्रम द्रौपदी";

const kruti = unicodeToKrutidev(input);
const neo = unicodeToAnuNeo(input);

console.log("=== KRUTI DEV OUTPUT ===");
console.log("Text:", kruti);
console.log("Chars:", [...kruti].map(c => c + '(' + c.charCodeAt(0) + ')').join(' '));

console.log("\\n=== NEO OUTPUT ===");
console.log("Text:", neo);
console.log("Chars:", [...neo].map(c => {
    let code = c.charCodeAt(0);
    if (code >= 0xF000 && code <= 0xF0FF) {
        return 'B' + (code - 0xF000);
    }
    return c + '(' + code + ')';
}).join(' '));

// Now let's trace word by word
const words = ["धर्म", "कर्म", "उद्देश्य", "प्रौद्योगिकी"];
for (const w of words) {
    console.log("\\n--- " + w + " ---");
    const k = unicodeToKrutidev(w);
    const n = unicodeToAnuNeo(w);
    console.log("Kruti:", k, "| chars:", [...k].map(c => c + '(' + c.charCodeAt(0) + ')').join(' '));
    console.log("Neo:  ", n, "| bytes:", [...n].map(c => {
        let code = c.charCodeAt(0);
        if (code >= 0xF000 && code <= 0xF0FF) return 'B' + (code - 0xF000);
        return c + '(' + code + ')';
    }).join(' '));
}
"""

with open('trace_both.ts', 'w') as f:
    f.write(code)

