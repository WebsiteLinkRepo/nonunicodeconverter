import { convertText } from './src/utils/converter.js';

try {
  console.log("Testing converter...");
  const res = convertText("హిందీ", "anu7", false, false, "telugu");
  console.log("Result:", res);
} catch (e) {
  console.error("Error:", e);
}
