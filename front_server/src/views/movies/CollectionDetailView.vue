<template>
  <div id="collection-detail">
    <h1>{{ collection.title }}</h1>
    <div id="collection-movie-list">
      <div id="collection-movie-item" v-for="movie in movies" :key="movie.id" :movie="movie">
        <router-link :to="{ name:'moviedetail', params: { id: movie.id } }">
          <div id="poster">
            <div id="collection-movie-title"><h2>{{ movie.title }}</h2></div>
            <img id="poster-img" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
          </div>
        </router-link>
      </div>
    </div>s
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CollectionDetailView',
  data() {
    return {
      collection : Object,
      movies : [],
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/collections/${this.$route.params.id}`
    })
    .then((res) => {
      this.collection = res.data.collection
      this.movies = res.data.movies
    })
    .catch(err => console.log(err))
  }
}
</script>

<style>
  #collection-detail {
    margin-top: 130px;
  }

  #collection-movie-list {
    display: flex;
  }

  #collection-movie-item {
    margin-right: 20px;
  }

  #collection-movie-title{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    white-space: normal;
    padding: 15px;
    position: absolute;
    width: 200px;
    height: 320px;
    color: rgba(255, 255, 255, 0);
    background-color: rgba(0, 0, 0, 0);
  }

  #collection-movie-title:hover{
    position: absolute;
    bottom: 5%;
    transition-duration: 0.2s;
    color: white;
    background-color: rgba(0, 0, 0, 0.795);
  }

  #poster {
    display: flex;
    align-items: flex-start;
    width: 230px;
  }

  #poster:hover {
    height: 368px;
  }

</style>