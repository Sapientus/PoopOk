import 'vue'

declare module 'vue' {
  interface ComponentCustomProperties {
    $t: (key: string, ...values: any[]) => string
    $i18n: {
      locale: string
      locales: { code: string; name: string }[]
    }
  }
}
