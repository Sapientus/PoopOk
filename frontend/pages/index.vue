<script setup lang="ts">
import { I18nD, useI18n } from "vue-i18n";
import HeaderPage from "../components/headerPage.vue";
const { t } = useI18n();
const router = useRouter();

definePageMeta({
    title: "Feed",
    description: "Feed page",
});

const { data: posts, pending } = useAsyncData("posts", async () => {
    // await new Promise((resolve) => setTimeout(resolve, 2000)); // Імітація затримки
    return await $fetch("/api/posts");
});

const routerToPost = (id: number) => {
    router.push(`/post/${id}`);
};
</script>

<template>
    <HeaderPage title="feed">
        <SkeletonPost v-if="pending" v-for="n in 12" :key="n" />
        <PostCard
            v-else
            v-for="post in posts"
            :key="post.id"
            :post="post"
            :user="post.user"
            @click="routerToPost(post.id)"
        />
    </HeaderPage>
</template>

<style lang="scss"></style>
