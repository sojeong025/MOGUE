<template>
  <div id="video-container">
    <div class="container-except-video">
      <div class="main">
        <h1 class="mogue">MOGUE</h1>
        <router-link class="magazine" :to="{ name: 'movie' }">MOVIE MAGAGINE</router-link>
      </div>
    </div>
    <video id="home-video" src="/finalback.mp4" class="video" type="video/mp4" autoplay muted loop></video>
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
  margin-top: 850px;
  position: absolute;
  /* z-index: 100; */
  text-align: center;
}

.mogue {
  color: #fff;
  font-size: 150px;
  font-weight: 600;
  transition: 0.5s;
  font-family: 'DM Serif Display', serif;
}
.mogue:hover {
  -webkit-text-stroke: 1px #fff;
  color: transparent;
}

.magazine:hover{
  background: rgba(255, 255, 255, 0.692);
  color: #000;
  /* border: 2px solid black */
}

.magazine{
  color: #fff;
  display: inline-block;
  font-size: 25px;
  border: 2px solid #fff;
  padding: 14px 25px;
  border-radius: 50px;
  margin: 10px 10px;
  font-family: 'DM Serif Display', serif;
}



#home-video {
  position: absolute;
  /* display: flex; */
  /* align-items: center;
  justify-content: center; */
  z-index: -1;
  width: 1921px;
  height: 877px;
}

</style>