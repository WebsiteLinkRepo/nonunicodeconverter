import { convertText } from './src/utils/converter';

const pairs = [
  {pua: "", expected: "డగ్గ"},
  {pua: "", expected: "ద్భు"},
  {pua: "", expected: "కృ"},
  {pua: "", expected: "క్ష"},
  {pua: "", expected: "క్ష్మి"},
  {pua: "", expected: "అనంతలక్ష్మి"}
];

pairs.forEach(p => {
  const fw = convertText(p.expected, "anu7", false).convertedText;
  const fw_hex = fw.split('').map(c=>'\\u'+c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')).join('');
  const pua_hex = p.pua.split('').map(c=>'\\u'+c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')).join('');
  console.log(`${p.expected}: Expected PUA -> ${pua_hex}, Act FWD -> ${fw_hex}`);
});
