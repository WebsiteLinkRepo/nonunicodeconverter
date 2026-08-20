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
    siteTitle: "Unicode to Non-Unicode",
    title: "Unicode to Non-Unicode Converter",
    subtitle: "Convert Telugu Unicode text to legacy Anu Script font formats instantly.",
    metaTitle: "Unicode to Anu 7.0 Converter Online | Legacy Telugu Font Converter",
    metaDescription: "Convert Telugu Unicode to legacy Anu Script 7.0 font layout. Free online converter for Photoshop, PageMaker, and InDesign DTP typesetting.",
    h1: "Unicode to Non-Unicode Converter",
    keywords: "unicode to non unicode, unicode to non unicode converter telugu, unicode to non unicode anu 7.0, anu unicode, unicode converter telugu, unicode to non unicode font, indesign telugu font converter, photoshop telugu font converter, anu script 7 telugu converter, priyanka telugu font converter, anupama telugu font converter",
    defaultFont: "anu7",
    selectFontLabel: "FONT STYLE:",
    autoDetectNotice: "Auto-detecting text format",
    cleanSpacesLabel: "Clean Linebreaks & Spaces",
    convertDigitsLabel: "Convert Digits (123 ↔ ౧౨౩)",
    altRaaVatthuLabel: "Alt Raa Vatthu (ర వత్తు)",
    inputBoxHeader: "TELUGU UNICODE INPUT",
    outputBoxHeader: "ANU LEGACY OUTPUT",
    pasteBtn: "Paste Text",
    clearBtn: "Clear",
    downloadBtn: "Download .txt",
    inputPlaceholder: "Paste Telugu Unicode text here... (ఉదాహరణ: తెలుగు నా ప్రాణము)",
    outputPlaceholder: "Converted legacy Anu 7.0 text will appear here automatically...",
    copyBtn: "COPY OUTPUT",
    copiedBtn: "✓ COPIED!",
    charsLabel: "chars",
    unmappedNotice: "Notice: Unmapped characters detected.",
    footerText: "Unicode2Anu7 • Instant & 100% Private (Runs locally in your browser)",
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
    siteTitle: "యూనికోడ్ టు అను 7.0 కన్వర్టర్",
    title: "యూనికోడ్ నుండి అను 7.0 తెలుగు ఫాంట్ కన్వర్టర్",
    subtitle: "తెలుగు యూనికోడ్ టెక్స్ట్‌ను అను స్క్రిప్ట్ 7.0 లెగసీ ఫాంట్‌లలోకి 1 క్లిక్‌తో మార్చండి.",
    metaTitle: "యూనికోడ్ నుండి అను 7.0 కన్వర్టర్ ఆన్‌లైన్ | తెలుగు లెగసీ ఫాంట్స్",
    metaDescription: "తెలుగు యూనికోడ్ నుండి అను స్క్రిప్ట్ 7.0 ఫాంట్ లేఅవుట్ కన్వర్టర్. ఫోటోషాప్, పేజ్‌మేకర్ మరియు ఇన్‌డిజైన్ డిటిపి కంపోజింగ్ కోసం ఉపయోగకరమైన ఉచిత సాధనం.",
    h1: "తెలుగు యూనికోడ్ నుండి అను 7.0 కన్వర్టర్",
    keywords: "యూనికోడ్ టు నాన్-యూనికోడ్, తెలుగు యూనికోడ్ కన్వర్టర్, అను 7.0 కన్వర్టర్, తెలుగు నాన్ యూనికోడ్ ఫాంట్లు, అను యూనికోడ్, ప్రియాంక తెలుగు ఫాంట్ కన్వర్టర్",
    defaultFont: "anu7",
    selectFontLabel: "ఫాంట్ శైలి:",
    autoDetectNotice: "టెక్స్ట్ ఆటో-డిటెక్ట్ అవుతోంది",
    cleanSpacesLabel: "అదనపు స్పేస్‌లు & లైన్‌బ్రేక్‌లు తొలగించు",
    convertDigitsLabel: "అంకెలు మార్చు (123 ↔ ౧౨౩)",
    altRaaVatthuLabel: "ఆల్టర్నేటివ్ ర వత్తు (ర వత్తు)",
    inputBoxHeader: "తెలుగు యూనికోడ్ ఇన్‌పుట్",
    outputBoxHeader: "అను లెగసీ అవుట్‌పుట్",
    pasteBtn: "పేస్ట్ చేయండి",
    clearBtn: "క్లియర్",
    downloadBtn: "డౌన్‌లోడ్ .txt",
    inputPlaceholder: "మీ తెలుగు యూనికోడ్ టెక్స్ట్ ఇక్కడ పేస్ట్ చేయండి... (ఉదాహరణ: తెలుగు నా మాతృభాష)",
    outputPlaceholder: "మార్చిన అను 7.0 టెక్స్ట్ ఇక్కడ ఆటోమేటిక్‌గా కనిపిస్తుంది...",
    copyBtn: "కాపీ చేయండి",
    copiedBtn: "✓ కాపీ అయింది!",
    charsLabel: "అక్షరాలు",
    unmappedNotice: "గమనిక: కొన్ని అక్షరాలు మార్చడం సాధ్యపడలేదు.",
    footerText: "యూనికోడ్2అను7 • 100% వేగవంతమైనది మరియు ప్రైవేట్ (మీ బ్రౌజర్‌లోనే పనిచేస్తుంది)",
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
