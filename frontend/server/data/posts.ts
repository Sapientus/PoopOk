export interface User {
  id: number;
  username: string;
  avatar: string;
  name: string;
}

export interface Comment {
  id: number;
  user: User;
  text: string;
  createdAt: string;
  views: number;
  replies: Comment[];
  likes: number;
}

export interface Post {
  id: number;
  user: User;
  content: string;
  likes: number;
  views: number;
  createdAt: string;
  comments: Comment[];
}

const posts: Post[] = [
  {
    id: 1,
    user: {
      id: 1,
      username: "bogdan",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
      name: "Bogdan",
    },
    content: "Всі говорять про це, що ви думаєте?",
    likes: 51,
    views: 106,
    createdAt: "2025-02-10T00:50:28.879445Z",
    comments: [
      {
        id: 416,
        user: {
          id: 4,
          username: "alex",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
          name: "Alex",
        },
        text: "Вражаюче!",
        createdAt: "2025-02-16T12:50:28.879478Z",
        views: 119,
        replies: [
          {
            id: 320,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Цікава думка. lorem ipsum dolor sit amet consectetur adipisicing elit.",
            createdAt: "2025-02-24T13:50:28.879495Z",
            views: 26,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 2,
    user: {
      id: 1,
      username: "bogdan",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
      name: "Bogdan",
    },
    content: "Мої враження від останнього фільму.",
    likes: 6,
    views: 429,
    createdAt: "2025-02-18T10:50:28.879505Z",
    comments: [
      {
        id: 327,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Як цікаво!",
        createdAt: "2025-02-01T07:50:28.879514Z",
        views: 126,
        replies: [
          {
            id: 964,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Вражаюче!",
            createdAt: "2025-02-06T08:50:28.879522Z",
            views: 89,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 846,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-02T01:50:28.879531Z",
            views: 82,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 858,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Чудово написано!",
        createdAt: "2025-01-31T12:50:28.879541Z",
        views: 95,
        replies: [
          {
            id: 973,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Гарний пост!",
            createdAt: "2025-02-16T00:50:28.879548Z",
            views: 49,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 170,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Вражаюче!",
            createdAt: "2025-02-22T12:50:28.879554Z",
            views: 127,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 3,
    user: {
      id: 3,
      username: "mike",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
      name: "Mike",
    },
    content: "Що ви думаєте про нову технологію?",
    likes: 63,
    views: 308,
    createdAt: "2025-02-19T23:50:28.879561Z",
    comments: [
      {
        id: 208,
        user: {
          id: 4,
          username: "alex",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
          name: "Alex",
        },
        text: "Не згоден, але поважаю вашу точку зору.",
        createdAt: "2025-02-14T16:50:28.879568Z",
        views: 34,
        replies: [
          {
            id: 810,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-05T08:50:28.879574Z",
            views: 47,
            replies: [
              {
                id: 8766,
                user: {
                  id: 4,
                  username: "alex",
                  avatar:
                    "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
                  name: "Alex",
                },
                text: "Test!",
                createdAt: "2025-02-03T01:50:28.879580Z",
                views: 51,
                replies: [],
                likes: Math.floor(Math.random() * 100),
              },
            ],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 967,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Вражаюче!",
            createdAt: "2025-02-03T01:50:28.879580Z",
            views: 91,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 991,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Цікава думка. Цікава думка. lorem ipsum dolor sit amet consectetur adipisicing elit. Цікава думка. lorem ipsum dolor sit amet consectetur adipisicing elit. Цікава думка. lorem ipsum dolor sit amet consectetur adipisicing elit.",
            createdAt: "2025-02-12T01:50:28.879586Z",
            views: 11,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 296,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Вражаюче!",
        createdAt: "2025-01-30T07:50:28.879592Z",
        views: 96,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 4,
    user: {
      id: 4,
      username: "alex",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
      name: "Alex",
    },
    content: "Це тестовий пост!",
    likes: 71,
    views: 989,
    createdAt: "2025-02-21T22:50:28.879599Z",
    comments: [
      {
        id: 925,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Дякую за корисну інформацію.",
        createdAt: "2025-02-26T09:50:28.879606Z",
        views: 132,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 203,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Гарний пост!",
        createdAt: "2025-01-30T11:50:28.879622Z",
        views: 76,
        replies: [
          {
            id: 830,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Не згоден, але поважаю вашу точку зору.",
            createdAt: "2025-02-25T20:50:28.879629Z",
            views: 154,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 370,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Як цікаво!",
            createdAt: "2025-02-21T11:50:28.879635Z",
            views: 91,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 600,
        user: {
          id: 3,
          username: "mike",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
          name: "Mike",
        },
        text: "Вражаюче!",
        createdAt: "2025-02-03T11:50:28.879642Z",
        views: 120,
        replies: [
          {
            id: 295,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Цікава думка.",
            createdAt: "2025-02-01T17:50:28.879648Z",
            views: 140,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 428,
            user: {
              id: 5,
              username: "lisa",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
              name: "Lisa",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-05T10:50:28.879654Z",
            views: 173,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 5,
    user: {
      id: 5,
      username: "lisa",
      avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
      name: "Lisa",
    },
    content: "Найкращий день у моєму житті!",
    likes: 90,
    views: 673,
    createdAt: "2025-02-23T20:50:28.879661Z",
    comments: [
      {
        id: 116,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Як цікаво!",
        createdAt: "2025-02-13T02:50:28.879668Z",
        views: 38,
        replies: [
          {
            id: 546,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Вражаюче!",
            createdAt: "2025-02-27T10:50:28.879674Z",
            views: 128,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 425,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Не згоден, але поважаю вашу точку зору.",
            createdAt: "2025-02-25T17:50:28.879680Z",
            views: 156,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 941,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Згоден на всі 100%!",
        createdAt: "2025-02-22T07:50:28.879686Z",
        views: 158,
        replies: [
          {
            id: 690,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "А де більше деталей?",
            createdAt: "2025-02-07T21:50:28.879692Z",
            views: 74,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 893,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Мені сподобалось.",
            createdAt: "2025-02-19T04:50:28.879698Z",
            views: 35,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 569,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Мені сподобалось.",
        createdAt: "2025-02-22T10:50:28.879705Z",
        views: 115,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 6,
    user: {
      id: 1,
      username: "bogdan",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
      name: "Bogdan",
    },
    content: "Мої враження від останнього фільму.",
    likes: 90,
    views: 277,
    createdAt: "2025-02-15T13:50:28.879711Z",
    comments: [
      {
        id: 667,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Згоден на всі 100%!",
        createdAt: "2025-02-21T04:50:28.879718Z",
        views: 192,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 578,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Чудово написано!",
        createdAt: "2025-02-16T20:50:28.879724Z",
        views: 61,
        replies: [
          {
            id: 351,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-22T22:50:28.879730Z",
            views: 22,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 762,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Вражаюче!",
            createdAt: "2025-02-15T13:50:28.879735Z",
            views: 68,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 521,
            user: {
              id: 5,
              username: "lisa",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
              name: "Lisa",
            },
            text: "Як цікаво!",
            createdAt: "2025-02-25T06:50:28.879750Z",
            views: 50,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 181,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Не згоден, але поважаю вашу точку зору.",
        createdAt: "2025-01-31T01:50:28.879761Z",
        views: 99,
        replies: [
          {
            id: 114,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "А де більше деталей?",
            createdAt: "2025-02-28T03:50:28.879771Z",
            views: 84,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 7,
    user: {
      id: 5,
      username: "lisa",
      avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
      name: "Lisa",
    },
    content: "Це тестовий пост!",
    likes: 51,
    views: 582,
    createdAt: "2025-02-16T10:50:28.879779Z",
    comments: [
      {
        id: 104,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Дякую за корисну інформацію.",
        createdAt: "2025-02-28T05:50:28.879786Z",
        views: 52,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 215,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Мені сподобалось.",
        createdAt: "2025-02-08T10:50:28.879791Z",
        views: 105,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 102,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Цікава думка.",
        createdAt: "2025-02-16T22:50:28.879797Z",
        views: 50,
        replies: [
          {
            id: 250,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Гарний пост!",
            createdAt: "2025-02-21T18:50:28.879803Z",
            views: 47,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 156,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "А де більше деталей?",
            createdAt: "2025-02-09T21:50:28.879809Z",
            views: 134,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 253,
            user: {
              id: 5,
              username: "lisa",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
              name: "Lisa",
            },
            text: "Вражаюче!",
            createdAt: "2025-02-26T15:50:28.879814Z",
            views: 180,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 8,
    user: {
      id: 5,
      username: "lisa",
      avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
      name: "Lisa",
    },
    content: "Найкращий день у моєму житті!",
    likes: 90,
    views: 972,
    createdAt: "2025-02-01T00:50:28.879826Z",
    comments: [
      {
        id: 561,
        user: {
          id: 3,
          username: "mike",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
          name: "Mike",
        },
        text: "Згоден на всі 100%!",
        createdAt: "2025-02-17T13:50:28.879839Z",
        views: 192,
        replies: [
          {
            id: 922,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-11T02:50:28.879845Z",
            views: 44,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 574,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Не згоден, але поважаю вашу точку зору.",
            createdAt: "2025-02-10T02:50:28.879851Z",
            views: 137,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 731,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Згоден на всі 100%!",
        createdAt: "2025-02-25T21:50:28.879857Z",
        views: 79,
        replies: [
          {
            id: 792,
            user: {
              id: 5,
              username: "lisa",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
              name: "Lisa",
            },
            text: "Не згоден, але поважаю вашу точку зору.",
            createdAt: "2025-02-06T14:50:28.879863Z",
            views: 62,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 765,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Цікава думка.",
            createdAt: "2025-02-22T07:50:28.879869Z",
            views: 38,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 9,
    user: {
      id: 2,
      username: "jane",
      avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
      name: "Jane",
    },
    content: "Найкращий день у моєму житті!",
    likes: 22,
    views: 105,
    createdAt: "2025-02-07T05:50:28.880008Z",
    comments: [
      {
        id: 233,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Цікава думка.",
        createdAt: "2025-02-21T08:50:28.880018Z",
        views: 191,
        replies: [
          {
            id: 475,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Згоден на всі 100%!",
            createdAt: "2025-02-28T03:50:28.880024Z",
            views: 109,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 707,
        user: {
          id: 4,
          username: "alex",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
          name: "Alex",
        },
        text: "Не згоден, але поважаю вашу точку зору.",
        createdAt: "2025-02-16T08:50:28.880031Z",
        views: 196,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 10,
    user: {
      id: 1,
      username: "bogdan",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
      name: "Bogdan",
    },
    content: "Що ви думаєте про нову технологію?",
    likes: 81,
    views: 382,
    createdAt: "2025-02-09T16:50:28.880039Z",
    comments: [
      {
        id: 309,
        user: {
          id: 3,
          username: "mike",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
          name: "Mike",
        },
        text: "Вражаюче!",
        createdAt: "2025-02-14T11:50:28.880045Z",
        views: 113,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 11,
    user: {
      id: 4,
      username: "alex",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
      name: "Alex",
    },
    content: "Роблю новий проект!",
    likes: 22,
    views: 751,
    createdAt: "2025-02-07T00:50:28.880052Z",
    comments: [
      {
        id: 211,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Не згоден, але поважаю вашу точку зору.",
        createdAt: "2025-01-30T10:50:28.880058Z",
        views: 97,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 12,
    user: {
      id: 4,
      username: "alex",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
      name: "Alex",
    },
    content: "Як пройшов ваш тиждень?",
    likes: 16,
    views: 426,
    createdAt: "2025-01-30T02:50:28.880065Z",
    comments: [
      {
        id: 847,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Дякую за корисну інформацію.",
        createdAt: "2025-02-10T15:50:28.880074Z",
        views: 128,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 609,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Цікава думка.",
        createdAt: "2025-02-22T04:50:28.880084Z",
        views: 163,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 792,
        user: {
          id: 4,
          username: "alex",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
          name: "Alex",
        },
        text: "Не згоден, але поважаю вашу точку зору.",
        createdAt: "2025-02-18T23:50:28.880094Z",
        views: 76,
        replies: [
          {
            id: 478,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Не згоден, але поважаю вашу точку зору.",
            createdAt: "2025-02-06T21:50:28.880101Z",
            views: 55,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 844,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Як цікаво!",
            createdAt: "2025-02-04T14:50:28.880107Z",
            views: 45,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 13,
    user: {
      id: 3,
      username: "mike",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
      name: "Mike",
    },
    content: "Сьогодні чудова погода!",
    likes: 22,
    views: 607,
    createdAt: "2025-02-04T12:50:28.880114Z",
    comments: [
      {
        id: 718,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Цікава думка.",
        createdAt: "2025-02-05T06:50:28.880122Z",
        views: 196,
        replies: [
          {
            id: 111,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Чудово написано!",
            createdAt: "2025-01-31T22:50:28.880128Z",
            views: 10,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 933,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "А де більше деталей?",
            createdAt: "2025-02-09T02:50:28.880134Z",
            views: 58,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 807,
        user: {
          id: 3,
          username: "mike",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
          name: "Mike",
        },
        text: "Чудово написано!",
        createdAt: "2025-02-25T11:50:28.880140Z",
        views: 41,
        replies: [
          {
            id: 665,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-07T23:50:28.880146Z",
            views: 109,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 892,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Як цікаво!",
            createdAt: "2025-02-03T18:50:28.880158Z",
            views: 118,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 404,
            user: {
              id: 5,
              username: "lisa",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
              name: "Lisa",
            },
            text: "А де більше деталей?",
            createdAt: "2025-02-28T09:50:28.880165Z",
            views: 56,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 14,
    user: {
      id: 1,
      username: "bogdan",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
      name: "Bogdan",
    },
    content: "Сьогодні чудова погода!",
    likes: 71,
    views: 941,
    createdAt: "2025-02-12T09:50:28.880171Z",
    comments: [
      {
        id: 590,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Мені сподобалось.",
        createdAt: "2025-01-31T09:50:28.880178Z",
        views: 27,
        replies: [
          {
            id: 308,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Згоден на всі 100%!",
            createdAt: "2025-02-22T22:50:28.880184Z",
            views: 108,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 201,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Гарний пост!",
            createdAt: "2025-02-16T16:50:28.880189Z",
            views: 172,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 239,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Чудово написано!",
        createdAt: "2025-02-11T09:50:28.880196Z",
        views: 88,
        replies: [
          {
            id: 343,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Дякую за корисну інформацію.",
            createdAt: "2025-01-30T09:50:28.880203Z",
            views: 179,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 349,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Згоден на всі 100%!",
        createdAt: "2025-02-09T10:50:28.880249Z",
        views: 62,
        replies: [
          {
            id: 983,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Не згоден, але поважаю вашу точку зору.",
            createdAt: "2025-02-13T08:50:28.880256Z",
            views: 74,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 446,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "А де більше деталей?",
            createdAt: "2025-02-19T05:50:28.880262Z",
            views: 63,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 671,
            user: {
              id: 4,
              username: "alex",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
              name: "Alex",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-27T08:50:28.880267Z",
            views: 140,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 15,
    user: {
      id: 5,
      username: "lisa",
      avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
      name: "Lisa",
    },
    content: "Я щойно прочитав цікаву статтю.",
    likes: 30,
    views: 226,
    createdAt: "2025-02-22T08:50:28.880274Z",
    comments: [
      {
        id: 874,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Мені сподобалось.",
        createdAt: "2025-01-30T02:50:28.880281Z",
        views: 40,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 322,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Чудово написано!",
        createdAt: "2025-02-18T01:50:28.880288Z",
        views: 126,
        replies: [
          {
            id: 797,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Згоден на всі 100%!",
            createdAt: "2025-02-15T06:50:28.880294Z",
            views: 72,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 197,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Згоден на всі 100%!",
            createdAt: "2025-02-06T07:50:28.880300Z",
            views: 139,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 16,
    user: {
      id: 3,
      username: "mike",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
      name: "Mike",
    },
    content: "Що ви думаєте про нову технологію?",
    likes: 18,
    views: 630,
    createdAt: "2025-02-15T20:50:28.880311Z",
    comments: [
      {
        id: 751,
        user: {
          id: 5,
          username: "lisa",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
          name: "Lisa",
        },
        text: "Гарний пост!",
        createdAt: "2025-02-24T05:50:28.880317Z",
        views: 80,
        replies: [
          {
            id: 354,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Дякую за корисну інформацію.",
            createdAt: "2025-02-25T20:50:28.880337Z",
            views: 21,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 224,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "А де більше деталей?",
            createdAt: "2025-01-31T04:50:28.880344Z",
            views: 116,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 900,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Гарний пост!",
            createdAt: "2025-02-27T20:50:28.880356Z",
            views: 77,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 17,
    user: {
      id: 5,
      username: "lisa",
      avatar: "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
      name: "Lisa",
    },
    content: "Всі говорять про це, що ви думаєте?",
    likes: 73,
    views: 144,
    createdAt: "2025-01-30T23:50:28.880368Z",
    comments: [
      {
        id: 472,
        user: {
          id: 3,
          username: "mike",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
          name: "Mike",
        },
        text: "Чудово написано!",
        createdAt: "2025-02-26T03:50:28.880378Z",
        views: 100,
        replies: [
          {
            id: 270,
            user: {
              id: 5,
              username: "lisa",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/7.jpg",
              name: "Lisa",
            },
            text: "Вражаюче!",
            createdAt: "2025-01-31T03:50:28.880385Z",
            views: 134,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 382,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-11T10:50:28.880391Z",
            views: 67,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 546,
        user: {
          id: 3,
          username: "mike",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
          name: "Mike",
        },
        text: "Вражаюче!",
        createdAt: "2025-02-20T03:50:28.880397Z",
        views: 79,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 185,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Мені сподобалось.",
        createdAt: "2025-02-26T23:50:28.880403Z",
        views: 34,
        replies: [
          {
            id: 310,
            user: {
              id: 1,
              username: "bogdan",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
              name: "Bogdan",
            },
            text: "Цікава думка.",
            createdAt: "2025-02-09T22:50:28.880411Z",
            views: 80,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 18,
    user: {
      id: 1,
      username: "bogdan",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
      name: "Bogdan",
    },
    content: "Всі говорять про це, що ви думаєте?",
    likes: 66,
    views: 791,
    createdAt: "2025-01-30T20:50:28.880418Z",
    comments: [
      {
        id: 404,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Цікава думка.",
        createdAt: "2025-02-03T19:50:28.880424Z",
        views: 192,
        replies: [
          {
            id: 313,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Як цікаво!",
            createdAt: "2025-01-30T12:50:28.880439Z",
            views: 87,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 272,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Дякую за корисну інформацію.",
            createdAt: "2025-02-26T19:50:28.880445Z",
            views: 57,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 733,
        user: {
          id: 3,
          username: "mike",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
          name: "Mike",
        },
        text: "Чудово написано!",
        createdAt: "2025-02-06T15:50:28.880451Z",
        views: 95,
        replies: [
          {
            id: 664,
            user: {
              id: 3,
              username: "mike",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/male/9.jpg",
              name: "Mike",
            },
            text: "Згоден на всі 100%!",
            createdAt: "2025-02-01T08:50:28.880458Z",
            views: 198,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
          {
            id: 979,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Згоден на всі 100%!",
            createdAt: "2025-02-24T00:50:28.880463Z",
            views: 87,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
      {
        id: 495,
        user: {
          id: 2,
          username: "jane",
          avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
          name: "Jane",
        },
        text: "Мені сподобалось.",
        createdAt: "2025-02-09T12:50:28.880473Z",
        views: 141,
        replies: [],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 19,
    user: {
      id: 1,
      username: "bogdan",
      avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
      name: "Bogdan",
    },
    content: "Ділюсь своїми думками.",
    likes: 11,
    views: 617,
    createdAt: "2025-02-02T00:50:28.880480Z",
    comments: [
      {
        id: 273,
        user: {
          id: 1,
          username: "bogdan",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/19.jpg",
          name: "Bogdan",
        },
        text: "Вражаюче!",
        createdAt: "2025-02-09T21:50:28.880486Z",
        views: 40,
        replies: [
          {
            id: 225,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Не згоден, але поважаю вашу точку зору.",
            createdAt: "2025-02-05T08:50:28.880492Z",
            views: 143,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
  {
    id: 20,
    user: {
      id: 2,
      username: "jane",
      avatar: "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
      name: "Jane",
    },
    content: "Я щойно прочитав цікаву статтю.",
    likes: 11,
    views: 784,
    createdAt: "2025-02-08T14:50:28.880499Z",
    comments: [
      {
        id: 698,
        user: {
          id: 4,
          username: "alex",
          avatar: "https://xsgames.co/randomusers/assets/avatars/male/5.jpg",
          name: "Alex",
        },
        text: "Вражаюче!",
        createdAt: "2025-02-07T00:50:28.880505Z",
        views: 61,
        replies: [
          {
            id: 210,
            user: {
              id: 2,
              username: "jane",
              avatar:
                "https://xsgames.co/randomusers/assets/avatars/female/2.jpg",
              name: "Jane",
            },
            text: "Чудово написано!",
            createdAt: "2025-02-20T16:50:28.880511Z",
            views: 183,
            replies: [],
            likes: Math.floor(Math.random() * 100),
          },
        ],
        likes: Math.floor(Math.random() * 100),
      },
    ],
  },
];
export default posts;
