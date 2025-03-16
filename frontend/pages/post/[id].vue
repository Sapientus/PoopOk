<script setup lang="ts">
definePageMeta({
    title: "Post",
    description: "Post page",
    middleware: ["track-previous"],
});

import HeaderPage from "../../components/headerPage.vue";
import { useI18n } from "vue-i18n";
import { useRoute } from "vue-router";
const { t } = useI18n();

const showModal = ref(true);

const router = useRoute();
const postId = router.params.id;
const previousPage: string = useState("previousPath");
const backLink: string =
    previousPage.value === router.path ? "/" : previousPage;


const { data: post, pending } = useAsyncData(`post-${postId}`, async () => {
    return await $fetch(`/api/posts/${postId}`);
});


const openMadal = () => {
    showModal.value = true;
}
</script>

<template>
    <HeaderPage title="postTitle" :back-link="backLink">
        <div class="page-post">
            <div class="page-post__post">
                <SkeletonPost v-if="pending" />
                <PagePostCard v-else :post="post" :user="post.user" />
            </div>
            <div class="page-post__activity">
                <div class="page-post__activity--wrapper">
                    <span class="page-post__activity--answer">Відповіді</span>
                    <div class="page-post__activity--watch">
                        <span>Переглянути дії <Icon name="" /></span>
                    </div>
                </div>
            </div>
            <div
                class="page-post__comment"
                v-if="post?.comments?.length > 0"
                v-for="comment in post.comments"
                :key="comment.id"
            >
                <Comments :comment="comment" />
            </div>
        </div>
        <div class="page-post__input" @click="openMadal()">
            <div class="page-post__input--wrapper">
                <UserAvatar :src="post.user.avatar" />
                <span>{{ t('addComment') }}</span>
            </div>
        </div>
    </HeaderPage>
    <UiModal v-model="showModal" id="modal-post" title="addCommentTitle">
        <div class="modal__post">
            <SkeletonPost v-if="pending" />
            <div v-else class="modal__post--wrapper">
                <div class="modal__post--wrapper-avatar">
                    <UserAvatar :src="post.user.avatar" />
                </div>
                <div class="modal__post--wrapper-content">
                    <PostHeader :user="post.user" :createdAt="post.createdAt" />
                    <PostContent :content="post.content" />
                </div>
            </div>
        </div>
        <div class="modal__post--input">
            <div class="modal__post--input-avatar">
                <UserAvatar :src="user.avatar" />
            </div>
            <UiBaseInput v-model="comment" :placeholder="t('addComment')" />
        </div>

        <div class="modal__submit">
            <button type="submit" class="modal__submit-button">
                {{ t("send") }}
            </button>
        </div>
    </UiModal>
</template>


<style lang="scss">
.page-post {
    position: relative;
    display: flex;
    flex-direction: column;

    flex-grow: 1;

    height: 100%;

    &__input {
        position: sticky;
        bottom: 0;
        left: -3px;
        right: -3px;

        display: flex;
        align-items: center;
        justify-content: space-between;
        
        padding: 5px 24px;

        background-color: var(--primary-bg);

        border-top: 1px solid var(--border);

        cursor: pointer;

        &--wrapper {
            display: flex;
            align-items: center;
            gap: 10px;

            width: 100%;

            padding: 10px 15px;

            background-color: var(--secondary-bg);

            border-radius: 30px;

            span {
                font-size: 14px;
                font-weight: 400;
                color: var(--secondary-text);
            }
        }
    }

    &__activity {
        display: flex;
        align-items: center;
        justify-content: flex-end;

        width: 100%;

        margin-top: 5px;
        padding: 0 24px;

        font-size: 14px;

        border-top: 1px solid var(--border);

        &--wrapper {
            display: flex;

            width: 100%;

            padding: 24px 0;

            
        }

        &--answer {
            font-weight: 600;
            color: var(--primery-text);
        }

        &--watch {
            display: flex;
            justify-content: flex-end;

            width: 100%;

            color: var(--secondary-text);

            span {
                cursor: pointer;
            }
        }
    }

    &__comment {
        padding: 10px 24px;

        border-top: 1px solid var(--border);
    }
}

.modal__post {
    padding: var(--padding-medium);

    &--wrapper {
        position: relative;
        display: flex;
        gap: 10px;

        &::after {
            content: "";
            position: absolute;
            top: 40px;
            left: 18px;

            display: block;

            width: 2px;
            height: calc(100% - 20px);

            background-color: var(--border);
        }
        
        &-content {
            display: flex;
            flex-direction: column;
            gap: 10px;
            
        }
    }
}
</style>
