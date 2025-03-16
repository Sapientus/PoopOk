<template>
    <form @submit.prevent="handleSubmit" class="login-form">
        <div class="login-form__group">
            <label for="email" class="login-form__label">{{
                t("email")
            }}</label>
            <UiBaseInput
                v-model="form.email"
                type="email"
                placeholder="name@mail.com"
                :errorMessage="errors.email"
                :show-errors="showErrors"
                @input="inputHandler"
                class="login-form__input"
            >
                <template #icon>
                    <Icon
                        name="fluent:mail-24-regular"
                        class="login-form__icon"
                    />
                </template>
            </UiBaseInput>
        </div>

        <div class="login-form__group">
            <label for="password" class="login-form__label">{{
                t("password")
            }}</label>
            <UiBaseInput
                v-model="form.password"
                type="password"
                placeholder="******"
                :errorMessage="errors.password"
                :show-errors="showErrors"
                @input="inputHandler"
                class="login-form__input"
            />
        </div>

        <div class="login-form__group">
            <div class="login-form__checkbox-container">
                <input
                    type="checkbox"
                    id="remember"
                    class="login-form__checkbox"
                />
                <label for="remember" class="login-form__checkbox-label">{{
                    t("rememberMe")
                }}</label>
            </div>
            <NuxtLink to="/reset-password" class="login-form__forgot-password">
                {{ t("forgotPassword") }}
            </NuxtLink>
        </div>

        <button type="submit" class="login-form__submit-button">
            {{ t("login") }}
        </button>
    </form>
</template>

<script setup lang="ts">
import { computed, reactive, ref } from "vue";
import { useI18n } from "vue-i18n";
import { isEmail, minLength, required } from "../../utils/validationRules";
import { validateInput } from "../../utils/validation";
import { useAuthStore } from "../../store/authStore";

// Використовуємо i18n
const { t } = useI18n();

interface FormState {
    email: string;
    password: string;
}

const form = reactive<FormState>({
    email: "",
    password: "",
});

const errors = ref<Record<keyof FormState, string>>({
    email: "",
    password: "",
});

const showErrors = ref(false);

const emailRules = [required(t), isEmail(t)];
const passwordRules = [required(t), minLength(6, t)];

const formValid = computed(() =>
    Object.values(errors.value).every((error) => !error),
);

const authStore = useAuthStore();

function inputHandler() {
    errors.value.email = validateInput(form.email, emailRules);
    errors.value.password = validateInput(form.password, passwordRules);
}

function handleSubmit() {
    inputHandler();

    if (!formValid.value) {
        showErrors.value = true;
        return;
    }

    // Відправка форми
    fetch('/api/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(form),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Authentication failed');
            }
            return response.json();
        })
        .then(data => {
            localStorage.setItem('token', data.token);
            authStore.login(data.user);
        })
        .catch(error => {
            console.error('Error:', error);
        });

    // Очистка форми
    Object.assign(form, { email: '', password: '' });
}
</script>

<style scoped>
.login-form {
    width: 100%;

    margin: 0 auto;
    padding: 20px;
}

.login-form__group {
    position: relative;

    display: flex;
    justify-content: space-between;
    align-items: center;

    width: 100%;

    margin-bottom: 20px;
}

.login-form__label {
    position: absolute;
    top: -10px;
    left: 15px;

    padding: 0 5px;

    background: var(--primary-bg);

    font-size: 13px;
    color: var(--primary-text);
}

.login-form__input {
    width: 100%;
    padding: 15px;
    border: 1px solid var(--border);
    border-radius: 5px;
}

.login-form__checkbox-container {
    display: flex;
    align-items: center;
}

.login-form__checkbox {
    width: 16px;
    height: 16px;
    margin-right: 5px;
}

.login-form__checkbox-label {
    font-size: 14px;
    color: #333;
}
</style>
