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
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.user
      })
      .then(res => {
        console.log(res.data)
        localStorage.setItem('token', res.data.token)
        localStorage.setItem('user', res.data)
        this.$emit('login')
        this.$router.push({ name: 'home' })
      })
    }
  }
}
</script>

<style>

</style>