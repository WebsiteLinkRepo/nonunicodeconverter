const fs = require('fs');

const inputStr = fs.readFileSync('telugu_test_full.md', 'utf8');
const outputStr = `J
P
W
D
L
T
|°°
|°¶
Z
U
S
X
F
B
JO
J—
H›
Y
Q®
„¦¬°
V
KÇ
KÇ
[
~¡
&
@
~”¡
_È
_È
}
\`Ç
^ŠÎ
^Î
^Î
#
„¬
„¦¬
|
ƒ’
=°
†Ç°
~¡
\\
=
‰×
+¬
‹¬
‚¬ì
ˆ×
H›Æ
Ž
H›
Hê
H÷
H©
ä›½
ä›€
H›$
H›$ì
ïH
öH
ïHá
Hù
HË
HÒ
H›O
H›:
H›ø
Yš
Q®¾
„¦¬°É
VV
KÇó
KÇó
[û
~¡~¡
&ý
@“
~”¡»
_ÈÛ
_È_
}â
\`Çë
^ŠÎÖ
^Îí
^Îœ
#ß
„¬æ
„¦¬æ
|Ä
ƒ’Ä
=°à
†Ç°¼
ã~¡
Á
=Þ
‰×Å
+¬Â
‹¬ž
‚¬ì
ˆ×¤
H›ÆøÂ
Ž]`;

const inLines = inputStr.split('\n').map(l => l.trim()).filter(l => l.length > 0);
const outLines = outputStr.split('\n').map(l => l.trim()).filter(l => l.length > 0);

if (inLines.length !== outLines.length) {
  console.log(`Mismatch! in: ${inLines.length}, out: ${outLines.length}`);
}

const map = [];
for(let i=0; i<Math.min(inLines.length, outLines.length); i++) {
    map.push(`  { from: "${outLines[i].replace(/\\/g, '\\\\').replace(/"/g, '\\"')}", to: "${inLines[i]}" },`);
}

fs.writeFileSync('anu6_mapping.txt', `export const ANU6_UNICODE_TO_NONUNICODE = [\n${map.join('\n')}\n];`);
console.log("Written to anu6_mapping.txt");
