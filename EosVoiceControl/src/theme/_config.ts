import type { ThemeConfiguration } from '@/theme/types/config';

import { DarkTheme, DefaultTheme } from '@react-navigation/native';

export const enum Variant {
  DARK = 'dark',
}

const colorsDefault = {
  orange: '#EC9F00',
  EOSBlack: '#050505',
  EOSGray: '#141414',
  gray100: '#000000',
  gray200: '#BABABA',
  gray400: '#969696',
  gray50: '#EFEFEF',
  gray800: '#E0E0E0',
  purple100: '#252732',
  purple50: '#1B1A23',
  purple500: '#A6A4F0',
  red500: '#C13333',
  skeleton: '#303030',
} as const;

const sizes = [6, 8, 12, 16, 24, 32, 40, 80] as const;

export const config = {
  backgrounds: colorsDefault,
  borders: {
    colors: colorsDefault,
    radius: [4, 16],
    widths: [1, 2],
  },
  colors: colorsDefault,
  fonts: {
    colors: colorsDefault,
    sizes,
  },
  gutters: sizes,
  navigationColors: {
    ...DefaultTheme.colors,
    background: colorsDefault.EOSGray,
    card: colorsDefault.EOSBlack,
  },
  variants: {
  },
} as const satisfies ThemeConfiguration;
