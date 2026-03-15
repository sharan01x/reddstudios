import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://redd.in',
  output: 'static',
  build: {
    assets: '_assets'
  }
});
