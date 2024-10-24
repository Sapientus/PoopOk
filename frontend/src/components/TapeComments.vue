<template>
    <div>
        <div v-for="(comment, index) in comments" :key="index" class="flex items-center">
            <img :src="comment.userAvatar" alt="Avatar" class="w-10 h-10 rounded-full mr-3" />
            <div>
                <h2 class="text-gray-800 dark:text-gray-200 font-bold">{{ comment.username }}</h2>
                <p class="text-gray-600 dark:text-gray-400 text-sm">{{ comment.date }}</p>
                <p class="text-gray-800 dark:text-gray-200">{{ comment.text }}</p>
            </div>
        </div>

        <!-- Поле для введення нового коментаря -->
        <div class="mt-4 flex">
            <input v-model="newComments[index]" placeholder="Ваш коментар..." type="text"
                class="flex-1 p-2 bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 rounded-l focus:outline-none" />
            <button @click="addComment(index)"
                class="bg-blue-500 text-white p-2 rounded-r hover:bg-blue-600">Додати</button>
        </div>
    </div>

</template>

<script setup>
defineProps({
    comments: {
        type: Array,
        required: true
    }
})

function addComment(index) {
    if (newComments[index] !== '') {
        comments[index].comments.push({ text: newComments[index] });
        newComments[index] = '';
    }
}
</script>