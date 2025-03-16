export interface User {
  id: number;
  username: string;
  avatar: string;
  name: string;
  email: string;
  createdAt: string;
}

const user: User = {
  id: 1,
  username: "john_doe",
  avatar: "https://xsgames.co/randomusers/assets/avatars/male/1.jpg",
  name: "John Doe",
  email: "john.doe@example.com",
  createdAt: "2025-01-01T00:00:00.000Z",
};

export default user; 