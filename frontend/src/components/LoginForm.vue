<template>
    <form @submit.prevent="handleSubmit">
        <div class="mb-4 relative flex items-center">
            <label
                class="text-gray-800 dark:text-gray-100 text-[13px] bg-white dark:bg-gray-800 absolute px-2 top-[-9px] left-[18px] font-semibold z-10"
                >{{ t("email") }}</label
            >
            <BaseInput
                v-model="form.email"
                type="email"
                placeholder="name@mail.com"
                :errorMessage="errors.email"
                :show-errors="showErrors"
                @input="inputHandler"
            />

            <div class="h-5 w-5 absolute right-4 top-[16px]">
                <Icon
                    icon-name="icon-mail"
                    icon-class="h-5 w-5 text-gray-500"
                />
            </div>
        </div>
        <div class="mb-4 relative flex items-center">
            <label
                for="password"
                class="text-gray-800 dark:text-gray-100 text-[13px] bg-white dark:bg-gray-800 absolute px-2 top-[-9px] left-[18px] font-semibold z-10"
                >{{ t("password") }}</label
            >
            <BaseInput
                v-model="form.password"
                type="password"
                :errorMessage="errors.password"
                placeholder="******"
                :show-errors="showErrors"
                @input="inputHandler"
            />
        </div>
        <div class="flex items-center justify-between mb-4 relative">
          <div  class="flex items-center">
            <input type="checkbox" id="remember" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
            <label for="remember" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{ t("rememberMe") }}</label>
          </div>
          <div>
            <BaseLink to="/reset-password" class="text-blue-500">
              {{ t("forgotPassword") }}
            </BaseLink>
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
import Icon from "@/utils/Icon.vue";
import BaseLink from "@/UI/BaseLink.vue";

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
