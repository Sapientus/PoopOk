import { t } from "@/lang/i18n";

export const required = (value) => (value ? true : t("errorRequired"));

export const minLength = (min) => (value) =>
  value.length >= min ? true : t("errorMinLength", { min });

export const isEmail = (value) =>
  /\S+@\S+\.\S+/.test(value) ? true : t("errorEmail");

export const confirmPassword = (getPassword) => (value) => {
  const password = getPassword(); // Отримуємо актуальний пароль
  return value === password ? true : t("errorConfirmPassword");
};
