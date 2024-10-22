import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import pinia from "./stores/index.js";
import router from "./router";
import i18n from './lang/i18n.js';
import themePlugin from './themePlugin';

// Створюємо один екземпляр додатку
const app = createApp(App);

// Використовуємо pinia
app.use(pinia);
// Використовуємо themePlugin
app.use(themePlugin);
// Використовуємо i18n
app.use(i18n);
// Використовуємо router
app.use(router);

// Монтуємо додаток
app.mount("#app");
