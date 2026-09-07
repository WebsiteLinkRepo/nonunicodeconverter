import fs from 'fs';

const path = 'src/utils/mappings/anu7.ts';
let code = fs.readFileSync(path, 'utf8');

// Replace specific elements in the anu7 structure:
// \{ from: "క్ష్మి", to: "..."\}
function replaceMapping(fromStr, newToStr) {
    const regex = new RegExp(`\\{\\s*from:\\s*"${fromStr}",\\s*to:\\s*"[^"]*"\\s*\\}`, 'g');
    if (code.match(regex)) {
        code = code.replace(regex, `{ from: "${fromStr}", to: "${newToStr}" }`);
    } else {
        // Find the generic starting place and stick it there since it doesn't exist
        const startRegex = /(export const ANU7_UNICODE_TO_NONUNICODE:\s*MappingEntry\[\]\s*=\s*\[)/;
        code = code.replace(startRegex, `$1\n  { from: "${fromStr}", to: "${newToStr}" },`);
    }
}

// క్ష్మి -> ¿£Œˆ ()
replaceMapping("క్ష్మి", "\\uF0BF\\uF0A3\\uF08C\\uF088");

// క్షి -> ¿£Œ ()
replaceMapping("క్షి", "\\uF0BF\\uF0A3\\uF08C");

// క్కి -> ¿£Ø (\\uF0D8)
replaceMapping("క్కి", "\\uF0BF\\uF0A3\\uF0D8");

// డ్గ -> &ƒZ ()
replaceMapping("డ్గ", "\\uF026\\uF083\\uF05A");

// ద్మ -> <Šˆ ()
replaceMapping("ద్మ", "\\uF03C\\uF08A\\uF088");

// బ్య -> ‹« ()
replaceMapping("బ్య", "\\uF08B\\uF0AB");

// గ్ని -> Ð• ()
replaceMapping("గ్ని", "\\uF0D0\\uF095");

// ష vattu: ్ష -> Œ ()
replaceMapping("్ష", "\\uF08C");

fs.writeFileSync(path, code);
console.log("Replaced successfully!");
