<template>
  <div class="auth-container">
    <h1 class="text-gray-800 text-3xl font-bold mb-4 dark:text-gray-100">
      {{ isLogin ? t("login") : t("registration") }}
    </h1>
    <component :is="isLogin ? LoginForm : RegisterForm" />
    <p class="text-gray-800 dark:text-gray-100 mt-4 text-center text-sm">
      {{ isLogin ? t("dontHaveAccount") : t("alreadyHaveAccount") }}
      <button
        @click="toggleForm"
        class="text-blue-500 dark:text-blue-400 hover:underline transition ml-1"
      >
        {{ isLogin ? t("registerHere") : t("loginHere") }}
      </button>
    </p>
  </div>
</template>

<script setup>
import LoginForm from "./LoginForm.vue";
import RegisterForm from "./RegisterForm.vue";
import { ref } from "vue";
import { useI18n } from "vue-i18n";

// Використовуємо i18n
const { t } = useI18n();

const isLogin = ref(true);

const toggleForm = () => {
  isLogin.value = !isLogin.value;
};
</script>
