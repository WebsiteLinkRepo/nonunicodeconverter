const ts = require('typescript');
const fs = require('fs');
const converterStr = fs.readFileSync('src/utils/converter.ts', 'utf-8');
const anu7Str = fs.readFileSync('src/utils/mappings/anu7.ts', 'utf-8');

// I'll just run their project via ts-node or similar. Wait, it's Astro.
