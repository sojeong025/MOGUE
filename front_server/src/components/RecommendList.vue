<template>
  <div>
    <h1>요즘 뜨는 영화</h1>
    <div id="recommend-list">
      <RecommendListItem
      id="recommend-list-item"
      v-for="movie in movies" 
      :key="movie.id" 
      :movie="movie"/>
    </div>
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
      page: 1,
    }
  },
  created(){
    this.getRecommends()
  },
  methods: {
    getRecommends(){
      axios({
        method: 'get',
        url: `${API_URL}/movies/recommends/${this.page}`
      })
      .then((res) => {
        this.movies = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>
  #recommend-list{
    display: flex;
    margin-top: 20px;
    overflow: auto;
    white-space: nowrap;
  }

  #recommend-list::-webkit-scrollbar{
    display: none; 
}
</style>