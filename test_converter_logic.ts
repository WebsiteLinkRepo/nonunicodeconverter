const mapping = [ { from: '\u0915\u094D\u0937', to: '\uF0DF' } ];
const script = 'hindi';
const offset = 0x0300;

let processedMapping = mapping.map(entry => {
  let shiftedFrom = '';
  for (let i = 0; i < entry.from.length; i++) {
    const code = entry.from.charCodeAt(i);
    if (code >= 0x0900 && code <= 0x097F) shiftedFrom += String.fromCharCode(code + offset);
    else shiftedFrom += entry.from[i];
  }
  return { from: shiftedFrom, to: entry.to };
});

const lookupMap: Record<string, string> = {};
for (const entry of processedMapping) {
  if (entry.from) {
    lookupMap[entry.from] = entry.to;
  }
}

const input = '\u0C15\u0C4D\u0C37';
console.log('Value in lookupMap:', lookupMap[input]);
