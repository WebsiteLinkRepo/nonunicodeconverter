import { unicodeToAnu6 } from './src/utils/anu6Converter';

function pagemakerDownconvert(text: string) {
  return text.replace(/[-]/g, match => {
    const code = match.charCodeAt(0) - 0xF000;
    if (code >= 128 && code <= 159) {
      const cp1252toUni: Record<number, number> = {
        128: 0x20AC, 129: 0x0081, 130: 0x201A, 131: 0x0192,
        132: 0x201E, 133: 0x2026, 134: 0x2020, 135: 0x2021,
        136: 0x02C6, 137: 0x2030, 138: 0x0160, 139: 0x2039,
        140: 0x0152, 141: 0x008D, 142: 0x017D, 143: 0x008F,
        144: 0x0090, 145: 0x2018, 146: 0x2019, 147: 0x201C,
        148: 0x201D, 149: 0x2022, 150: 0x2013, 151: 0x2014,
        152: 0x02DC, 153: 0x2122, 154: 0x0161, 155: 0x203A,
        156: 0x0153, 157: 0x009D, 158: 0x017E, 159: 0x0178
      };
      return String.fromCharCode(cp1252toUni[code]);
    }
    return String.fromCharCode(code);
  });
}

const input = "కౄరమృగము ౠషి 'కోట్'";
const anu6 = unicodeToAnu6(input);
const myConverted = pagemakerDownconvert(anu6);

const compLine = "H›$ì~¡=°$Q®=ò |°¶+² 'HË\\˜Ñ";

console.log("Analyzing char mapping...");

let diffCount = 0;
for (let i = 0; i < Math.max(compLine.length, myConverted.length); i++) {
   const compCode = i < compLine.length ? compLine.charCodeAt(i) : null;
   const myCode = i < myConverted.length ? myConverted.charCodeAt(i) : null; 
   if (compCode !== myCode && diffCount < 20) {
      console.log(`Mismatch at ${i}:\n  Comp: ${compCode ? compCode.toString(16).padStart(4, '0') : 'none'} char: ${String.fromCharCode(compCode || 32)}\n  My  :   ${myCode ? myCode.toString(16).padStart(4, '0') : 'none'} char: ${String.fromCharCode(myCode || 32)}\n`);
      diffCount++;
   }
}
if (diffCount === 0) console.log("Perfect match!");
