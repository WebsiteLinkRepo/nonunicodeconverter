import { neoMap } from './src/utils/mappings/neo';
for (const key in neoMap) {
  let s = neoMap[key];
  let fixed = "";
  for (let i = 0; i < s.length; i++) {
    let code = s.charCodeAt(i);
    if (code >= 0xF000 && code <= 0xF0FF) {
      fixed += String.fromCharCode(code - 0xF000);
    } else {
      fixed += s[i];
    }
  }
  console.log(`${key}: ${fixed}`);
}
