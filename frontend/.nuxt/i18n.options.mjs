
// @ts-nocheck


export const localeCodes =  [
  "en",
  "uk"
]

export const localeLoaders = {
  "en": [{ key: "../lang/en-US.js", load: () => import("../lang/en-US.js" /* webpackChunkName: "locale__Users_ttt_WebstormProjects_PoopOk_frontend_lang_en_US_js" */), cache: true }],
  "uk": [{ key: "../lang/uk-UA.js", load: () => import("../lang/uk-UA.js" /* webpackChunkName: "locale__Users_ttt_WebstormProjects_PoopOk_frontend_lang_uk_UA_js" */), cache: true }]
}

export const vueI18nConfigs = [
  () => import("../i18n.config.ts?hash=bffaebcb&config=1" /* webpackChunkName: "__i18n_config_ts_bffaebcb" */)
]

export const nuxtI18nOptions = {
  "restructureDir": false,
  "experimental": {
    "localeDetector": "",
    "switchLocalePathLinkSSR": false,
    "autoImportTranslationFunctions": false,
    "typedPages": true,
    "typedOptionsAndMessages": false,
    "generatedLocaleFilePathFormat": "absolute",
    "alternateLinkCanonicalQueries": false
  },
  "bundle": {
    "compositionOnly": true,
    "runtimeOnly": false,
    "fullInstall": true,
    "dropMessageCompiler": false,
    "optimizeTranslationDirective": true
  },
  "compilation": {
    "jit": true,
    "strictMessage": true,
    "escapeHtml": false
  },
  "customBlocks": {
    "defaultSFCLang": "json",
    "globalSFCScope": false
  },
  "vueI18n": "./i18n.config.ts",
  "locales": [
    {
      "code": "en",
      "name": "English",
      "files": [
        "/Users/ttt/WebstormProjects/PoopOk/frontend/lang/en-US.js"
      ]
    },
    {
      "code": "uk",
      "name": "Українська",
      "files": [
        "/Users/ttt/WebstormProjects/PoopOk/frontend/lang/uk-UA.js"
      ]
    }
  ],
  "defaultLocale": "",
  "defaultDirection": "ltr",
  "routesNameSeparator": "___",
  "trailingSlash": false,
  "defaultLocaleRouteNameSuffix": "default",
  "strategy": "no_prefix",
  "lazy": true,
  "langDir": "./lang/",
  "detectBrowserLanguage": {
    "alwaysRedirect": false,
    "cookieCrossOrigin": false,
    "cookieDomain": null,
    "cookieKey": "i18n_redirected",
    "cookieSecure": false,
    "fallbackLocale": "",
    "redirectOn": "root",
    "useCookie": true
  },
  "differentDomains": false,
  "baseUrl": "",
  "customRoutes": "page",
  "pages": {},
  "skipSettingLocaleOnNavigate": false,
  "types": "composition",
  "debug": false,
  "parallelPlugin": false,
  "multiDomainLocales": false,
  "i18nModules": []
}

export const normalizedLocales = [
  {
    "code": "en",
    "name": "English",
    "files": [
      {
        "path": "/Users/ttt/WebstormProjects/PoopOk/frontend/lang/en-US.js"
      }
    ]
  },
  {
    "code": "uk",
    "name": "Українська",
    "files": [
      {
        "path": "/Users/ttt/WebstormProjects/PoopOk/frontend/lang/uk-UA.js"
      }
    ]
  }
]

export const NUXT_I18N_MODULE_ID = "@nuxtjs/i18n"
export const parallelPlugin = false
export const isSSG = false
export const hasPages = true

export const DEFAULT_DYNAMIC_PARAMS_KEY = "nuxtI18nInternal"
export const DEFAULT_COOKIE_KEY = "i18n_redirected"
export const SWITCH_LOCALE_PATH_LINK_IDENTIFIER = "nuxt-i18n-slp"
