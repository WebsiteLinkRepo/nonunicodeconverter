import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';

const testWords = [
  "संयुक्ताक्षरों",
  "अर्धवर्णों",
  "निर्मित",
  "वाङ्मय",
  "आयुर्वेद",
  "ग्रंथों",
  "क्लिष्ट",
  "किंकर्तव्यविमूढ़ता",
  "शृंगारिक",
  "प्रदर्शन",
  "अग्नि"
];

for (const word of testWords) {
  console.log(`${word} -> ${unicodeToAnuNeo(word)}`);
}
