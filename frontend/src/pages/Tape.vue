<template>
    <div class="w-full bg-gray-100 dark:bg-gray-900 p-6">
        <div class="max-w-3xl mx-auto">
            <!-- Стрічка постів -->
            <div v-for="(post, index) in posts" :key="index"
                class="bg-white dark:bg-gray-800 rounded-lg shadow-lg mb-6 p-4">
                <!-- Автор та дата посту -->
                <div class="flex justify-between items-center mb-4">
                    <div class="flex items-center">
                        <img :src="post.userAvatar" alt="Avatar" class="w-10 h-10 rounded-full mr-3" />
                        <div>
                            <h2 class="text-gray-800 dark:text-gray-200 font-bold">{{ post.username }}</h2>
                            <p class="text-gray-600 dark:text-gray-400 text-sm">{{ post.date }}</p>
                        </div>
                    </div>
                </div>

                <!-- Текст посту -->
                <p class="text-gray-800 dark:text-gray-200 mb-4">{{ post.text }}</p>

                <!-- Лайки та коментарі -->
                <div class="flex justify-between items-center w-auto">
                    <button @click="likePost(index)" class="flex items-center text-gray-600 dark:text-gray-400">
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                            viewBox="0 0 512 512" class="w-6 h-6 text-amber-900">
                            <path
                                d="M451.36 369.14C468.66 355.99 480 335.41 480 312c0-39.77-32.24-72-72-72h-14.07c13.42-11.73 22.07-28.78 22.07-48c0-35.35-28.65-64-64-64h-5.88c3.57-10.05 5.88-20.72 5.88-32c0-53.02-42.98-96-96-96c-5.17 0-10.15.74-15.11 1.52C250.31 14.64 256 30.62 256 48c0 44.18-35.82 80-80 80h-16c-35.35 0-64 28.65-64 64c0 19.22 8.65 36.27 22.07 48H104c-39.76 0-72 32.23-72 72c0 23.41 11.34 43.99 28.64 57.14C26.31 374.62 0 404.12 0 440c0 39.76 32.24 72 72 72h368c39.76 0 72-32.24 72-72c0-35.88-26.31-65.38-60.64-70.86z"
                                fill="currentColor"></path>
                        </svg>
                        <span class="ml-2 flex">{{ post.likes }} Likes</span>
                    </button>

                    <!-- Коментарі -->
                    <button @click="toggleComments(index)" class="text-gray-600 dark:text-gray-400">Коментарі</button>
                </div>

                <!-- Форма додавання коментаря -->
                <div v-if="post.showComments" class="mt-4">
                    <h3 class="text-gray-800 dark:text-gray-200 mb-2">Коментарі</h3>
                    <div v-for="(comment, commentIndex) in post.comments" :key="commentIndex"
                        class="p-2 bg-gray-100 dark:bg-gray-700 rounded mb-2">
                        <p class="text-gray-800 dark:text-gray-200">{{ comment.text }}</p>
                    </div>

                    <!-- Поле для введення нового коментаря -->
                    <div class="mt-2 flex">
                        <input v-model="newComments[index]" placeholder="Ваш коментар..." type="text"
                            class="flex-1 p-2 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 rounded-l focus:outline-none" />
                        <button @click="addComment(index)"
                            class="bg-blue-500 text-white p-2 rounded-r hover:bg-blue-600">Додати</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const posts = ref([
    {
        userAvatar: 'https://placehold.co/50x50',
        username: 'Користувач 1',
        date: '18 жовтня 2024',
        text: 'Це мій перший пост!',
        likes: 10,
        comments: [{ text: 'Це круто!' }, { text: 'Я згоден!' }],
        showComments: false,
    },
    {
        userAvatar: 'https://placehold.co/50x50',
        username: 'Користувач 2',
        date: '17 жовтня 2024',
        text: 'Що скажете про цей пост?',
        likes: 5,
        comments: [{ text: 'Це чудово!' }],
        showComments: false,
    },
]);

const newComments = ref(posts.value.map(() => ''));

const likePost = (index) => {
    posts.value[index].likes++;
};

const toggleComments = (index) => {
    posts.value[index].showComments = !posts.value[index].showComments;
};

const addComment = (index) => {
    if (newComments.value[index].trim() !== '') {
        posts.value[index].comments.push({ text: newComments.value[index] });
        newComments.value[index] = '';
    }
};
</script>
