import { defineStore } from 'pinia';

type Theme = 'light' | 'dark' | 'system';

export const useThemeStore = defineStore('theme', {
  state: () => ({
    theme: 'light' as Theme
  }),
  actions: {
    initTheme() {
      const savedTheme = localStorage.getItem('theme') as Theme | null;
      if (savedTheme) {
        this.setTheme(savedTheme);
      } else {
        this.setTheme('system');
      }
    },
    setTheme(theme: Theme) {
      this.theme = theme;
      localStorage.setItem('theme', theme);
      this.applyTheme(theme);
    },
    applyTheme(theme: Theme) {
      const root = document.documentElement;

      if (theme === 'system') {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        root.classList.toggle('dark', prefersDark);
      } else {
        root.classList.toggle('dark', theme === 'dark');
      }
    }
  }
});
