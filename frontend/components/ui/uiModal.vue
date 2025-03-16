<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from "vue";
import { onClickOutside } from "@vueuse/core";
import { useI18n } from "vue-i18n";

const { t } = useI18n();
interface Props {
    modelValue: boolean;
    id: string;
    title?: string;
}

const props = defineProps<Props>();
const emit = defineEmits<{
    (event: "update:modelValue", value: boolean): void;
}>();

const visible = ref<boolean>(props.modelValue);
const modalRef = ref<HTMLElement | null>(null);

watch(
    () => props.modelValue,
    (newVal) => {
        visible.value = newVal;
    },
);

const closeModal = () => {
    visible.value = false;
    emit("update:modelValue", false);
};

const onEscapeKey = (event: KeyboardEvent) => {
    if (event.key === "Escape") {
        closeModal();
    }
};

onMounted(() => {
    document.addEventListener("keydown", onEscapeKey);
});

onUnmounted(() => {
    document.removeEventListener("keydown", onEscapeKey);
});

onClickOutside(modalRef, closeModal);
</script>

<template>
    <div v-if="visible" class="modal">
        <div ref="modalRef" class="modal__content">
            <div class="modal__header">
                <div class="modal__close" @click="closeModal">{{ t('close') }}</div>
                <h2 class="modal__title" v-if="title">{{ t(title) }}</h2>
                <div class="modal__dots">
                    <Icon name="fluent:re-order-dots-vertical-24-regular" class="icon" />
                </div>
            </div>
            <slot />
            <div v-if="$slots.buttons" class="modal__buttons">
                <slot name="buttons" />
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.modal {
    position: fixed;

    display: flex;
    align-items: center;
    justify-content: center;

    padding-left: 100px;

    inset: 0;
    background: rgba(0, 0, 0, 0.7);

    z-index: 150;

    &__content {
        position: relative;

        width: var(--width-content);

        background: var(--secondary-bg);
        border: 1px solid var(--border);
        border-radius: var(--border-radius);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);

        color: var(--primary-text);
        font-family: var(--font-family);

        transition: all 0.3s ease;
    }


    &__header {
        display: flex;
        align-items: center;
        justify-content: space-between;   
        
        width: 100%;

        padding: 20px 20px;

        border-bottom: 1px solid var(--border);
    }

    &__close {
        width: 70px;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;

        cursor: pointer;
    }


    &__title {
        font-size: 20px;
        font-weight: 600;
    }

    &__dots {
        display: flex;
        align-items: center;
        justify-content: space-between;
        
        
    }

    
    &__buttons {
        margin-top: 20px;
        display: flex;
        justify-content: flex-end;
        gap: 10px;

        button {
            background-color: var(--button-bg);
            color: var(--button-text);
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;

            &:hover {
                background-color: var(--button-hover-bg);
            }
        }
    }
}
</style>
