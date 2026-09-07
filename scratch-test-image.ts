import { getMapping } from './src/utils/mappings/index';

const anu7 = getMapping("anu7", false);
const res = [];
["¿£Œ", "¿£Ø", "£", "Œ"].forEach(s => {
  const hex = s.split('').map(c=>'\\uF0'+c.charCodeAt(0).toString(16).toUpperCase().padStart(2, '0')).join('');
  res.push(`${s} -> ${hex}`);
});
console.log(res.join("\n"));
