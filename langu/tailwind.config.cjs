/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{svelte,js,ts}'],
  daisyui: {
    themes: [
      {
        mytheme: {
          "primary": "#5eead4",
          "secondary": "#c4b5fd",
          "accent": "#535bf2",
          "neutral": "#9ca3af",
          "base-100": "#FFFFFF",
          "info": "#3ABFF8",
          "success": "#22c55e",
          "warning": "#f97316",
          "error": "#dc2626",
        },
      },
      "dark"
    ],
  },
  plugins: [require('daisyui')],
}
