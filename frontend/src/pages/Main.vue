<template>
    <div class="flex justify-center h-full w-full items-center bg-white dark:bg-gray-900">
        <div class="w-1/2 h-full overflow-hidden">
            <img src="../assets/main.jpg" alt="Main" class="w-full h-full object-cover">
        </div>
        <div class="w-1/2 flex flex-col justify-center items-center">
            <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 max-w-md w-full">
                <div v-if="activeTab === 'register'">
                    <h2 class="text-center text-2xl font-bold text-gray-800 dark:text-gray-200">Реєстрація</h2>
                    <form @submit.prevent="register">
                        <div class="mb-4">
                            <label for="username" class="block text-gray-800 dark:text-gray-200">Ім'я
                                користувача</label>
                            <input type="text" id="username" v-model="username" required
                                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
                        </div>
                        <div class="mb-4">
                            <label for="email" class="block text-gray-800 dark:text-gray-200">Email</label>
                            <input type="email" id="email" v-model="email" required
                                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
                        </div>
                        <div class="mb-4">
                            <label for="password" class="block text-gray-800 dark:text-gray-200">Пароль</label>
                            <input type="password" id="password" v-model="password" required
                                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
                        </div>
                        <button type="submit"
                            class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
                            Зареєструватися
                        </button>
                    </form>
                </div>

                <div v-else>
                    <h2 class="text-center text-2xl font-bold text-gray-800 dark:text-gray-200">Увійти</h2>
                    <form @submit.prevent="login">
                        <div class="mb-4">
                            <label for="email" class="block text-gray-800 dark:text-gray-200">Email</label>
                            <input type="email" id="email" v-model="email" required
                                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
                        </div>
                        <div class="mb-4">
                            <label for="password" class="block text-gray-800 dark:text-gray-200">Пароль</label>
                            <input type="password" id="password" v-model="password" required
                                class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
                        </div>
                        <button type="submit"
                            class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
                            Увійти
                        </button>
                    </form>
                </div>

                <p class="mt-4 text-center text-gray-600 dark:text-gray-400" v-if="activeTab === 'register'">
                    Вже маєте аккаунт? <span @click="activeTab = 'login'"
                        class="text-blue-500 font-semibold cursor-pointer">Увійти</span>
                </p>
                <p class="mt-4 text-center text-gray-600 dark:text-gray-400" v-else>
                    Немає аккаунту? <span @click="activeTab = 'register'"
                        class="text-blue-500 font-semibold cursor-pointer">Зареєструватися</span>
                </p>
            </div>
        </div>
    </div>

</template>

<script setup>
import { ref } from 'vue';

const activeTab = ref('login'); // Вкладки логін/реєстрація

const loginForm = ref({
    email: '',
    password: ''
});

const registerForm = ref({
    name: '',
    email: '',
    password: ''
});

const handleLogin = () => {
    console.log('Login form submitted', loginForm.value);
};

const handleRegister = () => {
    console.log('Register form submitted', registerForm.value);
};
</script>
