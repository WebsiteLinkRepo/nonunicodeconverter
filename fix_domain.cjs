const fs = require('fs');
let code = fs.readFileSync('src/utils/security.ts', 'utf8');

code = code.replace(
  "host.includes('unicode2nonunicode.com') ||",
  "host.includes('unicode2nonunicode.com') || \n      host.includes('nonunicodeconverter.com') ||"
);

fs.writeFileSync('src/utils/security.ts', code);
