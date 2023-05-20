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
      </div>
    </nav>
    community
    movie
    search
    <router-view/>
  </div>
</template>

<style>
* {
  margin: 0px;
  padding: 0px;
}
</style>
