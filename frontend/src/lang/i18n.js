import { watch } from "vue";
import { createI18n } from "vue-i18n";
import translationUA from "./translationUA.json";
import translationEN from "./translationEN.json";

// Визначаємо мову за замовчуванням
const defaultLanguage = localStorage.getItem("language") || "uk";

// Додаємо переклади для різних мов
const messages = {
  en: translationEN,
  ua: translationUA,
};

// Створюємо екземпляр i18n
const i18n = createI18n({
  legacy: false, // Для використання Composition API
  locale: defaultLanguage, // Мова за замовчуванням
  fallbackLocale: "en", // Резервна мова
  messages, // Об'єкт з перекладами
  watchLocale: true,
});

// Відслідковуємо зміну мови
watch(i18n.global.locale, (newLocale) => {
  localStorage.setItem("language", newLocale);
});

export const t = i18n.global.t;
export default i18n;
