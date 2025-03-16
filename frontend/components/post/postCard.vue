<template>
    <div class="post-card">
        <div class="post-card__col">
            <UserAvatar :src="post.user.avatar" />
        </div>
        <div class="post-card__col">
            <PostHeader :user="post.user" :createdAt="post.createdAt" />
            <PostContent :content="post.content" />
            <PostActions
                :likes="post.likes"
                :commentsCount="post.comments.length"
                @openComments="routerToPost"
            />
        </div>
    </div>
</template>

<script setup lang="ts">
const { post } = defineProps<{
    post: Object;
}>();

const router = useRouter();

const routerToPost = () => {
    router.push(`/post/${post.id}`); // TODO: fix this
};
</script>

<style lang="scss">
.post-card {
    display: flex;
    gap: 1rem;

    width: 100%;

    padding: 1rem;

    border-bottom: 1px solid var(--border);

    cursor: pointer;

    &:last-child {
        border-bottom: none;
    }

    &__col {
        display: flex;
        flex-direction: column;
        gap: 0.7rem;
    }
}
</style>
