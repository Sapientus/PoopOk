<template>
    <div class="reset-password">
        <div class="reset-password__header">
            <h1 class="reset-password__title">{{ t("resetPassword") }}</h1>
            <p class="reset-password__description">
                {{ t("resetPasswordDescription") }}
            </p>
        </div>

        <form class="reset-password__form" @submit.prevent="resetPassword">
            <div class="reset-password__field">
                <label for="email" class="reset-password__label">
                    {{ t("email") }}
                </label>
                <UiBaseInput
                    id="email"
                    name="email"
                    v-model="email"
                    autocomplete="email"
                    placeholder="name@mail.com"
                    class="reset-password__input"
                    required
                >
                    <template #icon>
                        <Icon name="fluent:mail-24-regular" />
                    </template>
                </UiBaseInput>
            </div>
            <div class="reset-password__actions">
                <button type="submit" customClass="reset-password__button">
                    {{ t("resetPassword") }}
                </button>
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
const email = ref<string>("");

definePageMeta({
    layout: "empty",
});

const resetPassword = () => {
    console.log(email.value);
};
</script>

<style lang="scss" scoped>
.reset-password {
    max-width: 400px;
    width: 100%;

    padding: 20px;

    background: var(--primary-bg);
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);

    text-align: center;

    &__header {
        margin-bottom: 20px;
    }

    &__title {
        font-size: 1.5rem;
        font-weight: bold;
        color: var(--primary-text);
    }

    &__description {
        font-size: 0.875rem;
        color: var(--secondary-text);
    }

    &__form {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    &__field {
        position: relative;
        display: flex;
        flex-direction: column;
    }

    &__label {
        font-size: 0.875rem;
        font-weight: bold;
        background: var(--primary-bg);
        position: absolute;
        top: -8px;
        left: 15px;
        padding: 0 5px;
        color: var(--primary-text);
        z-index: 10;
    }

    &__input {
        width: 100%;
        padding: 15px;
        border: 1px solid var(--border);
        border-radius: 5px;
    }

    &__actions {
        display: flex;
        justify-content: center;
    }

    &__button {
        width: 100%;
    }
}
</style>
