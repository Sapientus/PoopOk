<template>
    <div v-if="comments.length" class="comments-section">
        <CommentThread
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"
        />
    </div>
</template>

<script setup>
defineProps(["comments"]);
</script>
