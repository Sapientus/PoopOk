<template>
    <div class="switcher">
        <!-- Arrow Close -->
        <div class="switcher__header">
            <Icon
                name="fluent:arrow-up-24-regular"
                class="switcher__arrow"
                @click="toggleOpen"
            />
            <span>{{ t("theme") }}</span>
        </div>
        <div class="switcher__block">
            <span class="switcher__bg" :style="`left: ${position}px`"></span>
            <label class="switcher__item">
                <input
                    type="radio"
                    name="theme"
                    value="light"
                    v-model="selectedTheme"
                />
                <Icon name="fluent:weather-sunny-24-regular" />
            </label>

            <label class="switcher__item">
                <input
                    type="radio"
                    name="theme"
                    value="dark"
                    v-model="selectedTheme"
                />
                <Icon name="fluent:weather-moon-24-regular" />
            </label>

            <label class="switcher__item switcher__item--text">
                <input
                    type="radio"
                    name="theme"
                    value="system"
                    v-model="selectedTheme"
                />
                {{ $t("auto") }}
            </label>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, defineProps, defineEmits } from "vue";
import { useI18n } from "vue-i18n";

const { t } = useI18n();

const props = defineProps<{
    toggleSwitcher?: boolean;
}>();

const emit = defineEmits(["update:toggle"]);

const toggleOpen = () => {
    emit("update:toggle", false);
};

const selectedTheme = ref<"light" | "dark" | "system">("system");
const position = ref(0);

// Проставляємо тему при завантаженні компонента
onMounted(() => {
    const savedTheme = localStorage.getItem("theme") as
        | "light"
        | "dark"
        | "system"
        | null;
    if (savedTheme) {
        selectedTheme.value = savedTheme;
        applyTheme(savedTheme);
    } else {
        applyTheme("system");
    }
});

// Слідкуємо за зміною теми і застосовуємо її
watch(selectedTheme, (newTheme) => {
    localStorage.setItem("theme", newTheme);
    applyTheme(newTheme);
});

// Функція зміни теми
function applyTheme(theme: "light" | "dark" | "system") {
    const root = document.documentElement;
    position.value = theme === "system" ? 145 : theme === "light" ? 5 : 75;
    if (theme === "system") {
        const prefersDark = window.matchMedia(
            "(prefers-color-scheme: dark)",
        ).matches;
        root.classList.toggle("dark", prefersDark);
    } else {
        root.classList.toggle("dark", theme === "dark");
    }
}
</script>

<style lang="scss">
.switcher {
    display: flex;
    flex-direction: column;
    align-items: center;

    padding: 10px;

    &__header {
        display: flex;
        justify-content: start;
        align-items: center;

        width: 100%;

        margin-bottom: 10px;

        cursor: pointer;
    }
    &__arrow {
        padding: 0 10px;
        margin-right: 55px;

        transform: rotateZ(-90deg);

        cursor: pointer;
    }

    &__block {
        position: relative;
        display: flex;

        background-color: var(--primary-bg);
        box-shadow: inset 0 0 5px 1px var(--box-shadow);
        border-radius: 15px;
    }

    &__bg {
        display: block;
        position: absolute;
        top: 5px;
        width: 60px;
        height: 35px;

        padding: 10px 15px;

        border-radius: 10px;

        background-color: var(--tertiary-bg);

        transition: left 0.3s cubic-bezier(0.38, 0.3, 0, 0.31);

        z-index: 0;
    }

    &__item {
        display: flex;
        align-items: center;
        justify-content: center;

        width: 70px;
        height: 45px;

        font-size: 20px;

        cursor: pointer;

        z-index: 1;

        &--text {
            font-size: 12px;
            text-transform: uppercase;
        }
    }
}

input[type="radio"] {
    margin-right: 8px;
    display: none;
}

.dark {
}
</style>
