<template>
  <div id="login-section">
    <h1>Login Page</h1>
    <form id="login-form" @submit.prevent="login">
      <input type="text" v-model="user.username" placeholder="ID">
      <input type="password" v-model="user.password" placeholder="PW">
      <input type="submit" value="LOGIN">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      user: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: this.user
      })
      .then(res => {
        const token = res.data.token;
        this.$store.dispatch('login', token)
        console.log(this.$router.pop)
        this.$router.go(-1)
      })
    }
  }
}
</script>

<style>
  #login-section {
    margin: 130px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  #login-form {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>