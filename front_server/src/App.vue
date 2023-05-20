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
        <router-link :to="{ name: 'profile' }"> Profile </router-link>
        <button @click="logout">Logout</button>
      </div>
    </nav>
    <router-link :to="{ name: 'community' }"> community </router-link>
    <router-link :to="{ name: 'movie' }"> movie </router-link>
    search
    <router-view @login="this.$store.state.isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isLogin: false,
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
  }
}
</script>


<style>
* {
  margin: 0px;
  padding: 0px;
}

</style>
