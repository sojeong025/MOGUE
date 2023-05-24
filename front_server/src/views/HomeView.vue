<template>
  <div id="video-container">
    <div class="container-except-video">
      <div class="main">
        <h1 class="mogue">MOGUE</h1>
        <router-link class="magazine" :to="{ name: 'movie' }">MOVIE MAGAGINE</router-link>
      </div>
    </div>
    <video id="home-video" src="/notebook.mp4" class="video" type="video/mp4" autoplay muted loop></video>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  created() {
    this.$store.dispatch('checkTextWhite', 'home')
  },
  destroyed() {
    this.$store.dispatch('checkTextWhite', 'else')
  }
}
</script>

<style scoped>
.container-except-video{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

#video-container{
  position:relative;
}

.main {
  top: 30%;
  position: absolute;
  /* z-index: 100; */
  text-align: center;
}

.mogue {
  color: #fff;
  font-size: 200px;
  font-weight: 600;
  transition: 0.5s;
  font-family: 'DM Serif Display', serif;
}

.mogue:hover {
  -webkit-text-stroke: 2px #fff;
  color: transparent;
}

.magazine{
  color: #fff;
  display: inline-block;
  font-size: 23px;
  border: 2px solid #fff;
  padding: 14px 7px;
  border-radius: 50px;
  margin: 20px 10px;
  font-family: 'DM Serif Display', serif;
}

#home-video {
  width: 100%;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: -1;
}

</style>