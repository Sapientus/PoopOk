<script setup lang="ts">
const { post } = defineProps<{
    post?: Object;
}>();
</script>

<template>
    <div class="pagePost-card">
        <div class="pagePost-card__header">
            <UserAvatar :src="post.user.avatar" />
            <PostHeader :user="post.user" :createdAt="post.createdAt" />
        </div>
        <div class="pagePost-card__col">
            <PostContent :content="post.content" />
            <PostActions
                :likes="post.likes"
                :commentsCount="post.comments.length"
            />
        </div>
    </div>
</template>

<style lang="scss">
.pagePost-card {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 24px 24px 0;
    border-bottom: 1px solid var(--border);

    &:last-child {
        border-bottom: none;
    }

    &__header {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    &__col {
        display: flex;
        flex-direction: column;
        gap: 0.7rem;
    }
}
</style>
