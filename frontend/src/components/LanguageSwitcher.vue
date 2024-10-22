<template>
    <div class="flex items-center">
        <select v-model="locale"
            class="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-500 text-gray-900 dark:text-gray-100 p-2">>
            <option v-for="lang in languageOptions" :key="lang.value" :value="lang.value" class="bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">{{ lang.label }}</option>
        </select>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';

// Використовуємо i18n
const { t, locale } = useI18n();

// Опції для випадаючого списку
const languageOptions = [
    { label: `${t('ukraine')}`, value: 'ua' },
    { label: `${t('english')}`, value: 'en' },
];


</script>