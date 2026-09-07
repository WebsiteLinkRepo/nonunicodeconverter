import { convertText } from './src/utils/converter';

const pairs = [
  ["అనంతలక్ష్మి", ""],
  ["బా", ""],
  ["బు", ""],
  ["బే", ""],
  ["ద్మ", ""],
  ["బ్య", ""],
  ["క్కి", ""],
  ["గ్ని", ""],
  ["డ్గ", ""],
  ["క్షి", ""],
  ["్ష", ""]
];

let failed = false;
for (const [telugu, nonUni] of pairs) {
  const fwd = convertText(telugu, "anu7", false).convertedText;
  if (fwd !== nonUni) {
    console.error(`FWD FAIL: expected '${nonUni}', got '${fwd}' for '${telugu}'`);
    failed = true;
  }

  const rev = convertText(nonUni, "anu7", true).convertedText;
  if (rev !== telugu) {
    console.error(`REV FAIL: expected '${telugu}', got '${rev}' for '${nonUni}'`);
    failed = true;
  }
}

if (!failed) console.log("ALL TESTS PASS");
