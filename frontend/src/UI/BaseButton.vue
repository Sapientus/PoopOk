<template>
  <button
    class="w-full bg-blue-500 text-white py-2 rounded disabled:opacity-50 disabled:cursor-not-allowed hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
    :type="type"
    :disabled="disabled"
    @click="clickHandler"
  >
    <slot></slot>
  </button>
</template>

<script setup>
const emit = defineEmits(["click"]);

defineProps({
  type: { type: String, default: "button" },
  disabled: { type: Boolean, default: false },
});

const clickHandler = () => {
  emit("click");
};
</script>
