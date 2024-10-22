<template>
    <div class="h-full w-full flex bg-gray-100 dark:bg-gray-900">
        <!-- Список чатів (історія чатів) -->
        <div
            class="w-1/4 h-full bg-white dark:bg-gray-800 p-4 overflow-y-auto border-r border-gray-300 dark:border-gray-600">
            <h2 class="text-2xl font-bold mb-4 text-gray-800 dark:text-gray-200">Історія чатів</h2>
            <ul>
                <li v-for="(chat, index) in chatList" :key="index" @click="selectChat(index)"
                    class="p-2 mb-2 cursor-pointer bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 rounded">
                    {{ chat.name }}
                </li>
            </ul>
        </div>

        <!-- Основний чат -->
        <div class="w-3/4 h-full flex flex-col bg-white dark:bg-gray-800 p-4">
            <div class="flex h-full overflow-hidden max-h-full items-end mb-4">
                <div class="max-h-full flex flex-col flex-1 overflow-y-auto" >
                    <!-- Повідомлення чату -->
                    <div v-for="(message, index) in currentChat.messages" :key="index"
                        class="mb-2 p-2 rounded-lg max-w-md"
                        :class="{ 'self-end bg-blue-500 text-white': message.from === 'me', 'self-start bg-gray-200 text-gray-800 dark:bg-gray-700': message.from === 'other' }">
                        {{ message.text }}
                    </div>
                </div>
            </div>

            <!-- Введення повідомлення -->
            <div class="flex items-center">
                <input v-model="newMessage" @keyup.enter="sendMessage" type="text"
                    placeholder="Написати повідомлення..."
                    class="flex flex-1 flex-col justify-end p-2 bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
                <button @click="sendMessage"
                    class="p-2 bg-blue-500 text-white rounded-r-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">
                    Відправити
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const chatList = ref([
    { name: 'Чат 1', messages: [{ from: 'other', text: 'Привіт!' }, { from: 'me', text: 'Привіт, як справи?' }, { from: 'other', text: 'New!' }] },
    { name: 'Чат 2', messages: [{ from: 'me', text: 'Що нового?' }] },
]);

const currentChatIndex = ref(0);
const currentChat = ref(chatList.value[currentChatIndex.value]);
const newMessage = ref('');

const selectChat = (index) => {
    currentChatIndex.value = index;
    currentChat.value = chatList.value[index];
};

const sendMessage = () => {
    if (newMessage.value.trim() === '') return;
    currentChat.value.messages.push({ from: 'me', text: newMessage.value });
    newMessage.value = '';
    // Автоскролл донизу
    setTimeout(() => {
        const chatBox = document.querySelector('.flex-1');
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 0);
};
</script>