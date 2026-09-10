import { en } from './locales/en';
import { te } from './locales/te';
import { hi } from './locales/hi';
import { ta } from './locales/ta';
import { kn } from './locales/kn';
import { ml } from './locales/ml';
import { mr } from './locales/mr';
import { gu } from './locales/gu';

export type Language = 'en' | 'te' | 'hi' | 'ta' | 'kn' | 'ml' | 'mr' | 'gu';

export type Translations = typeof en;

export const TRANSLATIONS: Record<Language, Translations> = {
  en,
  te,
  hi,
  ta,
  kn,
  ml,
  mr,
  gu
};
