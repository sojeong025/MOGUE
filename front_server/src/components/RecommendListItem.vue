<template>
    <router-link id="recommend-list-item" :to="{ name : 'moviedetail', params : { id: movie.id, movie: movie } }">
      <div id="poster">
        <div id="movie-title">
          <h3>{{ movie.title }} </h3>
          <p id="runtime">{{ movie.runtime }}분</p>
          <p id="recommend_overview">{{ movie.overview.slice(0, 66) }}...</p>
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
    margin-right: 20px;
  }

  #movie-title {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    white-space: normal;
    padding: 15px;
    position: absolute;
    width: 150px;
    height: 235px;
    color: rgba(255, 255, 255, 0);
    background-color: rgba(0, 0, 0, 0);
  }

  #movie-title:hover{
    position: absolute;
    bottom: 5%;
    transition-duration: 0.2s;
    color: white;
    background-color: rgba(0, 0, 0, 0.795);
  }

  #poster {
    display: flex;
    align-items: center;
    width: 180px;
  }

  #poster:hover {
    transition-duration: 10s;
    height: 295px;
  }

  #poster-img {
    display: flex;
    align-items: center;
    width: 180px;
    height: 265px;
  }


  #recommend_overview {
    font-size: 16px;
  }

  #runtime {
    font-size: 12px;
  }
</style>