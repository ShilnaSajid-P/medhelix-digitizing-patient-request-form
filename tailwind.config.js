/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './medhelix/templates/*.html',
    
  ],

 
  theme: {
    extend: {},
  },
  plugins: [

    require('@tailwindcss/forms'),

  ],
}

