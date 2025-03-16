// store/auth.ts
import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    isAuthenticated: false, // За замовчуванням користувач не авторизований
    user: null, // Додано для зберігання даних користувача
  }),
  actions: {
    login(userData: any) {
      this.isAuthenticated = true;
      this.user = userData; // Зберігаємо дані користувача
    },
    logout() {
      this.isAuthenticated = false;
      this.user = null; // Очищаємо дані користувача
    },
  },
});