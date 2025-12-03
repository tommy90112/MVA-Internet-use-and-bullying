/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // 馬卡龍色系 - 柔和淺色調
        primary: {
          50: '#fafbfc',
          100: '#f0f4f5',
          200: '#dfe8eb',
          300: '#b8d4dc',  // 馬卡龍藍
          400: '#a8c9ce',  // 柔和青色
          500: '#8FAFCC',  // 淺藍色
          600: '#78ABAF',  // 青綠色
          700: '#5D8696',  // 深青色
          800: '#4a6b78',
          900: '#3d5862',
        },
        accent: {
          cream: '#FAF8F5',    // 奶油白
          light: '#E8E6E3',    // 淺灰
          warm: '#E5CDB0',     // 淺奶茶色
          peach: '#F5DCD0',    // 蜜桃粉
          mint: '#C5DED6',     // 薄荷綠
          lavender: '#D4D0E8', // 薰衣草紫
          sky: '#C8DDF0',      // 天空藍
        },
        dark: {
          50: '#f8f9fa',
          100: '#e9ecef',
          200: '#dee2e6',
          300: '#ced4da',
          400: '#6c757d',
          500: '#495057',
          600: '#343a40',
          700: '#2d3238',
          800: '#1f2428',
          900: '#161a1d',
        }
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.6s ease-out',
        'slide-left': 'slideLeft 0.6s ease-out',
        'pulse-slow': 'pulse 3s infinite',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(30px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideLeft: {
          '0%': { opacity: '0', transform: 'translateX(30px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-20px)' },
        }
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'hero-pattern': 'linear-gradient(135deg, #FAF8F5 0%, #E8E6E3 100%)',
      }
    },
  },
  plugins: [],
}
