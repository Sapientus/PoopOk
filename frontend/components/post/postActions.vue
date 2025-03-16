<template>
    <div class="post-actions">
        <div
            class="post-actions__item post-actions__item--like"
            @click.stop="likePost"
        >
            <Icon
                :name="`fluent:thumb-like-24-${iconLike}`"
                class="post-actions__icon"
            />
            <span>{{ likes }}</span>
        </div>
        <div class="post-actions__item" @click.stop="openComments">
            <Icon name="fluent:comment-24-regular" class="post-actions__icon" />
            <span>{{ commentsCount }}</span>
        </div>
        <div class="post-actions__item" @click.stop>
            <span>
                <Icon
                    name="fluent:arrow-repeat-all-24-regular"
                    class="post-actions__icon"
                />
            </span>
            <span>2</span>
        </div>
    </div>
</template>

<script setup lang="ts">
defineProps(["likes", "commentsCount"]);
const emit = defineEmits<{
    (event: "openComments"): void;
}>();
const iconLike = ref("regular");

const likePost = () => {
    console.log("Like post");
    iconLike.value = "filled";
};

const openComments = () => {
    emit("openComments");
};
</script>

<style lang="scss">
.post-actions {
    display: flex;

    margin-left: -15px;

    &__item {
        display: flex;
        align-items: center;
        gap: 0.5rem;

        padding: 10px 15px;

        background: none;

        border: none;
        border-radius: 15px;

        color: var(--post-icon);

        cursor: pointer;

        transition: all 0.3s ease-in-out;

        &:hover {
            background-color: var(--hover-grey);
        }

        &--like {
            span {
                width: 18px;
            }
        }
    }

    &__icon {
        font-size: 18px;
    }
}
</style>
