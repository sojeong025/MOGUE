<template>
  <div>
    <h1>MovieDetail</h1>
    <p>{{ movie.title }}</p>
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
    }
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/${this.$route.params.id}`
    })
    .then((res) => {
      this.movie = res.data
    })
    .catch(err => console.log(err))
  }
}
</script>

<style>

</style>