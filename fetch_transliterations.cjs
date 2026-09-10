const fs = require('fs');

const teluguFonts = ["Aaradhana","Amrutha","BapuBold","BapuBrush","BapuScript","BrahmaScript","ChandraScript","Kusuma","Maanasa","Madhubala","RamanaBrush","RamanaScriptMedium","RamanaScript","Subhadra","Abhilasha","Ajantha","Akshara","Anjali","AnupamaBold","AnupamaExtraBold","AnupamaMedium","AnupamaThin","Anusha","AnuSubhalekhaOne","AnuSubhalekhaTwo","Apoorva","Ashwini","Avanthi","Bharghava","Bhavya","Brahma","Charitha","Deepika","Dharani","DingbitsEight","DingbitsEleven","DingbitsFive","DingbitsFour","DingbitsNine","DingbitsOne","DingbitsSeven","DingbitsSix","DingbitsTen","DingbitsThirteen","DingbitsThree","DingbitsTwelve","DingbitsTwo","Geetha","GowthamiBlack","GowthamiBold","GowthamiExtraBold","GowthamiMedium","GowthamiNarrow","GowthamiThin","Harsha","Hiranya","Jyothi","Kalaanjali","KeerthiFont","Kranthi","MeenaScript","Mohini","Natyamayuri","Neelima","Padmini","PallaviBold","PallaviMedium","PallaviThin","Prabhava","Pragathi","PragathiItalic","PragathiNarrow","PragathiSpecial","Praveena","Preethi","Pridhvi","Priyaanka","PriyaankaBold","Rachana","RachanaBold","Ravali","Reshma","Rohini","Saagari","Sanghavi","Sowmya","Sravya","Srujana","Suchithra","Sujatha","Suneetha","Supriya","Tejafont","TeluguNumbersBold","TeluguNumbersThin","Thripura","Udayam","Vaibhav","Vasantha","Vasundhara","Veenaa","Vikaas"];

const hindiFonts = ["NeoChandanBold","NeoChandanLight","NeoElephantaBold","NeoElephantaLight","NeoEurostyleBold","NeoEurostyleLight","NeoEurostyleMedium","NeoGaneshBold","NeoGaneshLight","NeoHansaBold","NeoHansaLight","NeoJavaharBold","NeoJavaharLight","NeoJyothiBold","NeoJyothiLight","NeoKailashBold","NeoKailashLight","NeoKailashMedium","NeoMahanBold","NeoMahanLight","NeoMahanMedium","NeoMangalBold","NeoMangalLight","NeoMangalMedium","NeoMitraBold","NeoMitraLight","NeoMitraMedium","NeoMonoharBold","NeoMonoharLight","NeoMonoharMedium","NeoNatrajBold","NeoNatrajLight","NeoNatrajMedium","NeoNileshBold","NeoNileshLight","NeoNileshMedium","NeoOmkarBold","NeoOmkarLight","NeoOmkarMedium","NeoPradnyaBold","NeoPradnyaLight","NeoRadhikaBold","NeoRadhikaLight","NeoRadhikaMedium","NeoShridharBold","NeoShridharLight","NeoShridharMedium","NeoShwetaBold","NeoShwetaLight","NeoShwetaMedium","NeoYogeshBold","NeoYogeshLight","NeoYogeshMedium"];

async function transliterate(text, langCode) {
    const spaceText = text.replace(/([a-z])([A-Z])/g, '$1 $2');
    const url = `https://inputtools.google.com/request?text=${encodeURIComponent(spaceText)}&itc=${langCode}-t-i0-und&num=1&cp=0&cs=1&ie=utf-8&oe=utf-8`;
    try {
        const res = await fetch(url);
        const data = await res.json();
        if (data[0] === 'SUCCESS') {
            const matches = data[1];
            let out = [];
            for (let m of matches) {
                out.push(m[1][0]);
            }
            return out.join(' ');
        }
    } catch(e) { console.error(e); }
    return spaceText;
}

async function run() {
    const teluguMap = {};
    for (let f of teluguFonts) {
        teluguMap[f] = await transliterate(f, 'te');
    }
    
    const hindiMap = {};
    for (let f of hindiFonts) {
        let name = f;
        if(name.startsWith('Neo')) name = 'Neo ' + name.substring(3);
        hindiMap[f] = await transliterate(name, 'hi');
    }

    fs.writeFileSync('/home/samuelvictor/nonunicodeconverter.com/src/utils/transliterations.json', JSON.stringify({te: teluguMap, hi: hindiMap}, null, 2));
    console.log("Done generating transliterations.json");
}

run();
