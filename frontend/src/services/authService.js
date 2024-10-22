import api from './axios';

const AuthService = {
  login(credentials) {
    return api.post('token/', credentials)
      .then(response => {
        if (response.data.access && response.data.refresh) {
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
        }
        return response.data;
      });
  },

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
  },

  refreshToken() {
    const refresh_token = localStorage.getItem('refresh_token');
    localStorage.setItem('access_token', refresh_token.data.access);
  }
};

export default AuthService;
