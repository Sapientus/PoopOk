/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: 'class',
  plugins: [],
  postcss: {
    plugins: [
      require('postcss-import'),
      require('tailwindcss'),
      require('autoprefixer'),
    ]
  },
};
