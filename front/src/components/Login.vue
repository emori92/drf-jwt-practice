<template>
  <div class="login">
    <h1>Login</h1>
    <p>
      <label for="username">username</label>
      <input type="text" v-model="username">
    </p>
    <p>
      <label for="password">password</label>
      <input type="password" v-model="password">
    </p>
    <p>
      <button @click="userLogin">Login</button>
    </p>
  </div>
</template>

<script>
export default {
  // component
  username: "login",
  // data
  data() {
    return {
      username: "",
      password: ""
    };
  },
  // method
  methods: {
    // login
    userLogin: async function() {
      // create JWT token
      const back = 'http://localhost:8000';
      const jwt = back + '/auth/jwt/create/'
      const user = { username: this.username, password: this.password };
      const response = await this.$http.post(jwt, user);
      // set JWT to head
      this.$http.interceptors.request.use(
        // 200
        req => {
          req.headers.Authorization = 'JWT ' + response.data.access;
          return req;
        },
        // error
        error => { return error; }
      );
      // request my info
      const myUser = back + '/auth/users/me/';
      const info = await this.$http.get(myUser);
      console.table(info.data);
    }
  }
};
</script>
