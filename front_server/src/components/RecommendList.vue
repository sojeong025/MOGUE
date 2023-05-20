<template>
  <div>
    <h1>RecommendList</h1>
    <RecommendListItem
    v-for="movie in movies" :key="movie.id" />
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import RecommendListItem from './RecommendListItem'

export default {
  name: 'RecommendList',
  components: {
    RecommendListItem,
  },
  data(){
    return {
      movies: [],
      page: Number,
    }
  },
  created(){
    this.getRecommends()
  },
  methods: {
    getRecommends(){
      axios({
        method: 'get',
        url: `${API_URL}/recommends/${this.page}`
      })
      .then((res) => {
        this.recommends = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>