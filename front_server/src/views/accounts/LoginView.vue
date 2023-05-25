<template>
  <div>
    <div class="container">
      <div class="forms-container">
        <div class="form-control login-form">
          <form id="login-form" @submit.prevent="login">
            <h2>Login</h2>
            <input type="text" placeholder="ID" v-model="user.username" required />
            <input type="password" placeholder="Password" v-model="user.password" required />
            <button>Login</button>
          </form>
          <div class="socials">
          <!-- <span>or login with</span> -->
            <i class="fab fa-facebook-f"></i>
            <i class="fab fa-google-plus-g"></i>
            <i class="fab fa-linkedin-in"></i>
          </div>
        </div>
        <div class="intro-control login-intro">
          <div class="intro-control__inner">
            <h2>Welcome back!</h2>
            <p>
              Welcome back! We are so happy to have you here. It's great to see you again. We hope you had a safe and enjoyable time away.
            </p>
          <router-link :to="{name: 'signup'}"><button id="signup-btn">No account yet? Signup.</button></router-link>
          </div>
        </div>
      </div>
    </div>
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
        this.$router.push({name: 'home'})
      })
      .catch(err => console.log(err))
    }
  }
}
</script>


<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 180px;
}
.forms-container {
  display: flex;
  max-width: 1000px;
  width: 100%;
}
.login-intro {
  flex: 1;
  background-color: #faf5db;
  padding: 80px 40px;
}
.login-form {
  flex: 1;
  background-color: #fff;
  padding: 80px 40px;
  margin-right: 20px;
}
.intro-control__inner {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}
h2 {
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
}
p {
  margin-bottom: 20px;
  word-break: keep-all;
  text-align: center;
}
input {
  width: 94%;
  padding: 10px;
  margin-bottom: 15px;
}
button {
  width: 100%;
  padding: 10px;
  background-color: #e8aa23;
  color: #fff;
  font-size: 17px;
  border: none;
  cursor: pointer;
  border-radius: 10px;
}
button:hover {
  background-color: #f3b541;
}
.socials {
  display: flex;
}
</style>