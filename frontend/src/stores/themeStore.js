import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useThemeStore = defineStore('theme', () => {
  const isDark = ref(false);

  // Дія для перемикання теми
  const toggleTheme = () => {
    isDark.value = !isDark.value;
    // Зберігаємо тему в localStorage
    localStorage.setItem('isDark', isDark.value);
    updateDOM();
  };

  // Дія для завантаження теми
  const loadTheme = () => {
    const savedTheme =  JSON.parse(localStorage.getItem('isDark'));
    isDark.value = savedTheme;
  };

  // Оновлення DOM для темної теми
  const updateDOM = () => {
    if (isDark.value) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  };

  return {
    isDark,
    toggleTheme,
    loadTheme,
  };
});
