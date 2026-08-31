import { unicodeToAnuNeo } from './src/utils/anuNeoConverter.ts';

const words = ["कर्म", "धर्म", "शर्म", "तर्क", "तर्कण", "कर्ता"];
for (const word of words) {
    console.log(`Word: ${word}`);
    const converted = unicodeToAnuNeo(word);
    console.log(`Converted: ${converted}`);
    for (let i = 0; i < converted.length; i++) {
        console.log(`  char: ${converted[i]}, hex: 0x${converted.charCodeAt(i).toString(16).toUpperCase()}`);
    }
}
