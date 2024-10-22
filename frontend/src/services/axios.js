import axios from 'axios';
import router from '../router';  // Підключимо роутер для редиректу після авторизації

// Створюємо інстанс axios
const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Тут має бути твій бекенд API
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }
});

// Перед кожним запитом додаємо токен до заголовків
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');  // Отримуємо токен з localStorage
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Обробляємо помилки від сервера, наприклад, якщо токен недійсний
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Якщо отримуємо 401 помилку (недійсний токен), намагаємось оновити токен
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        const refresh_token = localStorage.getItem('refresh_token');
        if (refresh_token) {
          const response = await axios.post('http://localhost:8000/api/token/refresh/', { refresh: refresh_token });
          localStorage.setItem('access_token', response.data.access);
          api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
          originalRequest.headers['Authorization'] = `Bearer ${response.data.access}`;
          return api(originalRequest);  // Повторюємо оригінальний запит з оновленим токеном
        }
      } catch (refreshError) {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        router.push({ name: 'Login' });  // Якщо оновлення не вдалось, редирект на логін
      }
    }

    return Promise.reject(error);
  }
);

export default api;
