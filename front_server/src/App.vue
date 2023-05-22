<template>
  <div id="app">
    <!-- nav바 구현 -->
    <nav>
      <div id="nav1">
        <div id="logo-container">
          <router-link :to="{ name: 'home' }">
            Logo
          </router-link>
        </div>
        <router-link :to="{ name: 'login' }"> Login </router-link>
        <router-link :to="{ name: 'signup' }"> Signup </router-link>
        <router-link :to="{ name: 'profile', params: { id: this.user_id } }"> Profile </router-link>
        <button @click="logout">Logout</button>
      </div>
    </nav>
    <router-link :to="{ name: 'community' }"> community </router-link>
    <router-link :to="{ name: 'movie' }"> movie </router-link>
    search
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
      user_id: jwtDecode(token).user_id
    }
  },
  methods: {
    logout() {
      this.isLogin = false
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      if (this.$router.name !== 'home') {
        this.$router.push({ name: 'home' })
      }
    }
  },
  created(){
    if (localStorage.getItem('token')) {
      console.log('로그인 돼있음')
    } else {
      console.log('로그인 안돼있음')
    }
  }
}
</script>


<style>
* {
  margin: 0px;
  padding: 0px;
}

</style>
