import { convertText } from './src/utils/converter';

// Build a mapping from standard win1252 to buffer matching it. 
// Just manually hardcode what node did for the string (win1252 to unicode)
const charToWin1252Hex = {
  "u": 0x75,
  "²": 0xB2,
  "‹": 0x8B,
  "T": 0x54,
  "ñ": 0xF1,
  "<": 0x3C,
  "Š": 0x8A,
  "ˆ": 0x88,
  "«": 0xAB,
  "¿": 0xBF,
  "£": 0xA3,
  "Ø": 0xD8,
  "Ð": 0xD0,
  "•": 0x95,
  "&": 0x26,
  "ƒ": 0x83,
  "Z": 0x5A,
  "Œ": 0x8C
};

const words = ["u²", "‹T", "uñ", "<Šˆ", "‹«", "¿£Ø", "Ð•", "&ƒZ", "¿£Œ"];

words.forEach(w => {
  const pua = w.split("").map(c => String.fromCharCode(0xF000 + charToWin1252Hex[c])).join("");
  const telugu = convertText(pua, "anu7", true).convertedText;
  console.log(`${w} -> PUA: ${pua.split("").map(c => "\\u"+c.charCodeAt(0).toString(16)).join("")} -> Telugu: ${telugu}`);
  
  const fw = convertText(telugu, "anu7", false).convertedText;
  const match = fw === pua ? "MATCH" : `MISMATCH: got ${fw.split("").map(c => "\\u"+c.charCodeAt(0).toString(16)).join("")}`;
  console.log(`      FWD -> ${match}`);
});
