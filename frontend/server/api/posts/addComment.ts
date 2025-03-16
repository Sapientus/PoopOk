import posts from "../../data/posts";
import { readBody } from 'h3';

interface User {
  id: number;
  username: string;
  avatar: string;
  name: string;
}

interface Comment {
  id: number;
  user: User;
  text: string;
  createdAt: string;
  views: number;
  replies: Comment[];
  likes: number;
}

export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const { postId, commentId, text, userId } = body;

  if (!text || !userId) {
    throw createError({ statusCode: 400, statusMessage: "Invalid data" });
  }

  const user = { id: userId, username: "user", avatar: "", name: "User" }; // Замість цього отримайте користувача з бази даних

  if (commentId) {
    // Додаємо реплай до існуючого коментаря або реплая
    const post = posts.find((p) => p.id === postId);
    if (!post) {
      throw createError({ statusCode: 404, statusMessage: "Пост не знайдено" });
    }
    const comment = findCommentById(post.comments, commentId);
    if (!comment) {
      throw createError({ statusCode: 404, statusMessage: "Коментар не знайдено" });
    }
    comment.replies.push({ id: Date.now(), user, text, createdAt: new Date().toISOString(), views: 0, replies: [], likes: 0 });
  } else {
    // Додаємо новий коментар до поста
    const post = posts.find((p) => p.id === postId);
    if (!post) {
      throw createError({ statusCode: 404, statusMessage: "Пост не знайдено" });
    }
    post.comments.push({ id: Date.now(), user, text, createdAt: new Date().toISOString(), views: 0, replies: [], likes: 0 });
  }

  return { success: true };
});

function findCommentById(comments: Comment[], id: number): Comment | null {
  for (const comment of comments) {
    if (comment.id === id) return comment;
    const reply = findCommentById(comment.replies, id);
    if (reply) return reply;
  }
  return null;
} 