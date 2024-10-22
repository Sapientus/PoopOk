<template>
    <div class="bg-gray-100 dark:bg-gray-900 w-full h-full p-4">
        <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg max-w-md mx-auto flex flex-col">
            <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-200">Налаштування профілю</h1>

            <div class="mt-4">
                <label for="profilePic" class="block text-gray-800 dark:text-gray-200">Фото профілю</label>
                <input type="file" id="profilePic" @change="handleProfilePicChange"
                    class="mt-1 block w-full text-gray-800 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
            </div>

            <div class="mt-4">
                <label for="username" class="block text-gray-800 dark:text-gray-200">Ім'я користувача</label>
                <input type="text" id="username" v-model="username"
                    class="mt-1 block w-full text-gray-800 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
            </div>

            <div class="mt-4">
                <label for="email" class="block text-gray-800 dark:text-gray-200">Email</label>
                <input type="email" id="email" v-model="email"
                    class="mt-1 block w-full text-gray-800 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
            </div>

            <div class="mt-4">
                <label class="block text-gray-800 dark:text-gray-200">Отримувати пуш-повідомлення?</label>
                <input type="checkbox" id="pushNotifications" v-model="pushNotifications" class="mt-1" />
            </div>

            <div class="mt-4">
                <label for="defaultTheme" class="block text-gray-800 dark:text-gray-200">Тема за замовчуванням</label>
                <ThemeSwitcher />
            </div>

            <div class="mt-4">
                <label for="language" class="block text-gray-800 dark:text-gray-200">Мова</label>
                <LanguageSwitcher />
            </div>

            <button @click="saveSettings"
                class="mt-6 w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
                Зберегти налаштування
            </button>
        </div>
    </div>

</template>

<script setup>
import { ref } from 'vue';
import ThemeSwitcher from '../components/ThemeSwitcher.vue';
import LanguageSwitcher from '../components/LanguageSwitcher.vue';

const username = ref('');
const email = ref('');
const pushNotifications = ref(false);
const defaultTheme = ref('light');
const language = ref('uk');

const handleProfilePicChange = (event) => {
    const file = event.target.files[0];
    if (file) {
        // Логіка для завантаження фото профілю
        console.log('Selected file:', file);
    }
};

const saveSettings = () => {
    // Логіка для збереження налаштувань
    console.log('Settings saved:', {
        username: username.value,
        email: email.value,
        pushNotifications: pushNotifications.value,
        defaultTheme: defaultTheme.value,
        language: language.value,
    });
};
</script>

<style scoped>
/* Додаткові стилі, якщо потрібно */
</style>