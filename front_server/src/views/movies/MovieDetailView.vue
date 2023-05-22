<template>
  <div>
    <div id="movie-section">
      <img id="poster-img" :src="`https://image.tmdb.org/t/p/w780/${movie.poster_path}`" alt="poster">
      <div id="detail-info">
        <h1 id="detail-title">{{ movie.title }} <span id="movie-runtime">{{ movie.runtime }}분</span></h1>
        <p id="detail-overview">{{ movie.overview.slice(0,150) }}</p>
      </div>
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
    display: flex;
    align-items: flex-end;
  }

  #movie-runtime {
    font-size: 16px;
  }

  #detail-overview {
    width: 500px;
    margin-top: 30px;
  }

  #detail-info {
    margin-left: 18px;
  }
</style>