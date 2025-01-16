<template>
    <form @submit.prevent="handleSubmit">
        <div class="mb-4 relative flex items-center h-full">
            <label
                for="username"
                class="text-gray-800 dark:text-gray-100 text-[13px] bg-white dark:bg-gray-800 absolute px-2 top-[-9px] left-[18px] font-semibold z-10"
                >{{ t("username") }}</label
            >
            <BaseInput
                v-model="form.username"
                :placeholder="t('username')"
                :error-message="errors.username"
                :show-errors="showErrors"
                @input="inputHandler"
            />
            <div class="h-5 w-5 absolute right-4 top-[16px]">
                <Icon
                    icon-name="icon-username"
                    icon-class="h-5 w-5 text-gray-500 dark:text-gray-100"
                />
            </div>
        </div>
        <div class="mb-4 relative flex items-center">
            <label
                for="email"
                class="text-gray-800 dark:text-gray-100 text-[13px] bg-white dark:bg-gray-800 absolute px-2 top-[-9px] left-[18px] font-semibold z-10"
                >{{ t("email") }}</label
            >
            <BaseInput
                v-model="form.email"
                :error-message="errors.email"
                :show-errors="showErrors"
                placeholder="name@mail.com"
                @input="inputHandler"
                type="email"
            />
            <div class="h-5 w-5 absolute right-4 top-[16px]">
                <Icon
                    icon-name="icon-mail"
                    icon-class="h-5 w-5 text-gray-500 dark:text-gray-100"
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
                placeholder="******"
                @input="inputHandler"
            />
        </div>

        <div class="mb-4 relative flex items-center">
            <label
                for="password"
                class="text-gray-800 dark:text-gray-100 text-[13px] bg-white dark:bg-gray-800 absolute px-2 top-[-9px] left-[18px] font-semibold z-10"
                >{{ t("confirmPassword") }}</label
            >
            <BaseInput
                v-model="form.confirm"
                type="password"
                placeholder="******"
                @input="inputHandler"
            />
        </div>
        <div class="mb-4">
            <div class="w-full bg-gray-200 rounded-md my-2 h-2 overflow-hidden">
                <div
                    class="h-full transition-all duration-300"
                    :style="{
                        width: progress + '%',
                        backgroundColor: progressColor,
                    }"
                ></div>
            </div>
            <div class="validation-rules text-gray-700 dark:text-gray-100">
                <div
                    :class="{ 'text-green-800': hasLowerAndUpper }"
                    class="flex items-center"
                >
                    <Icon
                        v-if="!hasLowerAndUpper"
                        icon-name="icon-exclamation"
                        icon-class="h-4 w-4 text-red-800 dark:text-rose-600"
                    />
                    <Icon
                        v-if="hasLowerAndUpper"
                        icon-name="icon-check"
                        icon-class="h-4 w-4 text-green-800"
                    />
                    <span class="ml-2">{{ t("passwordCase") }}</span>
                </div>
                <div
                    :class="{ 'text-green-800': hasNumber }"
                    class="flex items-center"
                >
                    <Icon
                        v-if="!hasNumber"
                        icon-name="icon-exclamation"
                        icon-class="h-4 w-4 text-red-800 dark:text-rose-600"
                    />
                    <Icon
                        v-if="hasNumber"
                        icon-name="icon-check"
                        icon-class="h-4 w-4 text-green-800"
                    />
                    <span class="ml-2">{{ t("passwordNumber") }}</span>
                </div>
                <div
                    :class="{ 'text-green-800': hasSpecialChar }"
                    class="flex items-center"
                >
                    <Icon
                        v-if="!hasSpecialChar"
                        icon-name="icon-exclamation"
                        icon-class="h-4 w-4 text-red-800 dark:text-rose-600"
                    />
                    <Icon
                        v-if="hasSpecialChar"
                        icon-name="icon-check"
                        icon-class="h-4 w-4 text-green-800"
                    />
                    <span class="ml-2">{{
                        t("passwordSpecial", { value: "(!@#$%^&*)" })
                    }}</span>
                </div>
                <div
                    :class="{ 'text-green-800': hasMinLength }"
                    class="flex items-center"
                >
                    <Icon
                        v-if="!hasMinLength"
                        icon-name="icon-exclamation"
                        icon-class="h-4 w-4 text-red-800 dark:text-rose-600"
                    />
                    <Icon
                        v-if="hasMinLength"
                        icon-name="icon-check"
                        icon-class="h-4 w-4 text-green-800"
                    />
                    <span class="ml-2">{{
                        t("passwordLength", { min: 6 })
                    }}</span>
                </div>
                <div
                    :class="{ 'text-green-800': hasPasswordConfirm }"
                    class="flex items-center"
                >
                    <Icon
                        v-if="!hasPasswordConfirm"
                        icon-name="icon-exclamation"
                        icon-class="h-4 w-4 text-red-800 dark:text-rose-600"
                    />
                    <Icon
                        v-if="hasPasswordConfirm"
                        icon-name="icon-check"
                        icon-class="h-4 w-4 text-green-800"
                    />
                    <span class="ml-2">{{ t("passwordConfirm") }}</span>
                </div>
            </div>
        </div>
        <BaseButton type="submit">{{ t("register") }}</BaseButton>
    </form>
    <Modal v-model="showModal" id="registerModal">
        <h2 class="text-xl font-bold mb-4">{{ t(modalValue) }}</h2>
        <p v-if="modalValue === 'emailExist'">{{ t("checkEmail") }}</p>
        <p v-else>Link</p>
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
import { useUserStore } from "@/stores/authStore";

// Використовуємо i18n
const { t } = useI18n();

const form = reactive({
    username: "",
    email: "",
    password: "",
    confirm: "",
});
const modalValue = ref("");

const errors = ref({
    username: "",
    email: "",
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

const hasPasswordConfirm = computed(() => {
    return form.password === form.confirm && form.confirm.length;
});
const totalValidConditions = computed(() => {
    return (
        hasLowerAndUpper.value +
        hasNumber.value +
        hasSpecialChar.value +
        hasMinLength.value +
        hasPasswordConfirm.value
    );
});
const progress = computed(() => {
    const startProgress = form.password.length > 0 ? 10 : 0;
    return startProgress + (totalValidConditions.value / 5) * 100;
});

const progressColor = computed(() => {
    if (progress.value < 20 || progress.value === 0) return "#da1e28"; // Червоний
    if (progress.value < 40) return "#8e6a00"; // Помаранчевий
    if (progress.value < 60) return "#ba4e00"; // Жовтий
    if (progress.value < 80) return "#ff832b"; // Жовтий
    if (progress.value < 100) return "#f1c21b"; // Жовтий
    return "#28a745"; // Зелений
});

const emailRules = [required, isEmail];
const nameRules = [required, minLength(3)];

const showErrors = ref(false);

const showModal = ref(false);

// Перевірка валідності форми
const formValid = computed(() =>
    Object.values(errors.value).every((error) => !error),
);

function inputHandler() {
    errors.value.username = validateInput(form.username, nameRules);
    errors.value.email = validateInput(form.email, emailRules);
}

const handleSubmit = async () => {
    const userStore = await useUserStore();

    inputHandler();
    if (!formValid.value || progress.value < 100) {
        showErrors.value = true;
        return;
    }

    // Відправка форми
    const res = userStore.signUp(form);
    if (res && res.status === 201) {
        modalValue.value = "emailExist";
        showModal.value = true;
    } else if (res) {
        modalValue.value = "successRegister";
        showModal.value = true;
    }

    // Очистка форми
    Object.assign(form, {
        username: "",
        email: "",
        password: "",
        confirm: "",
    });
};
</script>
