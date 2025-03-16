<!-- layouts/default.vue -->
<template>
    <div class="main">
        <!-- Header -->
        <Header />

        <div class="main__page">
            <slot />
        </div>

        <!-- Login Button -->
        <LoginButton />
    </div>
</template>

<script setup lang="ts">
import LoginButton from "../components/layout/loginButton.vue";
import Header from "../components/layout/header.vue";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
</script>

<style lang="scss">
.main {
    display: flex;
    flex-direction: column;

    min-height: 100vh;

    &__page {
        display: flex;
        justify-content: center;
        flex-grow: 1;

        width: 100%;
        height: auto;

        padding-left: 100px;
    }
}
</style>
