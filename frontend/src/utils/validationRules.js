export const required = (value) =>
    value ? true : "Це поле є обов'язковим.";

export const minLength = (min) => (value) =>
    value.length >= min ? true : `Мінімальна кількість символів: ${min}.`;

export const isEmail = (value) =>
    /\S+@\S+\.\S+/.test(value) ? true : "Введіть коректний email.";
