<template>
    <div class="container">
      <div class="forms-container">
        <div class="form-control signup-form">
          <form class="signup-form" @submit.prevent="signUp">
            <h2>Signup</h2>
            <input type="text" placeholder="ID" v-model="user.username" required />
            <input type="text" placeholder="NickName" v-model="user.nickname" required />
            <input type="password" placeholder="Password" v-model="user.password" required />
            <input type="password" placeholder="Confirm password" v-model="user.passwordConfirmation" required />
            <button class="signup-btn">Signup</button>
          </form>
          <div class="socials">
          <!-- <span>or signup with</span> -->
            <i class="fab fa-facebook-f"></i>
            <i class="fab fa-google-plus-g"></i>
            <i class="fab fa-linkedin-in"></i>
          </div>
        </div>
        <div class="intro-control signup-intro">
          <div class="intro-control__inner">
            <h2>Come join us!</h2>
            <p>
              We are so excited to have you here. If you haven't already, create an account to get access to exclusive offers, rewards, and discounts.
            </p>
            <router-link :to="{ name: 'login' }"><button id="signin-btn">Already have an account? Login.</button></router-link>
          </div>
        </div>
      </div>
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
      .catch(err => alert(err.response.data.error))
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

.signup-intro {
  display: flex;
  flex-direction: column;
  width: 400px;
  height: 400px;
  background-color: #faf5db;
  padding: 40px;
}

.signup-form {
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

p{
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
  width: 300px;
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

.signup-btn {
  width: 120px;
}
</style>