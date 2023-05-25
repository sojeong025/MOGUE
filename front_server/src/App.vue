<template>
  <div id="app">
    <!-- nav바 구현 -->
    <nav>
    <div id="nav-container">
        <div class="nav-left">
          <router-link :to="{ name: 'home' }" :class="{ 'textWhite': this.$store.state.textWhite }">
            <p class="logo" >MOGUE</p>
          </router-link>
        </div>

        <div class="nav-center">
            <router-link class="nav-font-size" :to="{ name: 'community' }" :class="{ 'textWhite': this.$store.state.textWhite }"> COMMUNITY </router-link>
            <router-link class="nav-font-size" :to="{ name: 'movie' }" :class="{ 'textWhite': this.$store.state.textWhite }"> MOVIE </router-link>
            <router-link class="nav-font-size" :to="{ name: 'search' }" :class="{ 'textWhite': this.$store.state.textWhite }">SEARCH</router-link>
        </div>

        <div class="nav-right">
          <div v-if="this.$store.state.isLogin" class="login-part">
            <router-link class="nav-font-size" :to="{ name: 'profile', params: { id: user_id } }" :class="{ 'textWhite': this.$store.state.textWhite }"> PROFILE </router-link>
            <span id="logout" :class="{ 'textWhite': this.$store.state.textWhite }" @click="logout">LOGOUT</span>
          </div>
          <div class="login-form nav-right" v-else>
            <span class="nav-item">
              <router-link class="nav-font-size" :to="{ name: 'signup' }" :class="{ 'textWhite': this.$store.state.textWhite }"> SIGNUP </router-link>
            </span>
            <span class="nav-item">
              <router-link class="nav-font-size" :to="{ name: 'login' }" :class="{ 'textWhite': this.$store.state.textWhite }"> LOGIN </router-link>
            </span>
          </div>
        </div>
      </div>
      </nav>
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
      scrollDirection: '',
      prevScrollPos: window.pageYOffset,
      navTop: 0,
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
  },
  destroyed() {
    this.logout()
  },
}
</script>


<style>
router-view {
  transition-duration: 3s;
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
  -webkit-user-selct: none;
  -moz-user-selct: none;
  -ms-user-selct: none;
  user-select: none;
  -webkit-user-drag: none;
}

*::-webkit-scrollbar{
    display: none;
}

/* .yellow {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;
  padding-top: 40px;
  padding-left: 50px;
  background-color: #e8aa23;
} */

#app {
  font-size: 18px;
  text-decoration: none;
}
a {
  font-size: 20px;
  text-decoration: none;
  color: black;
  padding: 0 20px 0;
}

nav{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100vw;
  height: 90px;
  position: sticky;
  border-bottom: 2px solid black;
}

#nav-container{
  display: flex;
  justify-content: space-between;
  width: 100%;
}
.logo{
  font-family: 'DM Serif Display', serif;
  font-size: 50px;
}

.nav-left{
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 500px;
  margin-left: 30px;
}

.nav-center{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
}

.nav-right{
  display: flex;
  justify-content: flex-end;
  align-items: center;
  width: 500px;
  margin-right: 30px;
}

#login{
  background-color: #e8aa23;
  border-radius: 10px;
  padding: 8px 8px; 
}

#logout {
  cursor: pointer;
  font-size: 26px;
}

.nav-font-size{
  font-size: 26px;
}


/* #nav-container{
  display: flex;
  justify-content: space-between;
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
  font-weight: 600;
}

#nav2 {
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: 600;
  margin: 10px 30px 0px;
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
*/

.login-part {
  margin-right: 30px;
}
</style>
