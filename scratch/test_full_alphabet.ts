import { convertText } from '../src/utils/converter';
const input = "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ల వ శ ష స హ ళ క్ష ఱ";
const chars = input.split(' ');
console.log("Char | Shree Out | Hex");
for (const c of chars) {
  const result = convertText(c, 'shreelipi', false, false, 'telugu');
  const shree = result.convertedText;
  const hex = typeof shree === 'string' ? [...shree].map(x => x.charCodeAt(0).toString(16).padStart(2, '0')).join(' ') : JSON.stringify(shree);
  console.log(`${c} | ${shree} | ${hex}`);
}
