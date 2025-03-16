import { defineEventHandler, readBody, createError } from 'h3';
import user from '../data/user';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const { username, password } = body;

  // Перевірка користувача
  if (user.username === username && password === 'password123') { // Простий приклад перевірки пароля
    return { token: 'fake-jwt-token', user };
  } else {
    throw createError({ statusCode: 401, statusMessage: 'Invalid credentials' });
  }
}); 