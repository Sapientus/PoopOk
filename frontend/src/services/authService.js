import api from "./axios";

const AuthService = {
  async logIn(credentials) {
    const data = new URLSearchParams();
    data.append("username", credentials.username);
    data.append("password", credentials.password);
    return await api
      .post("/api/auth/login", data, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
      .then((response) => {
        if (
          response.data &&
          response.data.token.access_token &&
          response.data.token.refresh_token
        ) {
          localStorage.setItem("access_token", response.data.access_token);
          localStorage.setItem("refresh_token", response.data.refresh_token);
        }
        return response.data;
      })
      .catch((error) => {
        return Promise.reject(error);
      });
  },

  logOut() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
  },

  refreshToken() {
    const response = localStorage.getItem("refresh_token");
    localStorage.setItem("access_token", response.data.access);
  },

  async signUp(credentials) {
    return await api
      .post("/api/auth/signup", credentials)
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        return Promise.reject(error);
      });
  },
};

export default AuthService;
