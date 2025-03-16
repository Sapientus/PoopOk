import { defineNuxtConfig } from "nuxt/config";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  components: true,
  nitro: {
    routeRules: {
      "/_nuxt/**": { headers: { "cache-control": "no-store, max-age=0" } },
    },
  },
  compatibilityDate: "2024-11-01",
  devtools: { enabled: false },
  modules: [
    "@nuxtjs/i18n",
    "@nuxtjs/seo",
    "@vueuse/nuxt",
    "@pinia/nuxt",
    "@nuxt/fonts",
    "@nuxt/icon",
    "@nuxt/image",
  ],
  i18n: {
    vueI18n: "./i18n.config.ts",
    langDir: "./lang/", // ВАЖЛИВО: переконайся, що папка `lang/` існує
    lazy: true,
    restructureDir: false,
    strategy: "no_prefix",
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: "i18n_redirected",
      redirectOn: "root",
    },
    locales: [
      { code: "en", name: "English", file: "en-US.js" },
      { code: "uk", name: "Українська", file: "uk-UA.js" },
    ],
  },
  fonts: {
    families: [{ name: "Montserrat", provider: "google" }],
  },
  image: {
    provider: 'ipx',
    domains: ['xsgames.co']
  },
  icon: {
    serverBundle: {
      collections: ["fluent"], // <!--- this
    },
    customCollections: [
      // Changed from object to array
      {
        prefix: "my-icon",
        dir: "./assets/my-icons",
      },
    ],
  },
  css: ["~/assets/scss/main.scss"],
  vite: {
    server: {
      watch: {
        usePolling: true,
      },
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `
            @use "~/assets/scss/_variables.scss" as *;
            @use "~/assets/scss/_mixins.scss" as *;
           `,
        },
      },
    },
  },
  app: {
    head: {
      script: [
        {
          innerHTML: `(function() {
            const theme = localStorage.getItem('theme') || 'system';
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            const isDark = theme === 'dark' || (theme === 'system' && prefersDark);
            if (isDark) {
              document.documentElement.classList.add('dark');
            } else {
              document.documentElement.classList.remove('dark');
            }
          })();`,
          type: "text/javascript",
          tagPosition: "head",
        },
      ],
      __dangerouslyDisableSanitizers: ["script"],
    } as any,
  },
});
