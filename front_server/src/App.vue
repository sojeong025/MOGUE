<template>
  <div id="app">
    <!-- nav바 구현 -->
    <div id="nav-container">
      <nav>
        <div id="nav1">
          <div id="logo-container">
            <div class="nav-item">
              <router-link :to="{ name: 'home' }" >
                <h1 :class="{ 'textWhite': this.$store.state.textWhite }">LOGO</h1>
              </router-link>
            </div>
          </div>
          <div v-if="this.$store.state.isLogin" class="login-part">
            <router-link :to="{ name: 'profile', params: { id: user_id } }" :class="{ 'textWhite': this.$store.state.textWhite }"> Profile </router-link>
            <span id="logout" :class="{ 'textWhite': this.$store.state.textWhite }" @click="logout">Logout</span>
          </div>
          <div class="login-form" v-else>
            <span class="nav-item">
              <router-link :to="{ name: 'login' }" :class="{ 'textWhite': this.$store.state.textWhite }"> Login </router-link>
            </span>
            <span class="nav-item">
              <router-link :to="{ name: 'signup' }" :class="{ 'textWhite': this.$store.state.textWhite }"> Signup </router-link>
            </span>
          </div>
        </div>
      </nav>
      <div id="nav2">
        <div class="nav-item">
          <router-link :to="{ name: 'community' }" :class="{ 'textWhite': this.$store.state.textWhite }"> community </router-link>
        </div>
        <div class="nav-item">
          <router-link :to="{ name: 'movie' }" :class="{ 'textWhite': this.$store.state.textWhite }"> movie </router-link>
        </div>
        <div class="nav-item">
          <router-link :to="{ name: 'search' }" :class="{ 'textWhite': this.$store.state.textWhite }">search</router-link>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import jwtDecode from "jwt-decode"
const token = localStorage.getItem('token')

export default {
  name: 'App',
  data() {
    return {
      user_id: jwtDecode(token).user_id,
      textWhite: false,
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token')
      this.$store.dispatch('checkLogin')
      if (this.$route.name !== 'home') {
        this.$router.push({ name: 'home' })
      }
    },
  },
  created(){
    if (localStorage.getItem('token')) {
      console.log('로그인 돼있음')
    } else {
      console.log('로그인 안돼있음')
    }
    this.$store.dispatch('checkLogin')
    this.$store.dispatch('checkTextWhite')
  }
}
</script>


<style>
  router-view {
    transition-duration: 3px;
  }

  @font-face {
    font-family: 'SUITE-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
  }

  * {
    margin: 0px;
    padding: 0px;
    word-break: break-all;
    font-family: 'Montserrat', 'sans-serif', 'SUITE-Regular';
  }

  h1 {
    font-size: 40px;
  }

  *::-webkit-scrollbar{
      display: none;
  }

  .yellow {
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: white;
    padding-top: 40px;
    padding-left: 50px;
    background-color: #ffca1c;
  }

  #app {
    font-size: 18px;
    text-decoration: none;
  }

  a {
    font-size: 24px;
    text-decoration: none;
    color: black;
  }

  #logout {
    cursor: pointer;
    font-size: 24px;
  }

  #nav-container{
    position: fixed;
    padding: 20px;
    top: 0%;
    width: 100%;
    z-index: 1000;
  }

  #nav1 {
    width: 100%;
    display: flex;
    justify-content: space-between;
    font-size: 18px;
  }

  #nav2 {
    display: flex;
    justify-content: space-between;
    font-size: 18px;
    margin-top: 10px;
  }

  .textWhite {
    color: #ffffff;
  }

  .nav-item {
    display: flex;
    justify-content: center;
    width: 150px;
  }

  .login-form {
    display: flex;
    width: 302px;
  }

  .login-part {
    padding-right: 50px;
  }
</style>
