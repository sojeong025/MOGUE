<template>
  <div class="container">
    <div class="forms-container">
      <div class="form-control login-form">
        <form class="login-form" @submit.prevent="login">
          <h2>Login</h2>
          <input type="text" placeholder="ID" v-model="user.username" required />
          <input type="password" placeholder="Password" v-model="user.password" required />
          <button class="login-btn">Login</button>
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
      .catch(err => alert(err.response.data.non_field_errors))
    }
  }
}
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 90vh;
}
.forms-container {
  display: flex;
  max-width: 1000px;
  width: 100%;
}
.login-intro {
  display: flex;
  flex-direction: column;
  width: 400px;
  height: 400px;
  background-color: #faf5db;
  padding: 40px;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 400px;
  height: 400px;
  padding: 40px;
  background-color: #fff;

}
.intro-control__inner {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}

h2 {
  font-size: 36px;
  margin-bottom: 20px;
  text-align: center;
  font-weight: 100;
}
p {
  margin-bottom: 20px;
  word-break: keep-all;
  text-align: center;
  line-height: 26px;
}
input {
  width: 94%;
  padding: 10px;
  margin-bottom: 22px;
  font-size: 16px;
}
button {
  width: 240px;
  padding: 10px;
  background-color: #e8aa23;
  color: #fff;
  font-size: 17px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}
button:hover {
  background-color: rgb(255, 190, 48);
}
.socials {
  display: flex;
}

.login-btn {
  width: 120px;
}

</style>