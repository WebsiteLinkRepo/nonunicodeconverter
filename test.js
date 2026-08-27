const code = `
  outputText.addEventListener('copy', (e) => {
    const pmChk = document.getElementById('pagemaker-chk');
    if (pmChk && pmChk.checked) {
      e.preventDefault();
      let text = window.getSelection().toString() || outputText.value;
      text = text.replace(/[\\uF000-\\uF0FF]/g, match => {
        const code = match.charCodeAt(0) - 0xF000;
        if (code >= 128 && code <= 159) {
          const map = {128: 0x20AC, 129: 0x0081, 130: 0x201A, 131: 0x0192, 132: 0x201E, 133: 0x2026, 134: 0x2020, 135: 0x2021, 136: 0x02C6, 137: 0x2030, 138: 0x0160, 139: 0x2039, 140: 0x0152, 141: 0x008D, 142: 0x017D, 143: 0x008F, 144: 0x0090, 145: 0x2018, 146: 0x2019, 147: 0x201C, 148: 0x201D, 149: 0x2022, 150: 0x2013, 151: 0x2014, 152: 0x02DC, 153: 0x2122, 154: 0x0161, 155: 0x203A, 156: 0x0153, 157: 0x009D, 158: 0x017E, 159: 0x0178};
          return String.fromCharCode(map[code]);
        }
        return String.fromCharCode(code);
      });
      e.clipboardData.setData('text/plain', text);
    }
  });
`;
