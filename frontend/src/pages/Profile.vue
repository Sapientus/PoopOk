<template>
    <div class="bg-gray-100 dark:bg-gray-900 w-full h-full p-4">
      <div class="max-w-4xl mx-auto bg-white dark:bg-gray-800 shadow-md rounded-lg p-6">
        <header class="flex items-center mb-6">
          <img
            class="w-16 h-16 rounded-full"
            :src="user.avatar"
            alt="User Avatar"
          />
          <div class="ml-4">
            <h1 class="text-2xl font-semibold text-gray-800 dark:text-gray-100">
              {{ user.name }}
            </h1>
            <p class="text-gray-600 dark:text-gray-300">{{ user.email }}</p>
          </div>
          <router-link
            class="ml-auto bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
            to="/settings"
          >
            Settings
          </router-link>
        </header>
  
        <section class="mb-6">
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-100 mb-2">About</h2>
          <p class="text-gray-600 dark:text-gray-300">{{ user.bio }}</p>
        </section>
  
        <section class="mb-6">
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-100 mb-2">Friends</h2>
          <div class="flex flex-wrap">
            <div
              v-for="friend in user.friends"
              :key="friend.id"
              class="flex items-center mr-4 mb-4"
            >
              <img
                class="w-10 h-10 rounded-full"
                :src="friend.avatar"
                alt="Friend Avatar"
              />
              <span class="ml-2 text-gray-800 dark:text-gray-100">{{ friend.name }}</span>
            </div>
          </div>
        </section>
  
        <section class="mb-6">
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-100 mb-2">Recent Activity</h2>
          <ul class="list-disc list-inside text-gray-600 dark:text-gray-300">
            <li v-for="activity in user.recentActivity" :key="activity.id">
              {{ activity.description }} - {{ activity.date }}
            </li>
          </ul>
        </section>
  
        <section>
          <h2 class="text-xl font-semibold text-gray-800 dark:text-gray-100 mb-2">Posts</h2>
          <div class="border-t border-gray-300 dark:border-gray-600 pt-4">
            <div
              v-for="post in user.posts"
              :key="post.id"
              class="bg-gray-50 dark:bg-gray-700 mb-4 p-4 rounded-lg shadow-sm"
            >
              <h3 class="font-semibold text-gray-800 dark:text-gray-100">{{ post.title }}</h3>
              <p class="text-gray-600 dark:text-gray-300">{{ post.content }}</p>
            </div>
          </div>
        </section>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const user = ref({
    name: "John Doe",
    email: "john.doe@example.com",
    bio: "Lover of nature, technology, and coffee.",
    avatar: "https://placehold.co/50x50",
    friends: [
      { id: 1, name: "Alice", avatar: "https://placehold.co/50x50" },
      { id: 2, name: "Bob", avatar: "https://placehold.co/50x50" },
      { id: 3, name: "Charlie", avatar: "https://placehold.co/50x50" },
    ],
    recentActivity: [
      { id: 1, description: "Liked a post", date: "2 hours ago" },
      { id: 2, description: "Commented on a photo", date: "1 day ago" },
    ],
    posts: [
      { id: 1, title: "My first post", content: "Hello, this is my first post!" },
      { id: 2, title: "Another day, another coffee", content: "Enjoying my coffee at the cafe." },
    ],
  });
  </script>
  
  <style scoped>
  /* Додаткові стилі, якщо потрібно */
  </style>
  