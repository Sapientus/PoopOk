<template>
    <form @submit.prevent="submitComment">
        <input v-model="commentText" placeholder="Напишіть коментар..." />
        <button type="submit">Відправити</button>
    </form>
</template>

<script setup>
import { ref } from "vue";

const emit = defineEmits(["add-comment"]);

const commentText = ref("");

const submitComment = () => {
    if (commentText.value.trim()) {
        emit("add-comment", commentText.value);
        commentText.value = "";
    }
};
</script>
