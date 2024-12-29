<template>
  <div
    class="flex justify-center h-full w-full items-center bg-white dark:bg-gray-900"
  >
    <div class="w-1/2 h-full overflow-hidden">
      <img
        src="../assets/main.jpg"
        alt="Main"
        class="w-full h-full object-cover"
      />
    </div>
    <div class="w-1/2 flex flex-col justify-center items-center">
      <div
        class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 max-w-md w-full"
      >
        <AuthForm />
      </div>
    </div>
  </div>
</template>

<script setup>
import AuthForm from "@/components/AuthForm.vue";
</script>
