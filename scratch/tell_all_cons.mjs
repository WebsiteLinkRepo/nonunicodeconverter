import { convertUnicodeToShreeLipiTelugu as conv } from '../src/utils/shreeLipiTeluguConverter.ts';

const input = "క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ప ఫ బ భ మ య ర ఱ ల ళ వ శ ష స హ క్ష";
const chars = input.split(" ");
for (let c of chars) {
  const out = conv(c);
  console.log(`${c}\t->\t${[...out].map(x => x.charCodeAt(0).toString(16).padStart(2, "0")).join(" + ")}`);
}
