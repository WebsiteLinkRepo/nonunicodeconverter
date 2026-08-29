import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';
console.log(unicodeToAnuNeo("कर्म").split('').map(c => {
    const code = c.charCodeAt(0);
    return code >= 0xF000 ? 'B' + (code - 0xF000).toString() : c;
}).join(' '));
