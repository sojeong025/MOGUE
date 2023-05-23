<template>
  <div id="movie">
    <div id="movie-headers">
    </div>
    <div id="movie-body">
      <div id="recommend-section">
        <RecommendList/>
      </div>
      <div id="collection-section">
        <h1>CollectionList</h1>
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
    margin-top: 50px;
  }

  #recommend-section {
    margin-top: 130px;
  }


</style>