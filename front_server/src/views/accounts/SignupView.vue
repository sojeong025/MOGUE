<template>
  <div>
    <h1>Singup Page</h1>
    <form id="signup-form" @submit.prevent="signUp">
      <label for="username"> 아이디 : </label>
      <input type="text" placeholder="ID" v-model="user.username">
      <button>중복 확인</button><br>

      <label for="nickname"> 닉네임 : </label>
      <input type="text" placeholder="nickname" v-model="user.nickname">

      <label for="password"> 비밀번호 : </label>
      <input type="password" id="password" v-model="user.password"><br>

      <label for="password2"> 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="user.passwordConfirmation"><br>

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignupView',
  data() {
    return {
      user: {
        username: null,
        nickname: null,
        password: "",
        passwordConfirmation: "",
      },

    }
  },
  methods: {
    signUp() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.user
      })
      .then(() => {
        this.$router.push({ name: 'login'})
      })
    }
  }
}
</script>

<style>

</style>