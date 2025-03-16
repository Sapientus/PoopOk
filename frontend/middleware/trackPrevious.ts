import { defineNuxtRouteMiddleware } from "nuxt/app";

export default defineNuxtRouteMiddleware((to, from) => {
  if (from.fullPath) {
    useState("previousPath", () => from.fullPath);
  }
});
