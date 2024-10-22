export default {
    install(app) {
      const savedTheme = JSON.parse(localStorage.getItem('isDark'));
      if (savedTheme) {
        document.documentElement.classList.toggle('dark', savedTheme);
      }
    }
  };