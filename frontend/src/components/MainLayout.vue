<template>
    <div class="w-full h-full flex flex-col">
        <header class="w-full bg-white dark:bg-gray-800 shadow-md py-4 fixed top-0">
            <div class="container mx-auto flex justify-between items-center px-4">
                <!-- Логотип -->
                <div class="text-2xl font-bold text-gray-800 dark:text-gray-200">
                    <router-link to="/">MySocial</router-link>
                </div>

                <!-- Навігаційні посилання -->
                <nav class="hidden md:flex space-x-6">
                    <router-link to="/"
                        class="text-gray-800 dark:text-gray-200 hover:text-blue-500">Профіль</router-link>
                    <router-link to="/tape"
                        class="text-gray-800 dark:text-gray-200 hover:text-blue-500">Стрічка</router-link>
                    <router-link to="/chat"
                        class="text-gray-800 dark:text-gray-200 hover:text-blue-500">Чат</router-link>
                    <router-link to="/about" class="text-gray-800 dark:text-gray-200 hover:text-blue-500">Про
                        проект</router-link>
                    <router-link to="/contact"
                        class="text-gray-800 dark:text-gray-200 hover:text-blue-500">Контакти</router-link>
                </nav>

                <!-- Профіль з випадаючим меню -->
                <div class="relative">
                    <button @click="toggleDropdown" class="flex items-center space-x-2 focus:outline-none">
                        <img src="https://placehold.co/50x50" alt="User Avatar"
                            class="w-10 h-10 rounded-full object-cover" />
                    </button>

                    <!-- Випадаюче меню -->
                    <transition name="fade">
                        <div v-if="dropdownOpen"
                            class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg py-2">
                            <router-link to="/profile"
                                class="block px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Профіль</router-link>
                            <router-link to="/settings"
                                class="block px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Налаштування</router-link>
                            <button @click="logout"
                                class="block w-full text-left px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">
                                Вийти
                            </button>
                        </div>
                    </transition>
                </div>

                <!-- Мобільне меню (приховане на великих екранах) -->
                <div class="md:hidden">
                    <button @click="toggleMobileMenu" class="text-gray-800 dark:text-gray-200 focus:outline-none">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                            stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16m-7 6h7" />
                        </svg>
                    </button>

                    <transition name="fade">
                        <nav v-if="mobileMenuOpen"
                            class="absolute top-16 left-0 w-full bg-white dark:bg-gray-800 shadow-md">
                            <router-link to="/profile"
                                class="block px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Профіль</router-link>
                            <router-link to="/feed"
                                class="block px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Стрічка</router-link>
                            <router-link to="/chat"
                                class="block px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Чат</router-link>
                            <router-link to="/about"
                                class="block px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Про
                                проект</router-link>
                            <router-link to="/contacts"
                                class="block px-4 py-2 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700">Контакти</router-link>
                        </nav>
                    </transition>
                </div>
            </div>
        </header>
        <main class="pt-[72px] h-full">
            <router-view />
        </main>
        <footer>© 2024 Мій Додаток</footer>
    </div>
</template>

<script setup>
import ThemeSwitcher from "./ThemeSwitcher.vue";
import LanguageSwitcher from "./LanguageSwitcher.vue";
import { ref } from 'vue';

const dropdownOpen = ref(false);
const mobileMenuOpen = ref(false);

const toggleDropdown = () => {
    dropdownOpen.value = !dropdownOpen.value;
};

const toggleMobileMenu = () => {
    mobileMenuOpen.value = !mobileMenuOpen.value;
};

const logout = () => {
    // Додайте логіку для виходу з облікового запису
    console.log('Вихід з облікового запису');
};
</script>

<style scoped>
/* Стилі для плавного відкриття випадаючого меню */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>