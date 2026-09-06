import { unicodeToHari } from '../../src/utils/hariGujaratiConverter.js';
import fs from 'fs';

const testFile = `ભારત એક વિવિધતાથી ભરેલો દેશ છે, જ્યાં અલગ-અલગ રાજ્યોમાં લોકો જુદી-જુદી ભાષાઓ બોલે છે. અહીંની સંસ્કૃતિ, કલા અને પરંપરાઓ વિશ્વભરમાં પ્રખ્યાત છે. શિક્ષણ અને વિજ્ઞાનના ક્ષેત્રમાં પણ ગુજરાતે ખૂબ પ્રગતિ કરી છે. વિદ્યાર્થીઓએ પોતાની માતૃભાષાનું સન્માન કરવું જોઈએ અને સાથે જ જ્ઞાનનો વ્યાપ વધારવા માટે અન્ય ભાષાઓ પણ શીખવી જોઈએ. રુચિ અનુસાર નવી વસ્તુઓ શીખવાથી બુદ્ધિનો વિકાસ થાય છે. ક્રમશઃ અને શ્રમપૂર્વક કાર્ય કરવાથી સફળતા ચોક્કસ મળે છે. વૃક્ષો વાવો, પર્યાવરણ બચાવો અને પૃથ્વીને હરિયાળી બનાવો.

// Vowels
અ આ ઇ ઈ ઉ ઊ ઋ એ ઐ ઓ ઔ અં અઃ

// Consonants
ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન પ ફ બ ભ મ ય ર લ વ શ ષ સ હ ળ ક્ષ જ્ઞ

// Ka family with all matras
ક કા કિ કી કુ કૂ કૃ કે કૈ કો કૌ કં કઃ ક્ ક્ય ક્ર

// Specialized conjuncts and combinations
દ્ય દ્વ દ્દ દ્ધ દ્મ સ્ત્ર શ્ર ટ્ર ડ્ર રુ રૂ દ્ર પ્ર ર્ય ર્ક ર્ગ ર્ચ ર્જ ર્ટ ર્ડ ર્ત ર્દ ર્પ ર્બ ર્મ ર્વ ર્શ ર્ષ ર્સ ર્હ`;

const expectedFile = \`Birt a[k (v(vFtiY) Br[li[ d[S C[, ¶yi> alg-alg ri¶yi[mi> li[ki[ j&d)-j&d) BiPiai[ bi[l[ C[. ah)>n) s>AkZ(t, kli an[ pr>priai[ (vVBrmi> p\\\\²yit C[. (SxN an[ (vXinni x[#imi> pN g&jrit[ K*b p\\\\g(t kr) C[. (vwiY„ai[a[ pi[tin) mitZBiPin&> sºmin krv&> ji[Ea[ an[ siY[ j Xinni[ Äyip vFirvi miT[ aºy BiPiai[ pN S)Kv) ji[Ea[. @(c an&sir nv) vAt&ai[ S)KviY) b&(Üni[ (vkis Yiy C[. k|mS: an[ ~mp*v<k kiy< krviY) sfLti ci[Ês mL[ C[. vZxi[ vivi[, pyi<vrN bcivi[ an[ pZ¸v)n[ h(ryiL) bnivi[.

// Vowels
a ai e E u U ä a[ a] ai[ ai] a> a:

// Consonants
k K g G ઙ c C j z ઞ T q D Q N t Y d F n p f b B m y r l v S P s h L x X

// Ka family with all matras
k ki (k k) k& k* kZ k[ k] ki[ ki] k> k: k\` ±y k|

// Specialized conjuncts and combinations
w o Ñ Ü Þ à ~ T^ D^ @ $ W p\\\\ y< k< g< c< j< T< D< t< d< p< b< m< v< S< P< s< h<\`;

function compareLines(actual, expected) {
  const alignLeft = (str, len) => str.padEnd(len, ' ');
  const actualLines = actual.split('\n');
  const expectedLines = expected.split('\n');
  
  for (let i = 0; i < Math.max(actualLines.length, expectedLines.length); i++) {
    const aLine = actualLines[i] || '';
    const eLine = expectedLines[i] || '';
    if (aLine !== eLine) {
        console.log(\`Line \${i+1}:\`);
        console.log(\`A: \${aLine}\`);
        console.log(\`E: \${eLine}\`);
        
        let aChars = Array.from(aLine);
        let eChars = Array.from(eLine);
        for(let j=0; j<Math.max(aChars.length, eChars.length); j++) {
            if(aChars[j] !== eChars[j]) {
                console.log(\`Diff at \${j}: '\${aChars[j]}' (\\u\${aChars[j]?.charCodeAt(0).toString(16).padStart(4, '0')}) vs E: '\${eChars[j]}' (\\u\${eChars[j]?.charCodeAt(0).toString(16).padStart(4, '0')})\`);
            }
        }
    }
  }
}

const out = unicodeToHari(testFile);
if (out === expectedFile) {
  console.log("Success! Match is 100%");
} else {
  console.log("Difference detected:");
  compareLines(out, expectedFile);
}
