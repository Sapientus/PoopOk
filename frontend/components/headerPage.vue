<script setup lang="ts">
import { useI18n } from "vue-i18n";

const { title, backLink, dots, views } = defineProps<{
    title: string;
    backLink?: string;
    dots?: boolean;
    views?: string | number;
}>();

const { t } = useI18n();
</script>

<template>
    <div class="content">
        <div class="content__title">
            <div class="content__blocks">
                <div class="content__item">
                    <NuxtLink
                        v-if="backLink"
                        :to="backLink"
                        class="content__item--link"
                    >
                        <Icon name="fluent:arrow-circle-left-24-regular" />
                    </NuxtLink>
                </div>
                <div class="content__item">
                    <h1>{{ t(title) }}</h1>
                    <span v-if="views" class="content__views">{{
                        t("views", { col: views })
                    }}</span>
                </div>
                <div class="content__item">
                    <div v-if="dots" class="content__button">
                        <Icon
                            name="fluent:re-order-dots-horizontal-24-regular"
                        />
                    </div>
                </div>
            </div>
            <div class="content__title-bottom" />
        </div>
        <div class="content__posts">
            <slot />
        </div>
    </div>
</template>

<style lang="scss">
.content {
    position: relative;

    display: flex;
    align-items: center;
    justify-content: start;
    flex-direction: column;

    width: var(--width-content);
    height: auto;

    // padding-bottom: 20px;

    h1 {
        font-size: 16px;
        font-weight: 600;
    }

    &__title {
        position: sticky;
        top: 0;
        right: 0;

        width: 100%;

        padding: 20px 0;

        background-color: var(--primary-bg);

        text-align: center;

        z-index: 100;

        &::before {
            content: "";
            position: absolute;
            bottom: -20px;
            left: 0;

            width: 20px;
            height: 20px;

            background: transparent;

            border-top: 1px solid var(--border);
            border-top-left-radius: 20px;
            box-shadow: -6px -6px var(--primary-bg);

            z-index: 10;
        }
        &::after {
            content: "";
            position: absolute;
            bottom: -20px;
            right: 0;

            width: 20px;
            height: 20px;

            background: transparent;

            border-top: 1px solid var(--border);
            border-top-right-radius: 20px;
            box-shadow: 6px -6px var(--primary-bg);

            z-index: 10;
        }
        &-bottom {
            position: absolute;
            bottom: 0;
            left: 20px;

            width: calc(100% - 40px);
            height: 1px;

            background-color: var(--border);
        }
    }

    &__blocks {
        display: flex;
        align-items: center;
        justify-content: space-between;

        width: 100%;

        padding: 0 20px;
    }

    &__item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        &--link {
            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 50%;

            font-size: 20px;

            transition: transform 0.3s;

            &:hover {
                transform: scale(1.1);
            }
        }
    }

    &__views {
        font-size: 12px;
        color: var(--secondary-text);
    }

    &__posts {
        position: relative;

        display: flex;
        flex-direction: column;

        width: 100%;
        height: 100%;

        border: 1px solid var(--border);
        border-top: 0;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;


        background-color: var(--secondary-bg);
    }
}
</style>
