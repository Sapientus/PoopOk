<script setup lang="ts">
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const { comment } = defineProps<{
    comment: Object;
}>();

const hideReplies = ref(true);
</script>

<template>
    <div :class="`comment ${comment.replies.length ? 'comment--haveReplies' : ''}`">
        <div v-if="comment.replies.length" class="comment__border"></div>
        <div class="comment__border-radius"></div>
        <div class="comment__content">

            <div class="comment__content-col">
                <UserAvatar :src="comment.user.avatar" />
            </div>
            <div class="comment__content-col">
                <PostHeader
                    :user="comment.user"
                    :createdAt="comment.createdAt"
                />
                <PostContent :content="comment.text" />
                <PostActions
                    :likes="comment?.likes"
                    :commentsCount="comment.replies.length"
                />
            </div>
        </div>
        <div v-if="comment.replies.length" class="comment__replies-wrapp">
            <div v-if="hideReplies" class="comment__replies--border"></div>
            <div
                class="comment__replies-more"
                v-if="hideReplies"
                @click="hideReplies = !hideReplies"
            >
                {{ comment.replies.length === 1 ? t('showRepliesOne', { count: comment.replies.length }) : t('showRepliesAll', { count: comment.replies.length }) }}
            </div>
            <div
                class="comment__replies"
                v-else-if="!hideReplies"
                v-for="replie in comment.replies"
                :key="replie.id"
            >
                <Comments :comment="replie" />
            </div>
        </div>
        <div v-if="!hideReplies" class="comment__input">
            <div class="comment__replies--border"></div>

            <input type="text" placeholder="Enter your comment" />
        </div>
    </div>
</template>
<style lang="scss">
.comment {
    position: relative;

    &--haveReplies {
        margin-bottom: 16px;
    }

    &__input {
        position: relative;
        padding-left: 42px;
        input {
            width: 100%;
            padding: 8px 16px;
            border: 1px solid var(--border);
            border-radius: 4px;
            background: var(--border);
            color: var(--primery-text);
        }
    }

    &__content {
        position: relative;
        display: flex;
        gap: 10px;
    }

    &__border {
        position: absolute;
        top: 38px;
        left: 16px;
        width: 2px;
        height: calc(100% - 60px);
        background-color: var(--border);
    }

    &__replies-wrapp {
        position: relative;
        padding-left: 42px;
    }

    &__replies {
        padding: 10px 0;
        .comment {
            &__border-radius {
                position: absolute;
                top: -15px;
                left: -26px;
                width: 22px;
                height: 36px;
                border-color: var(--border);
                border-bottom-left-radius: 10px;
                border-bottom-style: solid;
                border-left-style: solid;
                border-bottom-width: 2px;
                border-left-width: 2px;
            }
        }


        &--border {
            position: absolute;
            top: 0;
            left: 16px;
            width: 22px;
            height: calc(50% + 2px);
            border-color: var(--border);
            border-bottom-left-radius: 10px;
            border-bottom-style: solid;
            border-left-style: solid;
            border-bottom-width: 2px;
            border-left-width: 2px;
        }
    }

    &__replies-more {
        position: relative;
        padding: 8px 0;
        font-size: 14px;
        color: var(--primery-text);
        cursor: pointer;


    }
}
</style>
