<template>
  <div>
    <h1>CollectionDetail</h1>
    <p v-for="movie in movies" :key="movie.id" :movie="movie"></p>
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
      url: `${API_URL}/collections/${this.$route.params.id}`
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

</style>