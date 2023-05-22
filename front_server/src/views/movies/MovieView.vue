<template>
  <div id="movie">
    <div id="home-video">
        <div class="top"></div>
        <div class="bottom"></div>
      <video src="/notebook.mp4" class="video"
      type="video/mp4" autoplay muted loop></video>
    </div>
    <RecommendList/>
    <div id="collection-section">
      <h1>CollectionList</h1>
      <CollectionList/>
    </div>
  </div>
</template>

<script>
import RecommendList from '@/components/RecommendList'
import CollectionList from '@/components/CollectionList'


export default {
  name: 'MovieView',
  components: {
    RecommendList,
    CollectionList,
  }
}
</script>

<style>
  .video {
    width: 100%;
  }

  #home-video {
    position: relative;
  }

  #home-video .top {
    position: absolute;
    top: 0%;
    width: 100%;
    height: 60px;
    background: linear-gradient(to top, transparent, #ffffff);
  }

  #home-video .bottom {
    position: absolute;
    bottom: 0%;
    width: 100%;
    height: 60px;
    background: linear-gradient(to bottom, transparent, #ffffff);
  }

  #collection-section {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }
</style>