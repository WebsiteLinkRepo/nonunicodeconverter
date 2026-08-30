const code = 0xF0FE;
const signedUni = code > 32767 ? code - 65536 : code;
const winCode = code - 0xF000;
console.log(`\\u${signedUni}\\'${winCode.toString(16).padStart(2, '0')}`);
// \u-3842\'fe
