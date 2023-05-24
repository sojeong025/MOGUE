<template>
  <div id="movie">
    <div id="movie-headers">
      <img id="movie-main-image" :src="`http://127.0.0.1:8000/자전거배너.jpg`" alt="">
    </div>
    <div id="movie-body">
      <div class="box1"></div>
      <div id="recommend-section">
        <h1>| TODAY'S MOVIE</h1>
        <RecommendList/>
      </div>
      <div class="box2"></div>
      <div class="yellow recommend-section">
        <h1>| HOW ABOUT THIS?</h1>
        <RecommendList/>
      </div>
      <div id="collection-section">
        <CollectionList/>
      </div>
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

<style scoped>
  .box1{
    width: 109.9vw;
    height: 300px;
    background-color:#dededc77;
    position:absolute;
    top:10%;
    left:-10%
  }

  .box2{
    width: 109.9vw;
    height: 300px;
    background-color:#dededc77;
    position:absolute;
    top:35.5%;
    left:-10%
  }

  .video {
    width: 100%;
  }

  h1{
    font-size: 28px;
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

  #movie-body{
    margin-top: 90px;
    position: relative;
  }

  #collection-section {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    margin-top: 80px;
    width: 100%;
    height: 1000px;
  }

  #recommend-section {
    margin-top: 50px;
    margin-left: 50px;
  }

  .recommend-section {
    margin-top: 50px;
    margin-left: 50px;
  }

  #movie-main-image {
    width: 100%;
    height: 100%;
  }


</style>