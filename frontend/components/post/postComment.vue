<template>
    <div class="comment">
        <UserAvatar :src="comment.user.avatar" />
        <div>
            <strong>{{ comment.user.name }}</strong>
            <p>{{ comment.text }}</p>
        </div>
    </div>
</template>

<script setup>
defineProps(["comment"]);
</script>
