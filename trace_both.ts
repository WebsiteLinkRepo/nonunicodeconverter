import { unicodeToKrutidev } from './src/utils/krutiDevConverter';
import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';

const words = ["धर्म", "कर्म", "उद्देश्य", "प्रौद्योगिकी"];
for (const w of words) {
    console.log("\n--- " + w + " ---");
    const k = unicodeToKrutidev(w);
    const n = unicodeToAnuNeo(w);
    console.log("Kruti:", k);
    console.log("Kruti chars:", [...k].map(c => c + '(' + c.charCodeAt(0) + ')').join(' '));
    console.log("Neo bytes:", [...n].map(c => {
        let code = c.charCodeAt(0);
        if (code >= 0xF000 && code <= 0xF0FF) return 'B' + (code - 0xF000);
        return c + '(' + code + ')';
    }).join(' '));
}
