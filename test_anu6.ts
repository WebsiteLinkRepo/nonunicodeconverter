import { convertText } from './src/utils/converter';

const text = `అ ఆ ఇ ఈ ఉ ఊ ఋ ఎ ఏ ఐ ఒ ఓ ఔ అం అః
క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ
0 1 2 3 4 5 6 7 8 9`;

console.log("=== OUR ANU 6.0 OUTPUT ===");
console.log(convertText(text, 'anu6'));

console.log("\n=== OUR ANU 7.0 OUTPUT ===");
console.log(convertText(text, 'anu7'));
