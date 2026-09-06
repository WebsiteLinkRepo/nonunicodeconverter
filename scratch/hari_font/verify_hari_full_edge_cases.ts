import { unicodeToHari } from '../../src/utils/hariGujaratiConverter';

// Let's test the vowel output directly from our first test sequence
const inputVowels = "અ આ ઇ ઈ ઉ ઊ ઋ એ ઐ ઓ ઔ અં અઃ";
const inputConsonants = "ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન પ ફ બ ભ મ ય ર લ વ શ ષ સ હ ળ ક્ષ જ્ઞ";
const inputKaFamily = "ક કા કિ કી કુ કૂ કૃ કે કૈ કો કૌ કં કઃ ક્ ક્ય ક્ર";
const inputConjuncts = "દ્ય દ્વ દ્દ દ્ધ દ્મ સ્ત્ર શ્ર ટ્ર ડ્ર રુ રૂ દ્ર પ્ર ર્ય ર્ક ર્ગ ર્ચ ર્જ ર્ટ ર્ડ ર્ત ર્દ ર્પ ર્બ ર્મ ર્વ ર્શ ર્ષ ર્સ ર્હ";

const expectedVowels = "a ai e E u U ä a[ a] ai[ ai] a> a:";
const expectedConsonants = "k K g G ઙ c C j z ઞ T q D Q N t Y d F n p f b B m y r l v S P s h L x X";
const expectedKaFamily = "k ki (k k) k& k* kZ k[ k] ki[ ki] k> k: k` ±y k|";
const expectedConjuncts = "w o Ñ Ü Þ à ~ T^ D^ @ $ W p\\ y< k< g< c< j< T< D< t< d< p< b< m< v< S< P< s< h<";

const check = (name: string, input: string, expected: string) => {
    const actual = unicodeToHari(input);
    if (actual === expected) {
        console.log(`${name}: Passed`);
    } else {
        console.log(`${name}: FAILED`);
        console.log(`Expected: ${expected}`);
        console.log(`Actual  : ${actual}`);
    }
};

check("Vowels", inputVowels, expectedVowels);
check("Consonants", inputConsonants, expectedConsonants);
check("Ka Family", inputKaFamily, expectedKaFamily);
check("Conjuncts", inputConjuncts, expectedConjuncts);
