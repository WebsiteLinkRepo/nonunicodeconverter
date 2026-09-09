export interface FAQItem {
  question: string;
  answer: string;
}

export const faqData: FAQItem[] = [
  // Group 1: Basic Definitions & Fundamentals
  {
    question: "What does this converter do?",
    answer: "It bridges the gap between modern internet text (Unicode) and traditional print publishing software. It automatically translates standard text into the exact ASCII keystrokes required by legacy fonts."
  },
  {
    question: "What is unicode?",
    answer: "Unicode is the universal character encoding standard that allows computers, smartphones, and web browsers to consistently represent and exchange text in all world languages across different devices and platforms."
  },
  {
    question: "What is Unicode used for?",
    answer: "Unicode is used to ensure that text appears identical across all operating systems, web browsers, and devices, regardless of the language or region being used."
  },
  {
    question: "What is non-Unicode?",
    answer: "Non-Unicode refers to legacy 8-bit ASCII fonts (like Anu Script, Kruti Dev, or Bamini) created before a universal text standard existed. They map regional language characters to standard English keyboard keystrokes, requiring specific fonts to display correctly."
  },
  {
    question: "How do I write Unicode?",
    answer: "You can type Unicode text using standard system keyboards (like Windows Indic Input, iOS/Android language keypads, or Google Input Tools) or simply copy it from any website, WhatsApp, or standard document."
  },
  {
    question: "Can you convert Unicode to text?",
    answer: "Yes. While Unicode itself is standard digital text, our tool converts it into specific legacy non-Unicode font encodings (text mapped for traditional desktop publishing software) and vice versa."
  },
  
  // Group 2: Core Conversion Features & How To Use
  {
    question: "How to convert Unicode to non-Unicode ?",
    answer: "Select your desired output font (such as Anu Script, Kruti Dev, or Bamini), paste your standard Unicode text into the input box, and the tool will instantly translate it into the corresponding legacy font keystrokes."
  },
  {
    question: "How to convert non-Unicode to Unicode?",
    answer: "Paste your legacy non-Unicode text into our converter's input box. The tool automatically and instantly converts it into clean, standard web-ready Unicode."
  },
  {
    question: "Can I convert back to Unicode?",
    answer: "Yes, our tool is a robust two-way converter. You can paste legacy text (non-Unicode) into the converter and translate it back to clean, standard web-ready Unicode."
  },
  {
    question: "Can I copy and download the converted output?",
    answer: "Yes, you can instantly copy the converted text to your clipboard with a single click. There is no need to download files, making the workflow fast and seamless."
  },
  {
    question: "Is this converter really free?",
    answer: "Absolutely! Our tool is 100% free to use. There are no hidden fees, no registration requirements, and no daily usage limits."
  },

  // Group 3: Quality, Accuracy, & Technical Info
  {
    question: "How accurate is the conversion?",
    answer: "Our converter is highly accurate. Instead of basic find-and-replace, it uses an advanced rule-based syllable compiler that correctly processes complex consonants, vowel modifiers, and half-letters."
  },
  {
    question: "Can we convert Unicode to non-Unicode without losing data?",
    answer: "Yes, our advanced compiler ensures that complex syllables, specific vowel modifiers, and rare conjuncts are preserved perfectly during conversion without any data loss."
  },
  {
    question: "Will the tool fix spacing issues in old text?",
    answer: "Yes, our converter includes smart line-break cleaning, zero-width character stripping, and quote normalization to prevent corrupted glyphs and spacing issues common when pasting into Adobe InDesign and Photoshop."
  },
  {
    question: "Why does the output look weird on my device?",
    answer: "The converted output consists of ASCII keystrokes that only look correct when you apply the specific legacy font (like Anu 7.0 or Kruti Dev) in your design software. In a standard web browser or text editor, it will appear as English gibberish."
  },

  // Group 4: Supported Languages & Fonts (Broad)
  {
    question: "is it for all langauge?",
    answer: "It is designed specifically for major Indian regional languages (Indic scripts). We provide accurate conversions for Telugu, Hindi, Tamil, Malayalam, Kannada, Marathi, and Gujarati."
  },
  {
    question: "Does it support other languages?",
    answer: "Yes! Beyond Telugu, our converter fully supports Hindi, Marathi, Tamil, Malayalam, Kannada, and Gujarati using fonts like Kruti Dev, Bamini, Shree Lipi, ML-TT, Nudi, and more."
  },

  // Group 5: Telugu Specific (Anu, Telugu Unicode)
  {
    question: "What is the best Unicode to non-Unicode converter for Telugu?",
    answer: "Unicode2NonUnicode.com is the best online app. It requires no installation, offers instant real-time conversion without data loss, and processes all your text locally and privately within your web browser."
  },
  {
    question: "What are the Unicode characters for Telugu?",
    answer: "Telugu Unicode occupies the U+0C00 to U+0C7F code block. It comprehensively covers all Telugu vowels (అ-అః), consonants (క-హ), vowel signs (matras), conjunct markers (vattus), numbers, and symbols."
  },
  {
    question: "Can I type Telugu without installing any software?",
    answer: "Yes, you can use any standard keyboard or input tool to type Unicode Telugu on the web, then use our free web converter to generate legacy font text for your projects without installing dedicated desktop typing software."
  },
  {
    question: "How can I convert Unicode text to Anu fonts?",
    answer: "Select Anu 6 or Anu 7 from the font tabs, then paste your Telugu Unicode text. Our engine instantly translates the text into legacy Anu font ASCII keystrokes suitable for Adobe Photoshop, PageMaker, and InDesign."
  },
  {
    question: "How do I convert Unicode to Anu?",
    answer: "Choose Anu 6 or Anu 7 from our Telugu font options, paste your Unicode text, and instantly copy the Anu-compatible output for use in your DTP software."
  },
  {
    question: "How do I convert Anu to Unicode?",
    answer: "Paste your legacy Anu script text into the converter, select the appropriate Anu version, and it will automatically translate it back into standard Telugu Unicode text."
  },
  {
    question: "What is the difference between Anu 6 and Anu 7?",
    answer: "Both are legacy ASCII fonts for Telugu, but they use slightly different keyboard mappings and glyph assignments. Our tool provides precise rendering options for both versions to perfectly match your installed font files."
  },
  {
    question: "Do I need Anu Script Manager installed to use this converter?",
    answer: "No, you do not need Anu Script Manager installed on your computer. Our web tool handles the conversion logic entirely in your browser. You only need the actual Anu font files installed to view the final text in your software."
  },

  // Group 6: Hindi, Marathi, and Devanagari Specific (Kruti Dev, Mangal, Shree Dev)
  {
    question: "Can I convert Unicode to Kruti Dev 010?",
    answer: "Yes, you can easily convert Hindi Unicode text to Kruti Dev 010. Simply select the Kruti Dev option in the Hindi tab, paste your Unicode text, and copy the instantly generated result."
  },
  {
    question: "Does this converter support Chanakya and Mangal Hindi text?",
    answer: "Yes. You can paste Mangal (which is standard Hindi Unicode) into the input box and convert it seamlessly into legacy fonts like Kruti Dev, Shree Dev, or Chanakya."
  },
  {
    question: "Mangal से Krutidev में कन्वर्ट करते समय कोई गड़बड़ी होगी?",
    answer: "नहीं, हमारा कनवर्टर मंगल (यूनिकोड) से कृतिदेव में बेहद सटीक और बिना किसी डेटा लॉस के रूपांतरण करता है। सभी मात्राएं, आधे अक्षर और संयुक्त अक्षर सही ढंग से मैप किए जाते हैं।"
  },
  {
    question: "Unicode to SHREE DEV 0714 font converter",
    answer: "We provide dedicated support for SHREE DEV 0714. Simply select the Hindi/Marathi tab, choose Shree Dev 0714 from the options, and paste your Unicode text for instant, accurate conversion."
  },

  // Group 7: Other Languages (Kannada, Malayalam, Tamil / Shree Lipi)
  {
    question: "Can I convert Unicode Kannada back to Nudi or Baraha ASCII?",
    answer: "Yes, we fully support Unicode to Nudi and Baraha conversions, maintaining perfect syllable integrity for Kannada publishing workflows."
  },
  {
    question: "Can I use this Nudi to Unicode converter online for free?",
    answer: "Yes, the Nudi to Unicode and Unicode to Nudi conversion features are completely free, run locally in your browser, and require no account registration."
  },
  {
    question: "What are the steps required to convert Unicode Malayalam text to ML TT Font using the online converter mentioned?",
    answer: "1. Select the Malayalam language tab. 2. Choose ML-TT (or ISM Revathi) as the output font. 3. Paste your Malayalam Unicode text. 4. Copy the generated ML-TT output and paste it directly into your design software."
  },
  {
    question: "Is the Shree Lipi font converter free to use?",
    answer: "Yes, converting to and from Shree Lipi fonts (for Tamil, Telugu, Marathi, Hindi, etc.) is 100% free on our platform without any limitations."
  }
];
