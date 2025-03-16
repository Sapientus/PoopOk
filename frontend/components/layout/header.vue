<template>
    <header class="header">
        <Logo />
        <nav class="menu">
            <li class="menu__item">
                <NuxtLink to="/" class="menu__link">
                    <Icon
                        name="fluent:home-24-regular"
                        class="menu__item--icon"
                    />
                </NuxtLink>
            </li>
            <li class="menu__item">
                <NuxtLink to="/" class="menu__link">
                    <Icon
                        name="fluent:search-24-regular"
                        class="menu__item--icon"
                    />
                </NuxtLink>
            </li>
            <li class="menu__item">
                <button class="menu__button">
                    <Icon
                        name="fluent:add-24-regular"
                        class="menu__item--icon"
                    />
                </button>
            </li>
            <li class="menu__item">
                <NuxtLink to="/" class="menu__link">
                    <Icon
                        name="fluent:heart-24-regular"
                        class="menu__item--icon"
                    />
                </NuxtLink>
            </li>
            <li class="menu__item">
                <NuxtLink to="/" class="menu__link">
                    <Icon
                        name="fluent:person-24-regular"
                        class="menu__item--icon"
                    />
                </NuxtLink>
            </li>
        </nav>
        <div class="burgerWrapper">
            <div
                class="burgerToggle"
                ref="toggleBurgerRef"
                @click="showBurger = !showBurger"
            >
                <Icon name="fluent:list-24-regular" class="menu__item--icon" />
            </div>
            <!-- Burger Menu -->
            <Transition name="open_animate">
                <BurgerMenu v-if="showBurger" ref="menuRef"></BurgerMenu>
            </Transition>
        </div>
    </header>
</template>

<script setup lang="ts">
import Logo from "./logo.vue";
import BurgerMenu from "./burgerMenu.vue";
import { ref } from "vue";
import { onClickOutside } from "@vueuse/core";
import { useI18n } from "vue-i18n";
const { t } = useI18n();

const showBurger = ref(false);
const menuRef = ref<HTMLElement | null>(null);
const toggleBurgerRef = ref<HTMLElement | null>(null);

onClickOutside(
    menuRef,
    () => {
        showBurger.value = false;
    },
    { ignore: [toggleBurgerRef] },
);
</script>

<style lang="scss">
.open_animate-enter-active,
.open_animate-leave-active {
    transition: opacity 0.3s;
}

.open_animate-enter-from,
.open_animate-leave-to {
    opacity: 0;
}

.burgerToggle {
    cursor: pointer;
}

.burgerWrapper {
    position: relative;
}

.header {
    position: fixed;
    left: 0;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    max-width: 100px;
    width: 100%;
    height: 100%;

    padding: 10px;
    padding-bottom: 20px;

    background-color: var(--primary-bg);

    .menu {
        display: flex;
        flex-direction: column;
        align-items: center;

        &__item {
            list-style: none;

            &--icon {
                font-size: 25px;
                color: var(--navigation-icon);
            }
        }

        &__link {
            @include flex-row-center;

            margin: 10px 0;
            list-style: none;
            padding: 0;
            padding: 10px 20px;
            border-radius: 15px;
            transition: all 0.3s ease;

            &:hover {
                background-color: var(--hover-grey);
            }
        }

        &__button {
            @include flex-row-center;

            padding: 15px 20px;
            border-radius: 15px;
            border: none;
            background-color: var(--hover-grey);
            transition: all 0.3s ease;
            outline: none;

            &:hover {
                cursor: pointer;

                .menu__item--icon {
                    color: var(--primary-icon);
                }
            }
        }
    }
}
</style>
