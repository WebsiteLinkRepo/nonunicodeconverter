function getRtfChar(uniCode, winCode) {
    const signedUni = uniCode > 32767 ? uniCode - 65536 : uniCode;
    return `\\u${signedUni}\\'${winCode.toString(16).padStart(2, '0')}`;
}
console.log(getRtfChar(0xF08A, 0x8A));
