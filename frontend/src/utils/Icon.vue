<template>
  <svg :class="['icon', iconClass]" :width="size" :height="size">
    <use :xlink:href="`./src/assets/sprite.svg#${iconName}`"></use>
  </svg>
</template>

<script setup>
import { defineProps } from "vue";

defineProps({
  iconName: { type: String, required: true },
  size: { type: String, default: "24" },
  iconClass: { type: String, default: "" },
});
</script>
