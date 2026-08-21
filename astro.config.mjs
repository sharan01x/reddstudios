import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://redd.in',
  output: 'static',

  build: {
    assets: '_assets'
  },

  integrations: [sitemap()]
});