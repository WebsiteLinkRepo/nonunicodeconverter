import { neoMap } from './src/utils/mappings/neo.ts';

function pagemakerDownconvert(text) {
  let result = text;
  // Convert standard unicode characters to Anu bytes
  const keys = Object.keys(neoMap).sort((a, b) => b.length - a.length);
  for (const key of keys) {
    if (result.includes(key)) {
      result = result.split(key).join(neoMap[key]);
    }
  }
  
  let finalResult = '';
  for (let i = 0; i < result.length; i++) {
    let code = result.charCodeAt(i);
    if (code >= 0xF000 && code <= 0xF0FF) {
      code = code - 0xF000;
    }
    if (code >= 128 && code <= 159) {
      // Map CP1252
      const cp1252toUni = {
          128: 0x20AC, 129: 0x0081, 130: 0x201A, 131: 0x0192,
          132: 0x201E, 133: 0x2026, 134: 0x2020, 135: 0x2021,
          136: 0x02C6, 137: 0x2030, 138: 0x0160, 139: 0x2039,
          140: 0x0152, 141: 0x008D, 142: 0x017D, 143: 0x008F,
          144: 0x0090, 145: 0x2018, 146: 0x2019, 147: 0x201C,
          148: 0x201D, 149: 0x2022, 150: 0x2013, 151: 0x2014,
          152: 0x02DC, 153: 0x2122, 154: 0x0161, 155: 0x203A,
          156: 0x0153, 157: 0x009D, 158: 0x017E, 159: 0x0178
      };
      finalResult += String.fromCharCode(cp1252toUni[code]);
    } else {
      finalResult += String.fromCharCode(code);
    }
  }
  return finalResult;
}

const input = "काकी कुक्कू फौजी की फीता";
const output = pagemakerDownconvert(input);
let bytes = [];
for (let i=0; i<output.length; i++) {
  bytes.push(output.charCodeAt(i));
}
console.log(bytes.join(' '));
