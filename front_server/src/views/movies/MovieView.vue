<template>
  <div id="movie">
    <div id="movie-headers">
      <img id="movie-main-image" :src="`http://127.0.0.1:8000/자전거배너.jpg`" alt="">
    </div>
    <div id="movie-body">
      <!-- <div class="box1"></div> -->
        <div class="recommend-section">
        <div>
          <h1 class="today">| TODAY'S<br>&nbsp; MOVIE</h1>
        </div>
          <RecommendList/>
        </div>

        <div class="recommend-section">
        <div class="box2"></div>
        <div>
          <h1 class="today">| HOW<br>&nbsp; ABOUT<br>&nbsp; THIS?</h1>
        </div>
          <RecommendList/>
        </div>
      <div id="collection-section">
        <div class="collection-section-title">
          <h1>COLLECTIONS</h1>
        </div>
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
  .collection-section-title{
    display: flex;
    width: 1260px;
    margin-bottom: 20px;
  }

  .collection-section-title h1{
    font-size: 40px;
    font-weight: 100;
  }

  .recommend-section-box{
    display: flex;
  }
  
  .box2{
    width: 109.9vw;
    height: 300px;
    background-color:#dededc77;
    position:absolute;
    top:30%;
    left:-10%;
    z-index: -1;
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

  .recommend-section {
    display: flex;
    position: relative;
    margin-top: 50px;
    margin-left: 40px;
  }

  #movie-main-image {
    width: 100%;
    height: 100%;
  }

  .today{
    word-wrap : brek-word;
    width: 140px;
    font-weight: 100;
    font-size: 28px;
  }

</style>