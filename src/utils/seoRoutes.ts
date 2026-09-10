import { TRANSLATIONS, type Language } from './i18n';
import { HINDI_NEO_FONTS, TELUGU_RAA_FONTS, TELUGU_NORMAL_FONTS } from './fontLists';
import TRANSLITERATIONS from './transliterations.json';

interface SeoProps {
  script: string;
  format: string;
  exactFont?: string;
  title: string;
  h1: string;
  desc: string;
  keys: string;
  badge?: string;
}

const ALL_TELUGU_FONTS = [...TELUGU_RAA_FONTS, ...TELUGU_NORMAL_FONTS];

function formatFontName(label: string): string {
    return label.replace(/([a-z])([A-Z])/g, '$1 $2');
}

function getBaseRoutes(lang: Language): { params: { lang?: string, converter: string }, props: SeoProps }[] {
    const isEn = lang === 'en';
    
    // Helper to generate text based on language
    const getSeoTexts = (targetScript: string, targetFormatStr: string, fontNameStr: string = '') => {
        const fontDisplay = fontNameStr || targetFormatStr;
        
        switch (lang) {
            case 'te':
                return {
                    title: `యూనికోడ్ నుండి ${fontDisplay} కన్వర్టర్ ఆన్లైన్లో ఉచితం | Unicode to ${fontDisplay.toLowerCase()} converter free online`,
                    h1: `యూనికోడ్ నుండి ${fontDisplay} కన్వర్టర్`,
                    desc: `యూనికోడ్ నుండి ${fontDisplay} కన్వర్టర్. Convert Telugu Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, telugu unicode to anu converter, anu script converter`
                };
            case 'hi':
                return {
                    title: `यूनिकोड से ${fontDisplay} कनवर्टर | Unicode to ${fontDisplay.toLowerCase()} converter free online`,
                    h1: `यूनिकोड से ${fontDisplay} कनवर्टर`,
                    desc: `यूनिकोड से ${fontDisplay} कनवर्टर। Convert Hindi Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, hindi unicode to anu neo converter`
                };
            case 'ta':
                return {
                    title: `யூனிகோட் முதல் ${fontDisplay} மாற்றி | Unicode to ${fontDisplay.toLowerCase()} converter free online`,
                    h1: `யூனிகோட் முதல் ${fontDisplay} மாற்றி`,
                    desc: `யூனிகோட் முதல் ${fontDisplay} மாற்றி. Convert Tamil Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, tamil font converter`
                };
            case 'kn':
                return {
                    title: `ಯುನಿಕೋಡ್‌ನಿಂದ ${fontDisplay} ಪರಿವರ್ತಕ | Unicode to ${fontDisplay.toLowerCase()} converter free online`,
                    h1: `ಯುನಿಕೋಡ್‌ನಿಂದ ${fontDisplay} ಪರಿವರ್ತಕ`,
                    desc: `ಯುನಿಕೋಡ್‌ನಿಂದ ${fontDisplay} ಪರಿವರ್ತಕ. Convert Kannada Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, kannada font converter`
                };
            case 'ml':
                return {
                    title: `യൂണിക്കോഡ് ടു ${fontDisplay} കൺവെർട്ടർ | Unicode to ${fontDisplay.toLowerCase()} converter free online`,
                    h1: `യൂണിക്കോഡ് ടു ${fontDisplay} കൺവെർട്ടർ`,
                    desc: `യൂണിക്കോഡ് ടു ${fontDisplay} കൺവെർട്ടർ. Convert Malayalam Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, malayalam font converter`
                };
            case 'mr':
                return {
                    title: `युनिकोड ते ${fontDisplay} कन्व्हर्टर | Unicode to ${fontDisplay.toLowerCase()} converter free online`,
                    h1: `युनिकोड ते ${fontDisplay} कन्व्हर्टर`,
                    desc: `युनिकोड ते ${fontDisplay} कन्व्हर्टर. Convert Marathi Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, marathi font converter`
                };
            case 'gu':
                return {
                    title: `યુનિકોડ થી ${fontDisplay} કન્વર્ટર | Unicode to ${fontDisplay.toLowerCase()} converter free online`,
                    h1: `યુનિકોડ થી ${fontDisplay} કન્વર્ટર`,
                    desc: `યુનિકોડ થી ${fontDisplay} કન્વર્ટર. Convert Gujarati Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, gujarati font converter`
                };
            case 'en':
            default:
                return {
                    title: `Unicode to ${fontDisplay} converter online free`,
                    h1: `Unicode to ${fontDisplay} Converter`,
                    desc: `Convert Unicode text to ${fontDisplay} font format instantly for free.`,
                    keys: `unicode to ${fontDisplay.toLowerCase()} converter free online, font converter`
                };
        }
    };

    const routes: { params: { lang?: string, converter: string }, props: SeoProps }[] = [];
    
    const addRoute = (converter: string, script: string, format: string, formatStr: string, exactFontStr?: string) => {
        const seo = getSeoTexts(script, formatStr, exactFontStr);
        const route: any = {
            params: { converter },
            props: { script, format, exactFont: exactFontStr, ...seo }
        };
        if (!isEn) {
            route.params.lang = lang;
        }
        routes.push(route);
    };

    // Generic Converters
    addRoute('unicode-to-anu-converter', 'telugu', 'anu7', 'Anu 7.0 & 6.0');
    addRoute('unicode-to-anu-neo-converter', 'hindi', 'anuneo', 'Anu Neo');
    addRoute('unicode-to-kruti-dev-converter', 'hindi', 'krutidev', 'Kruti Dev');
    addRoute('unicode-to-shree-lipi-hindi-converter', 'hindi', 'shreelipi', 'Shree Lipi');
    addRoute('unicode-to-bamini-converter', 'tamil', 'bamini', 'Bamini');
    addRoute('unicode-to-shree-lipi-tamil-converter', 'tamil', 'shreelipitam', 'Shree Lipi Tamil');
    addRoute('unicode-to-nudi-converter', 'kannada', 'nudi', 'Nudi');
    addRoute('unicode-to-ism-ml-tt-converter', 'malayalam', 'ism', 'ISM / ML-TT');
    addRoute('unicode-to-shree-lipi-marathi-converter', 'marathi', 'shreelipimar', 'Shree Lipi Marathi');
    addRoute('unicode-to-hari-converter', 'gujarati', 'hari', 'Hari');

    // Telugu Anu Exact Fonts
    if (lang === 'en' || lang === 'te') {
        ALL_TELUGU_FONTS.forEach(font => {
            const fontNameEn = formatFontName(font.label);
            const transliterated = (TRANSLITERATIONS as any)?.te?.[font.label] || fontNameEn;
            const fontNameStr = lang === 'te' ? transliterated : fontNameEn;
            
            const slug = `unicode-to-${font.label.toLowerCase()}-converter`;
            addRoute(slug, 'telugu', 'anu7', 'Anu 7.0', fontNameStr);
        });
    }

    // Hindi Anu Neo Exact Fonts
    if (lang === 'en' || lang === 'hi') {
        HINDI_NEO_FONTS.forEach(font => {
            const fontNameEn = formatFontName(font.label);
            const transliterated = (TRANSLITERATIONS as any)?.hi?.[font.label] || fontNameEn;
            const fontNameStr = lang === 'hi' ? transliterated : fontNameEn;
            
            const slug = `unicode-to-${font.label.toLowerCase()}-converter`;
            addRoute(slug, 'hindi', 'anuneo', 'Anu Neo', fontNameStr);
        });
    }

    return routes;
}

export function getLocalizedRoutes() {
    let allRoutes: any[] = [];
    const langs = Object.keys(TRANSLATIONS).filter(l => l !== 'en') as Language[];
    
    langs.forEach(lang => {
        allRoutes = [...allRoutes, ...getBaseRoutes(lang)];
    });
    
    return allRoutes;
}

export function getEnglishRoutes() {
    return getBaseRoutes('en');
}
