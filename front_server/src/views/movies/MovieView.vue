<template>
  <div id="movie">
    <div id="movie-headers">
      <img id="movie-main-image" :src="`http://127.0.0.1:8000/자전거배너.jpg`" alt="">
    </div>
    <div id="movie-body">
      <!-- <div class="box1"></div> -->
        <div class="recommend-section">
        <div>
          <h1 class="today">| TODAY'S<br>&nbsp; MOVIES</h1>
        </div>
          <RecommendList/>
        </div>

        <div class="recommend-section">
        <div class="box2"></div>
        <div>
          <h1 class="today">| LATEST<br>&nbsp; MOVIES</h1>
        </div>
          <LatestList/>
        </div>
      <div id="collection-section">
        <div class="collection-section-title">
          <h1>COLLECTIONS</h1>
        </div>
        <CollectionList/>
      </div>
    </div>
    <FooterSection/>
  </div>
</template>

<script>
import RecommendList from '@/components/RecommendList'
import CollectionList from '@/components/CollectionList'
import LatestList from '../../components/LatestList'
import FooterSection from '../../components/FooterSection'


export default {
  name: 'MovieView',
  components: {
    RecommendList,
    CollectionList,
    LatestList,
    FooterSection,
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
    font-size: 40px !important;
    font-weight: 100;
  }

  .recommend-section-box{
    display: flex;
  }
  
  .box2{
    width: 107.7vw;
    height: 300px;
    background-color:#dededc77;
    position:absolute;
    top:-10%;
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
    width: 100%;
    height: 1000px;
    margin-top: 80px;
    margin-bottom: -100px;
  }

  .collection-section-title h1{
    font-size: 25px;
  }

  .recommend-section {
    display: flex;
    position: relative;
    margin-top: 50px;
    margin-left: 40px;
  }

  #movie-main-image {
  width: 2133px;
  height: 680px;
  }

  .today{
    word-wrap : break-word;
    width: 140px;
    font-weight: 100;
    font-size: 28px;
  }

</style>