<template>
  <div id="app">
    <!-- nav바 구현 -->
    <nav>
      <div id="nav1">
        <div id="logo-container">
          <router-link :to="{ name: 'home' }">
            <h1>LOGO</h1>
          </router-link>
        </div>
        <div v-if="this.$store.state.isLogin">
          <router-link :to="{ name: 'profile', params: { id: user_id } }"> Profile </router-link>
          <button @click="logout">Logout</button>
        </div>
        <div v-else>
          <router-link :to="{ name: 'login' }"> Login </router-link>
          <router-link :to="{ name: 'signup' }"> Signup </router-link>
        </div>
      </div>
    </nav>
    <div id="nav2">
      <router-link :to="{ name: 'community' }"> community </router-link>
      <router-link :to="{ name: 'movie' }"> movie </router-link>
      search
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
  }
}
</script>


<style>
  * {
    margin: 0px;
    padding: 0px;
    word-break: break-all;
  }

  *::-webkit-scrollbar{
      display: none;
  }

  #app {
    font-size: 18px;
    text-decoration: none;
  }

  a {
    font-size: 18px;
    text-decoration: none;
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
  }

</style>
