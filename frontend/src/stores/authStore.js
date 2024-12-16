import { defineStore } from "pinia";
import { ref, computed } from "vue";
import AuthService from "../services/authService";

export const useUserStore = defineStore(
  "auth",
  () => {
    const user = ref(null);
    const isAuthenticated = ref(!!localStorage.getItem("access_token"));

    function setUser(userData) {
      user.value = userData;
    }

    function setAuthenticated(authenticated) {
      isAuthenticated.value = authenticated;
    }

    async function login(credentials) {
      if (!credentials || !credentials.username || !credentials.password) {
        throw new Error(
          "Invalid credentials. Email and password are required.",
        );
      }

      try {
        const response = await AuthService.logIn(credentials);
        if (!response) {
          throw new Error(
            "Invalid response from the API. Token and user are required.",
          );
        }

        setUser(response.data); // Отриманий користувач після логіну
        setAuthenticated(true);
      } catch (error) {
        console.error("Error logging in:", error);
        throw error;
      }
    }

    function logout() {
      AuthService.logOut();
      setUser(null);
      setAuthenticated(false);
    }

    function refreshToken() {
      AuthService.refreshToken();
    }

    function signUp(credentials) {
      if (
        !credentials ||
        !credentials.username ||
        !credentials.password ||
        !credentials.email
      ) {
        throw new Error(
          "Invalid credentials. Email and password are required.",
        );
      }

      try {
        const response = AuthService.signUp(credentials);
        if (!response) {
          throw new Error(
            "Invalid response from the API. Token and user are required.",
          );
        }
      } catch (error) {
        console.error("Error signing up:", error);
        throw error;
      }
    }

    return {
      user,
      isAuthenticated,
      login,
      refreshToken,
      signUp,
    };
  },
  {
    persist: {
      key: "user-store", // назва ключа в localStorage
      paths: ["auth", "isAuthenticated"], // поля, які треба зберігати
      storage: "localStorage",
    },
  },
);
