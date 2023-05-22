<template>
  <div id="video-container">
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

<style>
  #home-video {
    width: 100vw;
  }
</style>