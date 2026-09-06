import { unicodeToHari } from '../../src/utils/hariGujaratiConverter';
import * as fs from 'fs';

const inputText = "ભારત એક વિવિધતાથી ભરેલો દેશ છે, જ્યાં અલગ-અલગ રાજ્યોમાં લોકો જુદી-જુદી ભાષાઓ બોલે છે. અહીંની સંસ્કૃતિ, કલા અને પરંપરાઓ વિશ્વભરમાં પ્રખ્યાત છે. શિક્ષણ અને વિજ્ઞાનના ક્ષેત્રમાં પણ ગુજરાતે ખૂબ પ્રગતિ કરી છે. વિદ્યાર્થીઓએ પોતાની માતૃભાષાનું સન્માન કરવું જોઈએ અને સાથે જ જ્ઞાનનો વ્યાપ વધારવા માટે અન્ય ભાષાઓ પણ શીખવી જોઈએ. રુચિ અનુસાર નવી વસ્તુઓ શીખવાથી બુદ્ધિનો વિકાસ થાય છે. ક્રમશઃ અને શ્રમપૂર્વક કાર્ય કરવાથી સફળતા ચોક્કસ મળે છે. વૃક્ષો વાવો, પર્યાવરણ બચાવો અને પૃથ્વીને હરિયાળી બનાવો.";

const expected = "Birt a[k (v(vFtiY) Br[li[ d[S C[, ¶yi> alg-alg ri¶yi[mi> li[ki[ j&d)-j&d) BiPiai[ bi[l[ C[. ah)>n) s>AkZ(t, kli an[ pr>priai[ (vVBrmi> p\\²yit C[. (SxN an[ (vXinni x[#imi> pN g&jrit[ K*b p\\g(t kr) C[. (vwiY„ai[a[ pi[tin) mitZBiPin&> sºmin krv&> ji[Ea[ an[ siY[ j Xinni[ Äyip vFirvi miT[ aºy BiPiai[ pN S)Kv) ji[Ea[. @(c an&sir nv) vAt&ai[ S)KviY) b&(Üni[ (vkis Yiy C[. k|mS: an[ ~mp*v<k kiy< krviY) sfLti ci[Ês mL[ C[. vZxi[ vivi[, pyi<vrN bcivi[ an[ pZ¸v)n[ h(ryiL) bnivi[.";

const actual = unicodeToHari(inputText);

if (actual === expected) {
    console.log("Success! Output matches perfectly.");
} else {
    console.log("Difference found:");
    console.log("Expected length:", expected.length);
    console.log("Actual length:", actual.length);
    
    let minLen = Math.min(actual.length, expected.length);
    for (let i = 0; i < minLen; i++) {
        if (actual[i] !== expected[i]) {
            console.log(`Mismatch at index ${i}: Expected '${expected[i]}' (code ${expected.charCodeAt(i)}), got '${actual[i]}' (code ${actual.charCodeAt(i)})`);
            // Show surrounding context
            let start = Math.max(0, i - 10);
            let end = Math.min(minLen, i + 10);
            console.log(`Context: expected -> ${expected.substring(start, end)}`);
            console.log(`Context: actual   -> ${actual.substring(start, end)}\n`);
            break;
        }
    }
}
