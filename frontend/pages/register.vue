<script lang="ts" setup>
import { useI18n } from "vue-i18n";

const { t } = useI18n();

definePageMeta({
    layout: "empty",
    title: "Register",
    description: "Register page",
});
</script>

<template>
    <div class="register-page">
        <h1 class="register-page__title">{{ t("register") }}</h1>
        <FormRegister />
        <div class="register-page__link">
            {{ t("haveAccount") }}
            <NuxtLink to="/login">{{ t("login") }}</NuxtLink>
        </div>
    </div>
</template>

<style scoped lang="scss">
.register-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    max-width: 400px;
    width: 100%;
    height: 100vh;

    &__title {
        font-size: 2rem;
        margin-bottom: 1rem;
    }
}
</style>
