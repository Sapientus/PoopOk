<template>
    <div class="flex items-center">
        <!-- Свічер -->
    <button
      @click="toggleTheme"
      class="relative inline-flex items-center h-6 rounded-full w-11 transition-colors duration-300"
      :class="isDark ? 'bg-green-600' : 'bg-gray-900'"
    >
      <!-- Іконка сонця для світлої теми -->
      <WeatherSunny28Filled v-if="isDark" class="h-4 w-4 absolute left-1 text-yellow-400"/>

      <!-- Іконка місяця для темної теми -->
      <WeatherMoon24Filled v-if="!isDark" class="h-4 w-4 absolute right-1 text-gray-400"  />

      <!-- Біла кругла кнопка -->
      <span
        class="inline-block w-4 h-4 transform bg-white rounded-full transition-transform duration-300"
        :class="isDark ? 'translate-x-6' : 'translate-x-1'"
      ></span>
    </button>
    </div>
</template>

<script setup>
import { computed } from 'vue';
import { useThemeStore } from '../stores/themeStore';
import { WeatherMoon24Filled, WeatherSunny28Filled } from "@vicons/fluent";

// Ініціалізація сховища теми
const themeStore = useThemeStore();

themeStore.loadTheme();
// Функція для перемикання теми
const toggleTheme = () => {
    themeStore.toggleTheme();
};

// Обчислене значення для отримання статусу теми
const isDark = computed(() => themeStore.isDark);

</script>