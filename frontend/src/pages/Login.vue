<template>
    <div
        class="flex justify-center h-full w-full items-center bg-white dark:bg-gray-900 bg-[url('./src/assets/bg_auth.svg')] bg-cover bg-top"
    >
        <div
            class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 max-w-md w-full"
        >
            <LoginForm />
            <p
                class="text-gray-800 dark:text-gray-100 mt-4 text-center text-sm"
            >
                {{ t("dontHaveAccount") }}
                <BaseLink to="/register">{{ t("registerHere") }}</BaseLink>
            </p>
        </div>
    </div>
</template>

<script setup>
import LoginForm from "../components/LoginForm.vue";
import BaseLink from "../UI/BaseLink.vue";

import { useI18n } from "vue-i18n";

// Використовуємо i18n
const { t } = useI18n();
</script>
