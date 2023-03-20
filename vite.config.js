import {resolve} from 'path';
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'

module.exports = {
  plugins: [
    vue(),
    vuetify({ styles: 'sass' }),
  ],
  root: resolve('./assets'),
  base: '/static/',
  server: {
    host: 'localhost',
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.vue'],
  },
  build: {
    outDir: resolve('./assets/dist'),
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    sourcemap: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./assets/js/main.js'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};