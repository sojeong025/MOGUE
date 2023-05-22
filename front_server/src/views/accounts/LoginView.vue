<template>
  <div>
    <h1>Login Page</h1>
    <form @submit.prevent="login">
      <input type="text" v-model="user.username"> <br>
      <input type="password" v-model="user.password">
      <input type="submit" value="로그인">
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
        this.$router.go(-1)
      })
    }
  }
}
</script>

<style>

</style>