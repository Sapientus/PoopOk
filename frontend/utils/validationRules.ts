type ValidatorFn = (value: string) => true | string;

export const required =
  (t: (key: string) => string): ValidatorFn =>
  (value: string) =>
    value.trim() ? true : t("errorRequired");

export const minLength =
  (min: number, t: (key: string, args?: any) => string): ValidatorFn =>
  (value: string) =>
    value.length >= min ? true : t("errorMinLength", { min });

export const isEmail =
  (t: (key: string) => string): ValidatorFn =>
  (value: string) =>
    /\S+@\S+\.\S+/.test(value) ? true : t("errorEmail");

export const confirmPassword =
  (getPassword: () => string, t: (key: string) => string): ValidatorFn =>
  (value: string) =>
    value === getPassword() ? true : t("errorConfirmPassword");
