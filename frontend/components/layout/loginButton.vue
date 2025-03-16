<template>
    <div class="login">
        <NuxtLink to="/login">
            <button class="login__button">{{ t("login") }}</button>
        </NuxtLink>
    </div>
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>

<style lang="scss">
.login {
    position: fixed;
    top: 20px;
    right: 20px;

    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
