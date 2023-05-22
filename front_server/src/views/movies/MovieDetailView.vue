<template>
  <div>
    <div id="movie-section">
      <img id="poster-img" :src="`https://image.tmdb.org/t/p/w780/${movie.poster_path}`" alt="poster">
      <h1>{{ movie.title }}</h1>
      <p>{{ movie.overview }}</p>
    </div>
    <div id="review-section">
      <p v-for="review in reviews" :key="review.id">{{ review.content }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  data() {
    return {
      movie: Object,
      reviews: Object,
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/${this.$route.params.id}`
    })
    .then((res) => {
      console.log(res)
      this.movie = res.data.movie
      this.reviews = res.data.reviews
    })
    .catch(err => console.log(err))
  }
}
</script>

<style scoped>
  #poster-img {
    display: flex;
    width: 300px;
    height: 480px;
  }

  #movie-section {
    
  }
</style>