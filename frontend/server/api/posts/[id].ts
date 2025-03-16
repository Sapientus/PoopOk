import posts from "../../data/posts";

export default defineEventHandler((event) => {
    const id = Number(getRouterParam(event, "id"));
    const post = posts.find((p) => p.id === id);

    if (!post) {
        throw createError({ statusCode: 404, statusMessage: "Пост не знайдено" });
    }

    return post;
});