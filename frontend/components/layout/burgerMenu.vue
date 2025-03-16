<template>
    <div class="burger">
        <div v-if="!toggleSwitcher">
            <ul class="burger__list">
                <li
                    class="burger__item burger__item--theme"
                    @click="toggleSwitcher ? '' : (toggleSwitcher = true)"
                >
                    <span>{{ t("theme") }}</span>
                    <Icon name="fluent:arrow-up-24-regular" class="icon" />
                </li>
                <li class="burger__item">
                    <NuxtLink to="insights">{{ t("insights") }}</NuxtLink>
                </li>
                <li class="burger__item">
                    <NuxtLink to="settings">{{ t("settings") }}</NuxtLink>
                </li>
            </ul>
            <ul class="burger__list">
                <li class="burger__item">
                    <span>{{ t("report") }}</span>
                </li>
                <li class="burger__item burger__item--red">
                    <NuxtLink to="logout">{{ t("logout") }}</NuxtLink>
                </li>
            </ul>
        </div>
        <!-- Theme Switcher -->
        <ThemeSwitcher v-if="toggleSwitcher" v-model:toggle="toggleSwitcher" />
    </div>
</template>

<script setup lang="ts">
import { useThemeStore } from "../../store/theme";
import { storeToRefs } from "pinia";
import { ref } from "vue";
import { useI18n } from "vue-i18n";

import ThemeSwitcher from "./themeSwitcher.vue";

const themeStore = useThemeStore();
const { theme } = storeToRefs(themeStore);

const { t } = useI18n();

const toggleSwitcher = ref(false);

const setTheme = (mode: "light" | "dark" | "system") => {
    themeStore.setTheme(mode);
};
</script>

<style lang="scss">
// burger styles
.burger {
    position: absolute;
    bottom: 0;
    left: 0;

    display: flex;
    flex-direction: column;

    background-color: var(--secondary-bg);
    box-shadow: 0 0 15px 1px var(--box-shadow);
    border: 1px solid var(--border);
    border-radius: 15px;

    color: var(--primary-text);

    transition: all 0.3s;

    overflow: hidden;

    &__list {
        display: flex;
        flex-direction: column;

        width: 250px;

        padding: 10px;

        list-style: none;

        a {
            text-decoration: none;
            color: var(--primary-text);
        }

        &:first-child {
            padding-bottom: 10px;
            border-bottom: 1px solid var(--border);
        }
    }

    &__item {
        padding: 10px;

        border-radius: 10px;

        font-size: 14px;
        font-weight: 600;

        cursor: pointer;

        &:hover {
            background-color: var(--hover-grey);
        }

        &--red a {
            color: red;
        }

        &--theme {
            display: flex;
            justify-content: space-between;
            align-items: center;

            .icon {
                transform: rotate(90deg);
            }
        }
    }
}

// burger animation
.burger-enter-active,
.burger-leave-active {
    transition: opacity 0.3s;
}

.burger-enter-from,
.burger-leave-to {
    opacity: 0;
}
// switcher animation
.switcher-enter-active,
.switcher-leave-active {
    transition: opacity 0.3s;
}

.switcher-enter-from,
.switcher-leave-to {
    opacity: 0;
}
</style>
