import { defineStore } from "pinia";
import { ref, computed } from 'vue';
import AuthService from '../services/authService';

export const useUserStore = defineStore(
  "auth",
  () => {
    const user = ref(null);
    const isAuthenticated = ref(!!localStorage.getItem('access_token'));

    function setUser(userData) {
      user.value = userData;
    }

    function setAuthenticated(authenticated) {
      isAuthenticated.value = authenticated;
    }

    async function login(credentials) {
      if (!credentials || !credentials.email || !credentials.password) {
        throw new Error("Invalid credentials. Email and password are required.");
      }

      try {
        const response = await AuthService.login(credentials);
        if (!response.user) {
          throw new Error("Invalid response from the API. Token and user are required.");
        }

        setUser(response.user); // Отриманий користувач після логіну
        setAuthenticated(true);

      } catch (error) {
        console.error("Error logging in:", error);
        throw error;
      }
    }

    function logout() {
      AuthService.logout();
      user.value = null;
      isAuthenticated.value = false;
    }

    function refreshToken() {
      AuthService.refreshToken();
    }

    return {
      user,
      isAuthenticated,
      setUser,
      login,
      logout,
      refreshToken
    };
  },
  {
    persist: {
      key: "user-store", // назва ключа в localStorage
      paths: ["auth", "isAuthenticated"], // поля, які треба зберігати
      storage: 'localStorage',
    },
  },
);
