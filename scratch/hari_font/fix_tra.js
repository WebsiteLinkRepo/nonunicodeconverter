const fs = require('fs');
const file = 'src/utils/mappings/hariGujarati.ts';
let data = fs.readFileSync(file, 'utf8');
data = data.replace("{ from: 'ત્ર', to: '#' },", "{ from: 'ત્ર', to: '#i' },");
fs.writeFileSync(file, data);
