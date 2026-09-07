const fs = require('fs');

const path = 'src/utils/mappings/anu7.ts';
let code = fs.readFileSync(path, 'utf8');

const regex = /(export const ANU7_UNICODE_TO_NONUNICODE:\s*MappingEntry\[\]\s*=\s*\[)/;

if (!regex.test(code)) {
    console.error("Could not find the start of the anu7 array.");
    process.exit(1);
}

const newMappings = `
  { from: "క్ష్మి", to: "\\uF0BF\\uF0A3\\uF08C\\uF088" },
  { from: "క్షి", to: "\\uF0BF\\uF0A3\\uF08C" },
  { from: "క్కి", to: "\\uF0BF\\uF0A3\\uF0D8" },
  { from: "డ్గ", to: "\\uF026\\uF083\\uF05A" },
  { from: "ద్మ", to: "\\uF03C\\uF08A\\uF088" },
  { from: "బ్య", to: "\\uF08B\\uF0AB" },
  { from: "గ్ని", to: "\\uF0D0\\uF095" },
  { from: "్ష", to: "\\uF08C" },
`;

code = code.replace(regex, "$1\n" + newMappings);

fs.writeFileSync(path, code);
console.log("Mappings inserted successfully.");
