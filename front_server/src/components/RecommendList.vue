<template>
  <div id="recommend-container">
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
const _ = require('lodash');

import RecommendListItem from './RecommendListItem'

export default {
  name: 'RecommendList',
  components: {
    RecommendListItem,
  },
  data(){
    return {
      movies: [],
      page: _.sample([0, 1, 2, 3, 4])
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
        console.log(res)
        this.movies = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>
  #recommend-container{
    height: 450px;
  }

  #recommend-list{
    /* border: 1px red solid; */
    display: flex;
    align-items: flex-end;
    height: 360px;
    display: flex;
    margin-top: 20px;
    overflow: auto;
    white-space: nowrap;
  }

  #recommend-list::-webkit-scrollbar{
    display: none; 
}
</style>