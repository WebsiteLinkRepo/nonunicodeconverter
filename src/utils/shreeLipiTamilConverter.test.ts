import { describe, it, expect } from 'vitest';
import { unicodeToShreeLipiTamil, shreeLipiTamilToUnicode } from './shreeLipiTamilConverter';

describe('Shree-Lipi Tamil Converter', () => {
  describe('Forward Conversion (Unicode -> Shree-Lipi)', () => {
    it('converts independent vowels correctly', () => {
      expect(unicodeToShreeLipiTamil('அ')).toBe('A');
      expect(unicodeToShreeLipiTamil('ஆ')).toBe('B');
      expect(unicodeToShreeLipiTamil('இ')).toBe('C');
      expect(unicodeToShreeLipiTamil('ஈ')).toBe('D');
      expect(unicodeToShreeLipiTamil('உ')).toBe('E');
      expect(unicodeToShreeLipiTamil('ஊ')).toBe('F');
      expect(unicodeToShreeLipiTamil('எ')).toBe('G');
      expect(unicodeToShreeLipiTamil('ஏ')).toBe('H');
      expect(unicodeToShreeLipiTamil('ஐ')).toBe('I');
      expect(unicodeToShreeLipiTamil('ஒ')).toBe('J');
      expect(unicodeToShreeLipiTamil('ஓ')).toBe('K');
      expect(unicodeToShreeLipiTamil('ஔ')).toBe('JÍ');
    });

    it('converts base consonants with pulli (mei ezhuthu) correctly', () => {
      expect(unicodeToShreeLipiTamil('க்')).toBe('U');
      expect(unicodeToShreeLipiTamil('ங்')).toBe('[');
      expect(unicodeToShreeLipiTamil('ச்')).toBe('a');
      expect(unicodeToShreeLipiTamil('ஞ்')).toBe('g');
      expect(unicodeToShreeLipiTamil('ட்')).toBe('m');
      expect(unicodeToShreeLipiTamil('ண்')).toBe('s');
      expect(unicodeToShreeLipiTamil('த்')).toBe('z');
      expect(unicodeToShreeLipiTamil('ந்')).toBe('¢');
      expect(unicodeToShreeLipiTamil('ப்')).toBe('¨');
      expect(unicodeToShreeLipiTamil('ம்')).toBe('®');
      expect(unicodeToShreeLipiTamil('ய்')).toBe('´');
    });

    it('converts uyirmei combinations (ka series) correctly', () => {
      expect(unicodeToShreeLipiTamil('க் க கா கி கீ கு கூ கெ கே கை கொ கோ கௌ'))
        .toBe('U P Põ Q R S T öP ÷P øP öPõ ÷Põ öPÍ');
    });

    it('converts complex sentences and paragraphs with 100% fidelity', () => {
      const input = "தமிழ் மொழி உலகின் மிகத் தொன்மையான செம்மொழிகளில் ஒன்றாகும். இரண்டாயிரத்திற்கும் மேற்பட்ட வரலாற்றுப் பெருமை கொண்ட சங்க இலக்கியங்கள், திருக்குறள், சிலப்பதிகாரம், மணிமேகலை ஆகியவை தமிழரின் பண்பாட்டையும் அறிவையும் பறைசாற்றுகின்றன.";
      const expected = "uªÌ ö©õÈ E»Qß ªPz öuõßø©¯õÚ ö\\®ö©õÈPÎÀ JßÓõS®. Cµshõ°µzvØS® ÷©Ø£mh Áµ»õØÖ¨ ö£¸ø© öPõsh \\[P C»UQ¯[PÒ, v¸USÓÒ, ]»¨£vPõµ®, ©o÷©Pø» BQ¯øÁ uªÇ›ß £s£õmøh²® AÔøÁ²® £øÓ\\õØÖQßÓÚ.";
      expect(unicodeToShreeLipiTamil(input)).toBe(expected);
    });
  });

  describe('Reverse Conversion (Shree-Lipi -> Unicode)', () => {
    it('converts independent vowels correctly', () => {
      expect(shreeLipiTamilToUnicode('A')).toBe('அ');
      expect(shreeLipiTamilToUnicode('B')).toBe('ஆ');
      expect(shreeLipiTamilToUnicode('C')).toBe('இ');
      expect(shreeLipiTamilToUnicode('D')).toBe('ஈ');
      expect(shreeLipiTamilToUnicode('E')).toBe('உ');
      expect(shreeLipiTamilToUnicode('F')).toBe('ஊ');
      expect(shreeLipiTamilToUnicode('G')).toBe('எ');
      expect(shreeLipiTamilToUnicode('H')).toBe('ஏ');
      expect(shreeLipiTamilToUnicode('I')).toBe('ஐ');
      expect(shreeLipiTamilToUnicode('J')).toBe('ஒ');
      expect(shreeLipiTamilToUnicode('K')).toBe('ஓ');
    });

    it('converts base consonants correctly', () => {
      expect(shreeLipiTamilToUnicode('U')).toBe('க்');
      expect(shreeLipiTamilToUnicode('a')).toBe('ச்');
      expect(shreeLipiTamilToUnicode('m')).toBe('ட்');
      expect(shreeLipiTamilToUnicode('z')).toBe('த்');
      expect(shreeLipiTamilToUnicode('¨')).toBe('ப்');
      expect(shreeLipiTamilToUnicode('®')).toBe('ம்');
    });

    it('converts complex sentences correctly', () => {
      const input = "¦µm]Pµ©õÚ PÂøuPÒ uªÇºPÎß ÷u\\£Uvø¯²® Âkuø» uõPzøu²® ÂÈ¨£øh¯a ö\\´uÚ.";
      const expected = "புரட்சிகரமான கவிதைகள் தமிழர்களின் தேசபக்தியையும் விடுதலை தாகத்தையும் விழிப்படையச் செய்தன.";
      expect(shreeLipiTamilToUnicode(input)).toBe(expected);
    });
  });
});
