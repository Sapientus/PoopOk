<template>
    <p class="post-content">{{ content }}</p>
</template>

<script setup>
defineProps(["content"]);
</script>

<style lang="scss">
.post-content {
    padding: 5px 0;

    font-size: 14px;
    font-weight: normal;
    line-height: 1.5;
    color: var(--primery-text);
    text-decoration: none;

    &:hover {
        text-decoration: none;
    }
}
</style>
