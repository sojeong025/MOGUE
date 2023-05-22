<template>
    <router-link id="recommend-list-item" :to="{ name : 'moviedetail', params : { id: movie.id, movie: movie } }">
      <div id="poster">
        <div id="movie-title"><h2>{{ movie.title }}</h2></div>
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
  data() {
    return {
    }
  },
  methods: {
  }
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
    padding: 5px;
    align-items: center;
    position: absolute;
    width: 170px;
    height: 255px;
    color: rgba(255, 255, 255, 0);
    background-color: rgba(0, 0, 0, 0);
  }

  #movie-title:hover{
    transition-duration: 0.2s;
    color: white;
    background-color: rgba(0, 0, 0, 0.795);
  }

  #poster {
    display: flex;
    align-items: center;
    width: 180px;
  }

  #poster-img {
    display: flex;
    align-items: center;
    width: 180px;
    height: 265px;
  }
</style>