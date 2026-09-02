import { describe, it, expect } from 'vitest';
import { unicodeToShreeLipi } from './src/utils/shreeLipiConverter';

describe('Shree-Lipi Converter Devanagari Tests', () => {
    it('should correctly convert words containing ma without rendering gaps', () => {
        expect(unicodeToShreeLipi("भस्म")).toBe("^ñ‘");
        expect(unicodeToShreeLipi("मंत्र")).toBe("‘§Ì");
        expect(unicodeToShreeLipi("मुक्त")).toBe("‘wº$");
    });

    it('should convert standard consonants, conjuncts and matras', () => {
        expect(unicodeToShreeLipi("कमल")).toBe("H$‘b");
        expect(unicodeToShreeLipi("नमस्ते")).toBe("Z‘ñVo");
        expect(unicodeToShreeLipi("माता")).toBe("‘mVm");
        expect(unicodeToShreeLipi("मित्र")).toBe("{‘Ì");
    });
});
