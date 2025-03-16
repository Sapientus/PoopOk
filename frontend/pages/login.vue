<template>
    <div class="login-page">
        <h1 class="login-page__title">{{ t("login") }}</h1>
        <FormLogin />
        <div class="login-page__link">
            {{ t("noAccount") }}
            <NuxtLink to="/register">{{ t("register") }}</NuxtLink>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { t } = useI18n();
definePageMeta({
    layout: "empty",
});
</script>

<style lang="scss">
.login-page {
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
