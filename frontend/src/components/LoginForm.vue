<template>
  <form @submit.prevent="handleSubmit">
    <div class="mb-4">
      <label for="email" class="block text-gray-800 dark:text-gray-200">{{
        t("email")
      }}</label>
      <BaseInput
        v-model="form.email"
        type="email"
        :errorMessage="errors.email"
        :show-errors="showErrors"
        @input="inputHandler"
      />
    </div>
    <div class="mb-4">
      <label for="password" class="block text-gray-800 dark:text-gray-200">{{
        t("password")
      }}</label>
      <div class="relative">
        <BaseInput
          v-model="form.password"
          type="password"
          :errorMessage="errors.password"
          :show-errors="showErrors"
          @input="inputHandler"
        />
      </div>
    </div>
    <BaseButton type="submit">{{ t("login") }}</BaseButton>
  </form>
</template>

<script setup>
import BaseInput from "@/UI/BaseInput.vue";
import { computed, reactive, ref, watch } from "vue";
import { isEmail, minLength, required } from "@/utils/validationRules.js";
import { validateInput } from "@/utils/validation.js";
import BaseButton from "@/UI/BaseButton.vue";
import { useI18n } from "vue-i18n";

// Використовуємо i18n
const { t } = useI18n();

const form = reactive({
  email: "",
  password: "",
});
const emailRules = [required, isEmail];
const passwordRules = [required, minLength(6)];

const errors = ref({
  email: "",
  password: "",
});

const showErrors = ref(false);

// Перевірка валідності форми
const formValid = computed(() =>
  Object.values(errors.value).every((error) => !error),
);
function inputHandler() {
  errors.value.email = validateInput(form.email, emailRules);
  errors.value.password = validateInput(form.password, passwordRules);
}

const handleSubmit = () => {
  inputHandler();

  if (!formValid.value) {
    showErrors.value = true;
    return;
  }

  // Відправка форми

  // Очистка форми
  Object.assign(form, {
    email: "",
    password: "",
  });
  console.log(form, formValid);
};
</script>
