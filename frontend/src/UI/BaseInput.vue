<template>
  <div class="input-wrapper">
    <div class="relative">
      <input
        :type="currentType"
        :value="model"
        @input="handlerInput"
        :autocomplete="
          currentType === 'password' ? 'current-password' : 'username'
        "
        class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        v-if="type === 'password'"
        type="button"
        @click="togglePasswordVisibility"
        class="absolute inset-y-0 right-0 top-1/2 -translate-y-2/4 pr-3 flex items-center text-sm leading-5"
      >
        <Icon
          v-if="showPassword"
          icon-name="icon-eye"
          icon-class="h-5 w-5 text-gray-500"
        />
        <Icon
          v-else
          icon-name="icon-eye-off"
          icon-class="h-5 w-5 text-gray-500"
        />
      </button>
    </div>
    <span v-if="errorMessage && showErrors" class="text-red-500 text-sm">{{
      errorMessage
    }}</span>
  </div>
</template>

<script setup>
// Props
import { ref } from "vue";
import Icon from "@/utils/Icon.vue";

const props = defineProps({
  type: { type: String, default: "text" }, // тип інпуту
  showErrors: { type: Boolean, default: false }, // показувати помилки
  errorMessage: { type: String, default: "" }, // текст помилки
});

const model = defineModel();

// Emit для оновлення значення
const emit = defineEmits(["input"]);

// Локальний стан для типу інпуту
const currentType = ref(props.type);

// Обробник вводу
function handlerInput(event) {
  model.value = event.target.value;
  emit("input", event.target.value);
}

// Показати/приховати пароль
const showPassword = ref(false);
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
  currentType.value = showPassword.value ? "text" : "password";
};
</script>
