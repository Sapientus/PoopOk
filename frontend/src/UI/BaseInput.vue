<template>
  <div class="input-wrapper">
    <div class="relative">
    <input
        :type="currentType"
        :value="modelValue"
        @input="onInput"
        @blur="validateInput"
        :autocomplete="currentType === 'password' ? 'current-password' : 'username'"
        class="mt-1 block w-full p-2 text-gray-800 bg-gray-200 dark:bg-gray-700 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
    />
      <button
          v-if="type === 'password'"
          type="button"
          @click="togglePasswordVisibility"
          class="absolute inset-y-0 right-0 top-1/2 -translate-y-2/4 pr-3 flex items-center text-sm leading-5"
      >
        <Icon v-if="showPassword" icon-name="icon-eye" icon-class="h-5 w-5 text-gray-500" />
        <Icon v-else icon-name="icon-eye-off" icon-class="h-5 w-5 text-gray-500" />
      </button>
    </div>
    <span v-if="errorMessage" class="text-red-500 text-sm">{{ errorMessage }}</span>
  </div>
</template>

<script setup>
// Props
import { ref } from "vue";
import Icon from "@/utils/Icon.vue";

const props = defineProps({
  modelValue: {type: [String, Number], required: true}, // value
  type: {type: String, default: "text"}, // тип інпуту
  rules: {type: Array, default: () => []}, // правила валідації
});

// Emit для оновлення значення
const emit = defineEmits(["update:modelValue", "validation-error"]);

const errorMessage = ref("");

// Локальний стан для типу інпуту
const currentType = ref(props.type);

// Обробник вводу
function onInput(event) {
  emit("update:modelValue", event.target.value);
  validateInput();
}

// Функція для перевірки інпуту
function validateInput() {
  for (const rule of props.rules) {
    const result = rule(props.modelValue);
    if (result !== true) {
      errorMessage.value = result; // Перше повідомлення про помилку
      emit("validation-error", result);
      return;
    }
  }
  errorMessage.value = ""; // Очищення помилки
  emit("validation-error", null);
}

const showPassword = ref(false);
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
  currentType.value = showPassword.value ? "text" : "password";
};

</script>
