<template>
    <router-link
        class="text-blue-500 dark:text-blue-400 hover:underline"
        :to="to"
    >
        <slot></slot>
    </router-link>
</template>

<script setup>
defineProps({
    to: { type: String, default: "/" },
});
</script>
