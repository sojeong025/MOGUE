<template>
  <div>
    <h1>Movie</h1>
    <div id="main-video">
      <video src="/notebook.mp4" class="video"
      type="video/mp4" autoplay muted loop></video>
    </div>
    <div id="collection-list">
      <RecommendList/>
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
  height: 500px;
}
</style>