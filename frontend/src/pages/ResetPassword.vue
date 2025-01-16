<template>
    <div
        class="flex justify-center h-full w-full items-center bg-white dark:bg-gray-900 bg-[url('./src/assets/bg_auth.svg')] bg-cover bg-top"
    >
        <div
            class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 max-w-md w-full"
        >
            <ResetPasswordForm />
        </div>
    </div>
</template>

<script setup>
import ResetPasswordForm from "../components/ResetPasswordForm.vue";
</script>