import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";
import tailwindcss from 'tailwindcss';
import autoprefixer from 'autoprefixer';
import postcssImport from 'postcss-import';
import { resolve } from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Ваш сервер
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/api/, ''), // Видаляє /api перед запитом до сервера
      },
    },
  },
  build: {
    target: "esnext",
    sourcemap: true,
    chunkSizeWarningLimit: 500, // Попередження для великих чанків
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'), // Шлях до вашої директорії src
    },
  },
  css: {
    postcss: {
      plugins: [
        postcssImport(),
        tailwindcss(),
        autoprefixer(),
      ],
    },
  },
});
