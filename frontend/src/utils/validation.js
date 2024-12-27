export function validateInput(value, rules) {
  for (const rule of rules) {
    const result = rule(value);
    if (result !== true) {
      return result; // Перше повідомлення про помилку
    }
  }
  return ""; // Очищення помилки
}
