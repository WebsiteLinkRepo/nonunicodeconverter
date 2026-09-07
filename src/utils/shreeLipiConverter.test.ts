import { describe, it, expect } from 'vitest';
import { unicodeToShreeLipi } from './src/utils/shreeLipiConverter';

describe('Shree-Lipi Converter Devanagari Tests', () => {
    it('should correctly convert words containing ma without rendering gaps', () => {
        expect(unicodeToShreeLipi("भस्म")).toBe("^ñ_");
        expect(unicodeToShreeLipi("मंत्र")).toBe("_§Ì");
        expect(unicodeToShreeLipi("मुक्त")).toBe("_wº$");
    });

    it('should convert standard consonants, conjuncts and matras', () => {
        expect(unicodeToShreeLipi("कमल")).toBe("H$_b");
        expect(unicodeToShreeLipi("नमस्ते")).toBe("Z_ñVo");
        expect(unicodeToShreeLipi("माता")).toBe("_mVm");
        expect(unicodeToShreeLipi("मित्र")).toBe("{_Ì");
    });
});
