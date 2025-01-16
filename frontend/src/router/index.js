import { createRouter, createWebHistory } from "vue-router";
import NotFound from "../pages/NotFound.vue";
import { useUserStore } from "../stores/authStore";

const routes = [
  {
    path: "",
    component: () => import("../components/MainLayout.vue"),
    children: [
      {
        path: "/login",
        component: import("../pages/Login.vue"),
        name: "login",
      },
      {
        path: "/register",
        component: import("../pages/Register.vue"),
        name: "register",
      },
      {
        path: "/reset-password",
        component: import("../pages/ResetPassword.vue"),
        name: "reset-password",
      },
      {
        path: "",
        component: () => import("../pages/Profile.vue"),
        name: "profile",
      },
      {
        path: "/about",
        component: () => import("../pages/About.vue"),
        meta: { requiresAuth: true },
        name: "about",
      },
      {
        path: "/contact",
        component: () => import("../pages/Contact.vue"),
        meta: { requiresAuth: true },
        name: "contact",
      },
      {
        path: "/settings",
        component: () => import("../pages/Settings.vue"),
        name: "settings",
      },
      {
        path: "/chat",
        component: () => import("../pages/Chat.vue"),
        name: "chat",
      },
      {
        path: "/tape",
        component: () => import("../pages/Tape.vue"),
        name: "tape",
      },
    ],
    name: "home",
  },

  {
    path: "/:pathMatch(.*)*",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Захищений маршрут
router.beforeEach((to, from, next) => {
  const authStore = useUserStore(); // Отримуємо store аутентифікації
  if (
    to.matched.some((record) => record.meta.requiresAuth) &&
    !authStore.isAuthenticated
  ) {
    next({ path: "/enter" }); // Якщо не авторизований, перенаправляємо на логін
  } else {
    next(); // Дозволяємо доступ
  }
});

export default router;
