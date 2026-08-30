const topBottomMatras = ''; // removed  (ं) and  (ँ)
const bridgeRegex = new RegExp(`([][${topBottomMatras}]*)(?![])`, 'g');

const testCases = {
    'क': '',
    'कं': '',
    'कँ': '',
    'के': '',
    'कें': '',
    'का': '',
};

for (const [k, v] of Object.entries(testCases)) {
    const res = v.replace(bridgeRegex, '$1');
    const hex = Array.from(res).map(c => '0x' + c.charCodeAt(0).toString(16).toUpperCase()).join(' ');
    console.log(k, '->', hex);
}
