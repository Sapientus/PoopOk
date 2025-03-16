export function validateInput(value: string, rules: Array<(value: string) => true | string>): string {
  for (const rule of rules) {
    const result = rule(value);
    if (result !== true) {
      return result; // Перше повідомлення про помилку
    }
  }
  return ""; // Очищення помилки
}
