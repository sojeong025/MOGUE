<template>
  <div id="collection-detail">
    <h1>{{ collection.title }}</h1>
    <div id="collection-movie-list">
      <div id="collection-movie-item" v-for="movie in movies" :key="movie.id" :movie="movie">
        <router-link :to="{ name:'moviedetail', params: { id: movie.id } }">
          <div id="movie-title"><h2>{{ movie.title }}</h2></div>
          <img id="poster-img" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
        </router-link>
      </div>
    </div>
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
</style>