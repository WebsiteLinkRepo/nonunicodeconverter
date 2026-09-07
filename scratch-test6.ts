import { getMapping } from './src/utils/mappings/index';
const anu7 = getMapping("anu7", false);

["డ్కు", "డు", "డూ"].forEach(word => {
  const match = anu7.find(e => e.from === word);
  if (match) {
    console.log(`${word} -> ${match.to.split('').map(c=>'\\u'+c.charCodeAt(0).toString(16).toUpperCase()).join('')}`);
  }
});
