<template>
  <div
    class="flex justify-center h-full w-full items-center bg-white dark:bg-gray-900"
  >
    <div class="w-1/2 h-full overflow-hidden">
      <img
        src="../assets/main.jpg"
        alt="Main"
        class="w-full h-full object-cover"
      />
    </div>
    <div class="w-1/2 flex flex-col justify-center items-center">
      <div
        class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 max-w-md w-full"
      >
        <div v-if="activeTab === 'register'">
          <h2
            class="text-center text-2xl font-bold text-gray-800 dark:text-gray-200"
          >
            Реєстрація
          </h2>
          <form @submit.prevent="handleRegister">
            <div class="mb-4">
              <label
                for="username"
                class="block text-gray-800 dark:text-gray-200"
                >Ім'я користувача</label
              >
              <input
                type="text"
                id="username"
                v-model="registerForm.username"
                required
                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div class="mb-4">
              <label for="email" class="block text-gray-800 dark:text-gray-200"
                >Email</label
              >
              <input
                type="email"
                id="email"
                v-model="registerForm.email"
                required
                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div class="mb-4">
              <label
                for="password"
                class="block text-gray-800 dark:text-gray-200"
                >Пароль</label
              >
              <div class="relative">
                <input
                  :type="showPassword ? 'text' : 'password'"
                  id="password"
                  v-model="registerForm.password"
                  required
                  class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button
                  type="button"
                  @click="togglePasswordVisibility"
                  class="absolute inset-y-0 right-0 top-1/2 -translate-y-2/4 pr-3 flex items-center text-sm leading-5"
                >
                  <svg
                    v-if="showPassword"
                    class="h-5 w-5 text-gray-500"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.477 0 8.268 2.943 9.542 7-.274.823-.68 1.597-1.196 2.3M15 12a3 3 0 01-6 0m6 0a3 3 0 01-6 0m6 0c0 1.657-1.343 3-3 3s-3-1.343-3-3m6 0c0-1.657-1.343-3-3-3s-3 1.343-3 3"
                    />
                  </svg>
                  <svg
                    v-else
                    class="h-5 w-5 text-gray-500"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13.875 18.825A10.05 10.05 0 0112 19c-4.477 0-8.268-2.943-9.542-7a10.05 10.05 0 011.196-2.3m1.196-2.3A10.05 10.05 0 0112 5c4.477 0 8.268 2.943 9.542 7-.274.823-.68 1.597-1.196 2.3M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M3 3l18 18"
                    />
                  </svg>
                </button>
              </div>
            </div>
            <button
              type="submit"
              class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Зареєструватися
            </button>
          </form>
        </div>

        <div v-if="activeTab === 'email'">
          <h3
            class="text-center text-2xl font-bold text-gray-800 dark:text-gray-200"
          >
            Дякуємо за реєстрацію, будь ласка перейдіть на свою пошту та
            підтвердіть свій email, щоб мати змогу увійти у ваш профайл
          </h3>
          <p class="mt-4 text-center text-gray-600 dark:text-gray-400">
            <span
              @click="activeTab = 'login'"
              class="text-blue-500 font-semibold cursor-pointer"
              >Увійти?</span
            >
          </p>
        </div>

        <div v-if="activeTab === 'login'">
          <h2
            class="text-center text-2xl font-bold text-gray-800 dark:text-gray-200"
          >
            Увійти
          </h2>
          <form @submit.prevent="handleLogin">
            <div class="mb-4">
              <label for="email" class="block text-gray-800 dark:text-gray-200"
                >Email</label
              >
              <input
                type="email"
                id="email"
                v-model="loginForm.username"
                required
                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div class="mb-4">
              <label
                for="password"
                class="block text-gray-800 dark:text-gray-200"
                >Пароль</label
              >
              <div class="relative">
                <input
                  :type="showPassword ? 'text' : 'password'"
                  id="password"
                  v-model="loginForm.password"
                  required
                  class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
                <button
                  type="button"
                  @click="togglePasswordVisibility"
                  class="absolute inset-y-0 right-0 top-1/2 -translate-y-2/4 pr-3 flex items-center text-sm leading-5"
                >
                  <svg
                    v-if="showPassword"
                    class="h-5 w-5 text-gray-500"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.477 0 8.268 2.943 9.542 7-.274.823-.68 1.597-1.196 2.3M15 12a3 3 0 01-6 0m6 0a3 3 0 01-6 0m6 0c0 1.657-1.343 3-3 3s-3-1.343-3-3m6 0c0-1.657-1.343-3-3-3s-3 1.343-3 3"
                    />
                  </svg>
                  <svg
                    v-else
                    class="h-5 w-5 text-gray-500"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M13.875 18.825A10.05 10.05 0 0112 19c-4.477 0-8.268-2.943-9.542-7a10.05 10.05 0 011.196-2.3m1.196-2.3A10.05 10.05 0 0112 5c4.477 0 8.268 2.943 9.542 7-.274.823-.68 1.597-1.196 2.3M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M3 3l18 18"
                    />
                  </svg>
                </button>
              </div>
            </div>
            <button
              type="submit"
              class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Увійти
            </button>
          </form>
        </div>
        <div v-if="activeTab !== 'email'">
          <p
            class="mt-4 text-center text-gray-600 dark:text-gray-400"
            v-if="activeTab === 'register'"
          >
            Вже маєте аккаунт?
            <span
              @click="activeTab = 'login'"
              class="text-blue-500 font-semibold cursor-pointer"
              >Увійти</span
            >
          </p>
          <p class="mt-4 text-center text-gray-600 dark:text-gray-400" v-else>
            Немає аккаунту?
            <span
              @click="activeTab = 'register'"
              class="text-blue-500 font-semibold cursor-pointer"
              >Зареєструватися</span
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "../stores/authStore";

const activeTab = ref("register"); // Вкладки логін/реєстрація

const loginForm = ref({
  username: "",
  password: "",
});

const registerForm = ref({
  username: "",
  email: "",
  password: "",
});

const showPassword = ref(false);
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
};

const handleLogin = async () => {
  await useUserStore.login(loginForm.value);
};

const handleRegister = async () => {
  await useUserStore.signUp(registerForm.value);
  activeTab.value = "email";
};
</script>
