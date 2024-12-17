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
              <BaseInput
                  v-model="registerForm.username"
                  :rules="[required, minLength(3)]"
                  @validation-error="onValidationError('username', $event)"
              />
            </div>
            <div class="mb-4">
              <label for="email" class="block text-gray-800 dark:text-gray-200"
                >Email</label
              >
              <BaseInput
                  v-model="registerForm.email"
                  :rules="[required, isEmail]"
                  type="email"
                  @validation-error="onValidationError('email', $event)"
              />
            </div>
            <div class="mb-4">
              <label
                for="password"
                class="block text-gray-800 dark:text-gray-200"
                >Пароль</label
              >
              <div class="relative">
                <BaseInput
                    v-model="registerForm.password"
                    :rules="[required, minLength(6)]"
                    type="password"
                    @validation-error="onValidationError('password', $event)"
                />
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
              <BaseInput
                  v-model="loginForm.email"
                  :rules="[required, isEmail]"
                  type="email"
                  @validation-error="onValidationError('email', $event)"
              />
            </div>
            <div class="mb-4">
              <label
                for="password"
                class="block text-gray-800 dark:text-gray-200"
                >Пароль</label
              >
              <div class="relative">
                <BaseInput
                    v-model="loginForm.password"
                    :rules="[required, minLength(6)]"
                    type="password"
                    @validation-error="onValidationError('password', $event)"
                />
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
import { ref, computed } from "vue";
import { useUserStore } from "../stores/authStore";
import BaseInput from "@/UI/BaseInput.vue";
import { required, minLength, isEmail } from "@/utils/validationRules";

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

const errors = ref({
  username: "",
  email: "",
  password: "",
});


// Обробник помилок
function onValidationError(field, message) {
  errors.value[field] = message;
}

// Перевірка валідності форми
const formValid = computed(() =>
    Object.values(errors.value).every((error) => !error)
);

const handleLogin = async () => {
  await useUserStore.login(loginForm.value);
};

const handleRegister = async () => {
  if (formValid.value) {
    await useUserStore.signUp(registerForm.value);
    activeTab.value = "email";
  }
};
</script>
