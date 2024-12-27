<template>
  <div
    v-if="visible"
    class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
    @click="closeModal"
  >
    <div
      class="text-gray-600 bg-white dark:bg-gray-800 p-6 rounded-lg relative"
      @click.stop
    >
      <button
        class="absolute top-2 right-2 text-gray-500 hover:text-gray-700 dark:text-gray-300 dark:hover:text-gray-100"
        @click="closeModal"
      >
        ×
      </button>
      <slot />
      <div v-if="$slots.buttons" class="mt-4 flex justify-end space-x-2">
        <slot name="buttons" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from "vue";

const props = defineProps({
  modelValue: { type: Boolean, required: true },
  id: { type: String, required: true },
});

const emit = defineEmits(["update:modelValue"]);

const visible = ref(props.modelValue);

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

const onEscapeKey = (event) => {
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
</script>
