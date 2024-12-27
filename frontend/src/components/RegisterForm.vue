<template>
  <form @submit.prevent="handleSubmit">
    <div class="mb-4">
      <label for="username" class="block text-gray-800 dark:text-gray-200">{{
        t("username")
      }}</label>
      <BaseInput
        v-model="form.username"
        :error-message="errors.username"
        :show-errors="showErrors"
        @input="inputHandler"
      />
    </div>
    <div class="mb-4">
      <label for="email" class="block text-gray-800 dark:text-gray-200">{{
        t("email")
      }}</label>
      <BaseInput
        v-model="form.email"
        :error-message="errors.email"
        :show-errors="showErrors"
        @input="inputHandler"
        type="email"
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
          :error-message="errors.password"
          :show-errors="showErrors"
          @input="inputHandler"
        />
      </div>
    </div>
    <div class="mb-4">
      <label for="password" class="block text-gray-800 dark:text-gray-200">{{
        t("confirmPassword")
      }}</label>
      <div class="relative">
        <BaseInput
          v-model="form.confirm"
          type="password"
          :error-message="errors.confirmPassword"
          :show-errors="showErrors"
          @input="inputHandler"
        />
      </div>
    </div>
    <BaseButton type="submit">{{ t("register") }}</BaseButton>
  </form>
  <Modal v-model="showModal" id="registerModal">
    <h2 class="text-xl font-bold mb-4">{{ t("successRegister") }}</h2>
    <p>{{ t("sendRegisterLink") }}</p>
  </Modal>
</template>

<script setup>
import BaseInput from "@/UI/BaseInput.vue";
import { computed, reactive, ref } from "vue";
import {
  confirmPassword,
  isEmail,
  minLength,
  required,
} from "@/utils/validationRules.js";
import { validateInput } from "@/utils/validation.js";
import BaseButton from "@/UI/BaseButton.vue";
import Modal from "@/UI/Modal.vue";
import { useI18n } from "vue-i18n";

// Використовуємо i18n
const { t } = useI18n();

const form = reactive({
  username: "",
  email: "",
  password: "",
  confirm: "",
});

const errors = ref({
  username: "",
  email: "",
  password: "",
  confirmPassword: "",
});

const emailRules = [required, isEmail];
const nameRules = [required, minLength(3)];
const passwordRules = [required, minLength(6)];
const confirmPasswordRules = [required, confirmPassword(() => form.password)];

const showErrors = ref(false);

const showModal = ref(false);

// Перевірка валідності форми
const formValid = computed(() =>
  Object.values(errors.value).every((error) => !error),
);

function inputHandler() {
  errors.value.username = validateInput(form.username, nameRules);
  errors.value.email = validateInput(form.email, emailRules);
  errors.value.password = validateInput(form.password, passwordRules);

  errors.value.confirmPassword = validateInput(
    form.confirm,
    confirmPasswordRules,
  );
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
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  showModal.value = true;
  console.log(form, formValid);
};
</script>
