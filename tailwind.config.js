/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./songbird/templates/*.html",
    "./songbird/templates/**/*.html",
    "./templates/*.html",
    "./templates/**/*.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
