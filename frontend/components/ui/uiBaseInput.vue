<template>
    <div class="input">
        <div class="input__wrapper">
            <input
                :type="currentType"
                :value="modelValue"
                @input="handleInput"
                :placeholder="placeholder"
                :autocomplete="
                    currentType === 'password' ? 'current-password' : 'username'
                "
                class="input__field"
            />
            <div
                v-if="type === 'password'"
                @click="togglePasswordVisibility"
                class="input__icon-wrapper input__icon-wrapper--password"
            >
                <Icon
                    v-if="showPassword"
                    name="fluent:eye-24-regular"
                    icon-class="input__icon"
                />
                <Icon
                    v-else
                    name="fluent:eye-off-24-regular"
                    icon-class="input__icon"
                />
            </div>
            <div v-else class="input__icon-wrapper">
                <slot name="icon" />
            </div>
        </div>
        <span v-if="errorMessage && showErrors" class="input__error">
            {{ errorMessage }}
        </span>
    </div>
</template>

<script setup lang="ts">
import { ref, defineProps, defineEmits } from "vue";

// Типізація пропсів
const props = defineProps<{
    type?: string;
    modelValue: string;
    showErrors?: boolean;
    errorMessage?: string;
    placeholder?: string;
}>();

// Типізація подій
const emit = defineEmits<{
    (e: "update:modelValue", value: string): void;
}>();

// Локальний стан для типу інпуту
const currentType = ref(props.type || "text");
const showPassword = ref(false);

// Обробник вводу
function handleInput(event: Event) {
    const target = event.target as HTMLInputElement;
    emit("update:modelValue", target.value);
}

// Показати/приховати пароль
const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value;
    currentType.value = showPassword.value ? "text" : "password";
};
</script>

<style scoped lang="scss">
/* BEM Стилі */
.input {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.input__wrapper {
    position: relative;
    width: 100%;
}

.input__field {
    width: 100%;

    padding: 10px 15px;

    background: var(--primary-bg);
    border: 1px solid var(--border);
    border-radius: 5px;
    outline: none;

    font-size: 14px;
    color: #333;

    transition: border-color 0.2s;
}

.input__field:focus {
    border-color: var(--border-focus);
}

.input__icon-wrapper {
    position: absolute;
    right: 10px;
    top: 50%;

    display: flex;
    align-items: center;

    background: none;
    border: none;

    transform: translateY(-50%);

    &--password {
        cursor: pointer;
    }
}

.input__icon {
    width: 20px;
    height: 20px;
    color: var(--primary-icon);
}

.input__error {
    margin-top: 5px;
    font-size: 12px;
    color: red;
}
</style>
