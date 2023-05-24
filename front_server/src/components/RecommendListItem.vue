<template>
    <router-link id="recommend-list-item" :to="{ name : 'moviedetail', params : { id: movie.id, movie: movie } }">
      <div id="poster">
        <div id="movie-title">
          <h5>{{ movie.title }} </h5>
          <p id="runtime">{{ movie.runtime }}분</p>
          <p id="recommend_overview">{{ movie.overview.slice(0,80) }}...</p>
        </div>
        <img id="poster-img" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
      </div>
    </router-link>
</template>

<script>
export default {
  name: 'RecommendListItemView',
  props: {
    movie: Object,
  },
}
</script>

<style>
  #recommend-list-item {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    padding: 0px;
    margin: 0px 25px;
    box-shadow: 8px 8px 10px 0px rgba(128, 128, 128, 0.432);
  }

  #movie-title {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    white-space: normal;
    padding: 28px;
    position: absolute;
    font-size: 30px;
    width: 174px;
    height: 294px;
    color: rgba(255, 255, 255, 0);
    background-color: rgba(0, 0, 0, 0);
  }

  #movie-title:hover{
    position: absolute;
    transition-duration: 0.2s;
    color: white;
    background-color: rgba(0, 0, 0, 0.795);
  }

  #poster {
    display: flex;
    align-items: flex-start;
    width: 230px;
  }

  #poster-img {
    width: 230px;
    height: 350px;
  }

  #recommend_overview {
    margin-top: 30px;
    font-size: 16px;
  }

  #runtime {
    font-size: 12px;
  }
</style>