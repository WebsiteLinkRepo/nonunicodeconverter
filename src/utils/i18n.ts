export type Language = 'en' | 'te' | 'hi' | 'ta' | 'ml';

export interface Translations {
  siteTitle: string;
  title: string;
  subtitle: string;
  metaTitle: string;
  metaDescription: string;
  h1: string;
  keywords: string;
  defaultFont: string;
  selectFontLabel: string;
  autoDetectNotice: string;
  cleanSpacesLabel: string;
  convertDigitsLabel: string;
  altRaaVatthuLabel: string;
  inputBoxHeader: string;
  outputBoxHeader: string;
  pasteBtn: string;
  clearBtn: string;
  downloadBtn: string;
  inputPlaceholder: string;
  outputPlaceholder: string;
  copyBtn: string;
  copiedBtn: string;
  charsLabel: string;
  unmappedNotice: string;
  footerText: string;
  installAppBtn: string;
  historyTitle: string;
  clearHistoryBtn: string;
  fonts: {
    anu6: string;
    anu7: string;
    bamini: string;
    malayalam: string;
    krutiDev: string;
    shreeLipi: string;
    appleTelugu: string;
  };
}

export const TRANSLATIONS: Record<Language, Translations> = {
  en: {
    siteTitle: "Unicode to Non-Unicode",
    title: "Unicode to Non-Unicode Converter",
    subtitle: "Convert Indic text (Telugu, Hindi, Tamil, Malayalam) to legacy font formats in 1 click.",
    metaTitle: "Unicode To Non Unicode Converter Telugu & Anu 7.0 | Anu Unicode Online",
    metaDescription: "Free online unicode to non unicode converter tool. Convert Telugu Unicode to Anu 7.0 & Anu Unicode, and Hindi to Kruti Dev fonts for Photoshop & InDesign.",
    h1: "Unicode To Non Unicode Converter",
    keywords: "unicode to non unicode, unicode to non unicode converter telugu, unicode to non unicode anu 7.0, anu unicode, unicode converter telugu, unicode to non unicode font, hindi unicode to non unicode converter, kruti dev 010 to unicode, mangal to kruti dev converter, unicode to bamini tamil converter, ism revathi malayalam converter, shree lipi telugu converter, indesign telugu font converter, photoshop telugu font converter, anu 6 to unicode converter",
    defaultFont: "anu6",
    selectFontLabel: "SELECT FONT:",
    autoDetectNotice: "Auto-detecting text format",
    cleanSpacesLabel: "Clean Linebreaks & Spaces",
    convertDigitsLabel: "Convert Digits (123 ↔ ౧౨౩)",
    altRaaVatthuLabel: "Alt Raa Vatthu (ర వత్తు)",
    inputBoxHeader: "UNICODE TEXT INPUT",
    outputBoxHeader: "NON-UNICODE OUTPUT",
    pasteBtn: "Paste Text",
    clearBtn: "Clear",
    downloadBtn: "Download .txt",
    inputPlaceholder: "Paste Unicode text here... (e.g. తెలుగు / हिंदी / தமிழ் / മലയാളം)",
    outputPlaceholder: "Converted legacy font text will appear here automatically...",
    copyBtn: "COPY OUTPUT",
    copiedBtn: "✓ COPIED!",
    charsLabel: "chars",
    unmappedNotice: "Notice: Unmapped Unicode characters detected.",
    footerText: "Unicode2NonUnicode • Instant & 100% Private (Runs locally in your browser)",
    installAppBtn: "Install Desktop App",
    historyTitle: "Recent Conversions",
    clearHistoryBtn: "Clear History",
    fonts: {
      anu6: "Anu 6 (Telugu)",
      anu7: "Anu 7 (Telugu)",
      bamini: "Bamini (Tamil)",
      malayalam: "ISM Revathi (Malayalam)",
      krutiDev: "Kruti Dev (Hindi)",
      shreeLipi: "Shree-Lipi",
      appleTelugu: "Apple Telugu"
    }
  },
  te: {
    siteTitle: "యూనికోడ్ టు నాన్-యూనికోడ్",
    title: "యూనికోడ్ నుండి నాన్-యూనికోడ్ కన్వర్టర్",
    subtitle: "1 క్లిక్‌లో యూనికోడ్ టెక్స్ట్‌ని నాన్-యూనికోడ్ ఫాంట్‌లకు (తెలుగు, హిందీ, తమిళం, మలయాళం) మార్చండి.",
    metaTitle: "యూనికోడ్ టు నాన్-యూనికోడ్ కన్వర్టర్ | అను 7.0 & అను 6 ఫాంట్స్",
    metaDescription: "ఉచిత ఆన్‌లైన్ తెలుగు యూనికోడ్ నుండి అను 7.0, అను 6, అను యూనికోడ్ మరియు శ్రీ-లిపి నాన్-యూనికోడ్ ఫాంట్ కన్వర్టర్. ఫోటోషాప్, ఇన్‌డిజైన్ కోసం వేగవంతమైన సాధనం.",
    h1: "యూనికోడ్ నుండి నాన్-యూనికోడ్ కన్వర్టర్ (తెలుగు అను 7.0 & అను 6)",
    keywords: "యూనికోడ్ టు నాన్-యూనికోడ్, తెలుగు యూనికోడ్ కన్వర్టర్, అను 7.0 కన్వర్టర్, అను 6 కన్వర్టర్, తెలుగు నాన్ యూనికోడ్ ఫాంట్లు, అను యూనికోడ్, శ్రీ-లిపి తెలుగు",
    defaultFont: "anu6",
    selectFontLabel: "ఫాంట్ ఎంచుకోండి:",
    autoDetectNotice: "టెక్స్ట్ ఆటో-డిటెక్ట్ అవుతోంది",
    cleanSpacesLabel: "అదనపు స్పేస్‌లు & లైన్‌బ్రేక్‌లు తొలగించు",
    convertDigitsLabel: "అంకెలు మార్చు (123 ↔ ౧౨౩)",
    altRaaVatthuLabel: "ఆల్టర్నేటివ్ ర వత్తు (ర వత్తు)",
    inputBoxHeader: "యూనికోడ్ ఇన్పుట్",
    outputBoxHeader: "నాన్-యూనికోడ్ అవుట్‌పుట్",
    pasteBtn: "పేస్ట్ చేయండి",
    clearBtn: "క్లియర్",
    downloadBtn: "డౌన్‌లోడ్ .txt",
    inputPlaceholder: "మీ టెక్స్ట్ ఇక్కడ పేస్ట్ చేయండి... (ఉదాహరణకు: తెలుగు / हिंदी / தமிழ் / മലയാളം)",
    outputPlaceholder: "మార్చిన ఫాంట్ టెక్స్ట్ ఇక్కడ ఆటోమేటిక్‌గా కనిపిస్తుంది...",
    copyBtn: "కాపీ చేయండి",
    copiedBtn: "✓ కాపీ అయింది!",
    charsLabel: "అక్షరాలు",
    unmappedNotice: "గమనిక: కొన్ని అక్షరాలు మార్చడం సాధ్యపడలేదు.",
    footerText: "యూనికోడ్2నాన్-యూనికోడ్ • 100% వేగవంతమైనది మరియు ప్రైవేట్ (మీ బ్రౌజర్‌లోనే పనిచేస్తుంది)",
    installAppBtn: "యాప్ ఇన్‌స్టాల్ చేయండి",
    historyTitle: "ఇటీవలి కన్వర్షన్లు",
    clearHistoryBtn: "చరిత్ర తొలగించు",
    fonts: {
      anu6: "అను 6 (తెలుగు)",
      anu7: "అను 7 (తెలుగు)",
      bamini: "బామిని (తమిళం)",
      malayalam: "రేవతి (మలయాళం)",
      krutiDev: "కృతి దేవ్ (హిందీ)",
      shreeLipi: "శ్రీ-లిపి",
      appleTelugu: "యాపిల్ తెలుగు"
    }
  },
  hi: {
    siteTitle: "यूनिकोड टू नॉन-यूनिकोड",
    title: "यूनिकोड टू नॉन-यूनिकोड कनवर्टर",
    subtitle: "1 क्लिक में पाठ्य को नॉन-यूनिकोड फॉन्ट (कृति देव, अनु, बामिनी, रेवती) में कन्वर्ट करें।",
    metaTitle: "यूनिकोड टू नॉन-यूनिकोड कनवर्टर | कृति देव 010 & श्री-लिपि",
    metaDescription: "निःशुल्क ऑनलाइन हिंदी यूनिकोड से कृति देव 010 (Kruti Dev) और श्री-लिपि (Shree-Lipi) नॉन-यूनिकोड फॉन्ट कनवर्टर। एडोब फोटोशॉप और इनडिजाइन के लिए सर्वश्रेष्ठ टूल।",
    h1: "यूनिकोड टू नॉन-यूनिकोड कनवर्टर (कृति देव & अनु)",
    keywords: "यूनिकोड टू नॉन-यूनिकोड, कृति देव 010 कनवर्टर, मंगल टू कृति देव, श्री लिपि कनवर्टर, हिंदी फॉन्ट कनवर्टर, नॉन यूनिकोड फॉन्ट",
    defaultFont: "kruti-dev",
    selectFontLabel: "फॉन्ट चुनें:",
    autoDetectNotice: "ऑटो-डिटेक्ट हो रहा है",
    cleanSpacesLabel: "अतिरिक्त स्पेस और लाइनब्रेक हटाएं",
    convertDigitsLabel: "अंक बदलें (123 ↔ ౧౨౩)",
    altRaaVatthuLabel: "ऑल्टरनेटिव र वत्तू (ర వత్తు)",
    inputBoxHeader: "यूनिकोड इनपुट",
    outputBoxHeader: "नॉन-यूनिकोड आउटपुट",
    pasteBtn: "पेस्ट करें",
    clearBtn: "क्लियर",
    downloadBtn: "डाउनलोड .txt",
    inputPlaceholder: "अपना यूनिकोड टेक्स्ट यहाँ पेस्ट करें... (उदा. कृति देव / अनु / तमिल)",
    outputPlaceholder: "परिवर्तित टेक्स्ट यहाँ दिखाई देगा...",
    copyBtn: "कॉपी करें",
    copiedBtn: "✓ कॉपी हो गया!",
    charsLabel: "वर्ण",
    unmappedNotice: "सूचना: कुछ वर्ण परिवर्तित नहीं हो सके।",
    footerText: "यूनिकोड2नॉनयूनिकोड • 100% सुरक्षित और तेज़",
    installAppBtn: "ऐप इंस्टॉल करें",
    historyTitle: "हाल के रूपांतरण",
    clearHistoryBtn: "इतिहास साफ़ करें",
    fonts: {
      anu6: "अनु 6 (तेलुगु)",
      anu7: "अनु 7 (तेलुगु)",
      bamini: "बामिनी (तमिल)",
      malayalam: "रेवती (मलयालम)",
      krutiDev: "कृति देव (हिंदी)",
      shreeLipi: "श्री-लिपि",
      appleTelugu: "ऐप्पल तेलुगु"
    }
  },
  ta: {
    siteTitle: "யூனிகோட் டூ நான்-யூனிகோட்",
    title: "யூனிகோட் முதல் நான்-யூனிகோட் மாற்றி",
    subtitle: "1 கிளிக்கில் உரையை நான்-யூனிகோட் பாமினி, அனு, ரேவதி எழுத்துருக்களாக மாற்றவும்.",
    metaTitle: "யூனிகோட் முதல் நான்-யூனிகோட் மாற்றி | பாமினி தமிழ் எழுத்துரு",
    metaDescription: "இலவச ஆன்லைன் தமிழ் யூனிகோட் முதல் பாமினி (Bamini) நான்-யூனிகோட் தமிழ் எழுத்துரு மாற்றி. போட்டோஷாப் மற்றும் இன்டிசைன் பயன்பாட்டிற்கு மிகவும் ஏற்றது.",
    h1: "யூனிகோட் முதல் நான்-யூனிகோட் தமிழ் மாற்றி (பாமினி)",
    keywords: "யூனிகோட் டூ நான்-யூனிகோட், பாமினி தமிழ் எழுத்துரு மாற்றி, தமிழ் யூனிகோட் கன்வெர்ட்டர், நான் யூனிகோட் பாமினி",
    defaultFont: "bamini-tamil",
    selectFontLabel: "எழுத்துருவைத் தேர்ந்தெடுக்கவும்:",
    autoDetectNotice: "தானாக கண்டறியப்படுகிறது",
    cleanSpacesLabel: "கூடுதல் இடைவெளிகளை நீக்கு",
    convertDigitsLabel: "எண்களை மாற்றுக (123)",
    altRaaVatthuLabel: "ஆல்டர்னேடிவ் ர வத்து",
    inputBoxHeader: "யூனிகோட் உள்ளீடு",
    outputBoxHeader: "நான்-யூனிகோட் வெளியீடு",
    pasteBtn: "ஒட்டு",
    clearBtn: "அழி",
    downloadBtn: "பதிவிறக்கம் .txt",
    inputPlaceholder: "யூனிகோட் உரையை இங்கே ஒட்டவும்... (எ.கா. தமிழ் / తెలుగు / हिंदी)",
    outputPlaceholder: "மாற்றப்பட்ட உரை இங்கே தோன்றும்...",
    copyBtn: "பிரதியை நகலெடு",
    copiedBtn: "✓ நகலெடுக்கப்பட்டது!",
    charsLabel: "எழுத்துக்கள்",
    unmappedNotice: "அறிவிப்பு: சில எழுத்துக்கள் மாற்றப்படவில்லை.",
    footerText: "யூனிகோட்2நான்-யூனிகோட் • வேகமானது & 100% பாதுகாப்பானது",
    installAppBtn: "செயலியை நிறுவு",
    historyTitle: "சமீபத்திய மாற்றங்கள்",
    clearHistoryBtn: "வரலாற்றை அழி",
    fonts: {
      anu6: "அனு 6 (தெலுங்கு)",
      anu7: "அனு 7 (தெலுங்கு)",
      bamini: "பாமினி (தமிழ்)",
      malayalam: "ரேவதி (மலையாளம்)",
      krutiDev: "கிருதி தேவ் (ஹிந்தி)",
      shreeLipi: "ஸ்ரீ-லிபி",
      appleTelugu: "ஆப்பிள் தெலுங்கு"
    }
  },
  ml: {
    siteTitle: "യൂണികോഡ് ടു നോൺ-യൂണികോഡ്",
    title: "യൂണികോഡ് നോൺ-യൂണികോഡ് മാറ്റുന്ന ഉപകരണം",
    subtitle: "ഒറ്റ ക്ലിക്കിൽ വാചകം നോൺ-യൂണികോഡ് ഫോണ്ടുകളിലേക്ക് മാറ്റുക.",
    metaTitle: "യൂണികോഡ് നോൺ-യൂണികോഡ് മാറ്റുന്ന ഉപകരണം | ISM രേവതി",
    metaDescription: "സൗജന്യ ഓൺലൈൻ മലയാളം യൂണികോഡ് മുതൽ ISM രേവതി (Revathi) നോൺ-യൂണികോഡ് ഫോണ്ട് മാറ്റുന്ന ഉപകരണം. ഇൻഡിസൈൻ, ഫോട്ടോഷോപ്പ് ആപ്പുകൾക്ക് അനുയോജ്യം.",
    h1: "യൂണികോഡ് നോൺ-യൂണികോഡ് മാറ്റുന്ന ഉപകരണം (മലയാളം)",
    keywords: "യൂണികോഡ് നോൺ-യൂണികോഡ്, രേവതി മലയാളം ഫോണ്ട്, ISM രേവതി കൺവെർട്ടർ, മലയാളം യൂണികോഡ് ഉപകരണം",
    defaultFont: "ism-malayalam",
    selectFontLabel: "ഫോണ്ട് തിരഞ്ഞെടുക്കുക:",
    autoDetectNotice: "ഓട്ടോ-ഡിറ്റക്ട് ചെയ്യുന്നു",
    cleanSpacesLabel: "അധിക സ്പേസുകൾ ഒഴിവാക്കുക",
    convertDigitsLabel: "അക്കങ്ങൾ മാറ്റുക (123)",
    altRaaVatthuLabel: "ആൾട്ടർനേറ്റീവ് ര വത്തു",
    inputBoxHeader: "യൂണികോഡ് ഇൻപുട്ട്",
    outputBoxHeader: "നോൺ-യൂണികോഡ് ഔട്ട്പുട്ട്",
    pasteBtn: "പേസ്റ്റ് ചെയ്യുക",
    clearBtn: "ക്ലിയർ",
    downloadBtn: "ഡൗൺലോഡ് .txt",
    inputPlaceholder: "യൂണികോഡ് ടെക്സ്റ്റ് ഇവിടെ പേസ്റ്റ് ചെയ്യുക...",
    outputPlaceholder: "മാറ്റിയ ടെക്സ്റ്റ് ഇവിടെ കാണാം...",
    copyBtn: "കോപ്പി ചെയ്യുക",
    copiedBtn: "✓ കോപ്പി ചെയ്തു!",
    charsLabel: "അക്ഷരങ്ങൾ",
    unmappedNotice: "ശ്രദ്ധിക്കുക: ചില അക്ഷരങ്ങൾ മാറ്റാനായില്ല.",
    footerText: "യൂണികോഡ്2നോൺയൂണികോഡ് • വേഗതയേറിയതും സുരക്ഷിതവും",
    installAppBtn: "ആപ്പ് ഇൻസ്റ്റാൾ ചെയ്യുക",
    historyTitle: "സമീപകാല മാറ്റങ്ങൾ",
    clearHistoryBtn: "ചരിത്രം മായ്ക്കുക",
    fonts: {
      anu6: "അനു 6 (തെലുഗു)",
      anu7: "അനു 7 (തെലുഗു)",
      bamini: "ബാമിനി (തമിഴ്)",
      malayalam: "രേവതി (മലയാളം)",
      krutiDev: "കൃതി ദേവ് (ഹിന്ദി)",
      shreeLipi: "ശ്രീ-ലിപി",
      appleTelugu: "ആപ്പിൾ തെലുഗു"
    }
  }
};
