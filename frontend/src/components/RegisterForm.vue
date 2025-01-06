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
      <div class="w-full bg-gray-200 rounded-md my-2 h-2 overflow-hidden">
        <div
            class="h-full transition-all duration-300"
            :style="{ width: progress + '%', backgroundColor: progressColor }"
        ></div>
      </div>
      <div class="validation-rules text-gray-700">
        <div :class="{ 'text-green-800': hasLowerAndUpper }" class="flex items-center">
          <Icon v-if="!hasLowerAndUpper" icon-name="icon-exclamation" icon-class="h-4 w-4 text-red-800" />
          <Icon
            v-if="hasLowerAndUpper"
            icon-name="icon-check"
            icon-class="h-4 w-4 text-green-800"/>
          <span class="ml-2">{{t('passwordCase')}}</span></div>
        <div :class="{ 'text-green-800': hasNumber }" class="flex items-center">
          <Icon v-if="!hasNumber" icon-name="icon-exclamation" icon-class="h-4 w-4 text-red-800" />
          <Icon
            v-if="hasNumber"
            icon-name="icon-check"
            icon-class="h-4 w-4 text-green-800"/>
          <span class="ml-2">{{t('passwordNumber')}}</span></div>
        <div :class="{ 'text-green-800': hasSpecialChar }" class="flex items-center">
          <Icon v-if="!hasSpecialChar" icon-name="icon-exclamation" icon-class="h-4 w-4 text-red-800" />
          <Icon
            v-if="hasSpecialChar"
            icon-name="icon-check"
            icon-class="h-4 w-4 text-green-800"/>
          <span class="ml-2">{{t('passwordSpecial')}}</span></div>
        <div :class="{ 'text-green-800': hasMinLength }" class="flex items-center">
          <Icon v-if="!hasMinLength" icon-name="icon-exclamation" icon-class="h-4 w-4 text-red-800" />
          <Icon
            v-if="hasMinLength"
            icon-name="icon-check"
            icon-class="h-4 w-4 text-green-800"/>
          <span class="ml-2">{{t('passwordLength', {min: 6})}}</span></div>
      </div>
    </div>
<!--    <div class="mb-4">-->
<!--      <label for="password" class="block text-gray-800 dark:text-gray-200">{{-->
<!--        t("confirmPassword")-->
<!--      }}</label>-->
<!--      <div class="relative">-->
<!--        <BaseInput-->
<!--          v-model="form.confirm"-->
<!--          type="password"-->
<!--          :error-message="errors.confirmPassword"-->
<!--          :show-errors="showErrors"-->
<!--          @input="inputHandler"-->
<!--        />-->
<!--      </div>-->
<!--    </div>-->
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
import Icon from "@/utils/Icon.vue";

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
  // confirm: "",
});

const errors = ref({
  username: "",
  email: "",
  password: "",
  // confirmPassword: "",
});

const hasLowerAndUpper = computed(() => {
  return /[a-z]/.test(form.password) && /[A-Z]/.test(form.password);
});

const hasNumber = computed(() => {
  return /[0-9]/.test(form.password);
});

const hasSpecialChar = computed(() => {
  return /[!@#$%^&*]/.test(form.password);
});

const hasMinLength = computed(() => {
  return form.password.length >= 6;
});
const totalValidConditions = computed(() => {
  return (
      hasLowerAndUpper.value +
      hasNumber.value +
      hasSpecialChar.value +
      hasMinLength.value
  );
});
const progress = computed(() => {
  const startProgress = form.password.length > 0 ? 10 : 0;
  return startProgress + (totalValidConditions.value / 4) * 100;
});

const progressColor = computed(() => {
  console.log(progress.value);
  if (progress.value < 25 || progress.value === 0) return "#FF0000"; // Червоний
  if (progress.value < 50) return "#FFA500"; // Помаранчевий
  if (progress.value < 100) return "#FFD700"; // Жовтий
  return "#28a745"; // Зелений
});


const emailRules = [required, isEmail];
const nameRules = [required, minLength(3)];
const passwordRules = [required, minLength(6)];
// const confirmPasswordRules = [required, confirmPassword(() => form.password)];

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

  // errors.value.confirmPassword = validateInput(
  //   form.confirm,
  //   confirmPasswordRules,
  // );
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
    // confirmPassword: "",
  });

  showModal.value = true;
  console.log(form, formValid);
};
</script>
