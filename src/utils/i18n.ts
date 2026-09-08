export type Language = 'en' | 'te';

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
    priyanka: string;
    anupama: string;
    subhalekha: string;
    bapu: string;
    ramana: string;
    gowthami: string;
  };
}

export const TRANSLATIONS: Record<Language, Translations> = {
  en: {
    siteTitle: "NonUnicodeConverter.com",
    title: "Unicode to Non-Unicode Converter",
    subtitle: "Convert Indian languages Unicode text to legacy font formats instantly.",
    metaTitle: "NonUnicodeConverter.com | Indian Legacy Fonts",
    metaDescription: "Convert Unicode to legacy font layouts like Anu Script, Kruti Dev, Bamini, and Shree-Lipi. Free online converter for Photoshop, PageMaker, and InDesign.",
    h1: "Unicode to Non-Unicode Converter",
    keywords: "unicode to non unicode, kruti dev converter, anu script converter, bamini converter, hindi unicode to non unicode, telugu unicode to anu, tamil unicode to bamini, shree lipi converter, indesign font converter, photoshop font converter",
    defaultFont: "anu7",
    selectFontLabel: "FONT STYLE:",
    autoDetectNotice: "Auto-detecting text format",
    cleanSpacesLabel: "Clean Linebreaks & Spaces",
    convertDigitsLabel: "Convert Digits (123 ↔ ౧౨౩)",
    altRaaVatthuLabel: "Alt Raa Vatthu (ర వత్తు)",
    inputBoxHeader: "UNICODE INPUT",
    outputBoxHeader: "LEGACY OUTPUT",
    pasteBtn: "Paste Text",
    clearBtn: "Clear",
    downloadBtn: "Download .txt",
    inputPlaceholder: "Paste Unicode text here... (e.g. नमस्ते, నమస్కారం, வணக்கம்)",
    outputPlaceholder: "Converted legacy text will appear here automatically...",
    copyBtn: "COPY OUTPUT",
    copiedBtn: "✓ COPIED!",
    charsLabel: "chars",
    unmappedNotice: "Notice: Unmapped characters detected.",
    footerText: "NonUnicodeConverter.com • Instant & 100% Private (Runs locally in your browser)",
    installAppBtn: "Install Desktop App",
    historyTitle: "Recent Conversions",
    clearHistoryBtn: "Clear History",
    fonts: {
      priyanka: "Anu Priyanka",
      anupama: "Anu Anupama",
      subhalekha: "Anu Subhalekha",
      bapu: "Anu Bapu Script",
      ramana: "Anu Ramana Script",
      gowthami: "Anu Gowthami"
    }
  },
  te: {
    siteTitle: "NonUnicodeConverter.com",
    title: "యూనికోడ్ నుండి నాన్-యూనికోడ్ ఫాంట్ కన్వర్టర్",
    subtitle: "భారతీయ భాషల యూనికోడ్ టెక్స్ట్‌ను లెగసీ ఫాంట్‌లలోకి 1 క్లిక్‌తో మార్చండి.",
    metaTitle: "NonUnicodeConverter.com ఆన్‌లైన్ | లెగసీ ఫాంట్స్",
    metaDescription: "యూనికోడ్ నుండి అను స్క్రిప్ట్, కృతి దేవ్, బామిని వంటి ఫాంట్ లేఅవుట్ కన్వర్టర్. ఫోటోషాప్, పేజ్‌మేకర్ మరియు ఇన్‌డిజైన్ కోసం ఉచిత సాధనం.",
    h1: "యూనికోడ్ టు నాన్-యూనికోడ్ కన్వర్టర్",
    keywords: "యూనికోడ్ టు నాన్-యూనికోడ్, తెలుగు యూనికోడ్ కన్వర్టర్, అను 7.0 కన్వర్టర్, కృతి దేవ్ కన్వర్టర్, బామిని కన్వర్టర్, హిందీ నాన్ యూనికోడ్, అను యూనికోడ్",
    defaultFont: "anu7",
    selectFontLabel: "ఫాంట్ శైలి:",
    autoDetectNotice: "టెక్స్ట్ ఆటో-డిటెక్ట్ అవుతోంది",
    cleanSpacesLabel: "అదనపు స్పేస్‌లు & లైన్‌బ్రేక్‌లు తొలగించు",
    convertDigitsLabel: "అంకెలు మార్చు (123 ↔ ౧౨౩)",
    altRaaVatthuLabel: "ఆల్టర్నేటివ్ ర వత్తు (ర వత్తు)",
    inputBoxHeader: "యూనికోడ్ ఇన్‌పుట్",
    outputBoxHeader: "లెగసీ అవుట్‌పుట్",
    pasteBtn: "పేస్ట్ చేయండి",
    clearBtn: "క్లియర్",
    downloadBtn: "డౌన్‌లోడ్ .txt",
    inputPlaceholder: "మీ యూనికోడ్ టెక్స్ట్ ఇక్కడ పేస్ట్ చేయండి... (ఉదాహరణ: నమస్కారం, नमस्ते, வணக்கம்)",
    outputPlaceholder: "మార్చిన టెక్స్ట్ ఇక్కడ ఆటోమేటిక్‌గా కనిపిస్తుంది...",
    copyBtn: "కాపీ చేయండి",
    copiedBtn: "✓ కాపీ అయింది!",
    charsLabel: "అక్షరాలు",
    unmappedNotice: "గమనిక: కొన్ని అక్షరాలు మార్చడం సాధ్యపడలేదు.",
    footerText: "NonUnicodeConverter.com • 100% వేగవంతమైనది మరియు ప్రైవేట్ (మీ బ్రౌజర్‌లోనే పనిచేస్తుంది)",
    installAppBtn: "యాప్ ఇన్‌స్టాల్ చేయండి",
    historyTitle: "ఇటీవలి కన్వర్షన్లు",
    clearHistoryBtn: "చరిత్ర తొలగించు",
    fonts: {
      priyanka: "అను ప్రియాంక",
      anupama: "అను అనుపమ",
      subhalekha: "అను శుభలేఖ",
      bapu: "అను బాపు స్క్రిప్ట్",
      ramana: "అను రమణ స్క్రిప్ట్",
      gowthami: "అను గౌతమి"
    }
  }
};
