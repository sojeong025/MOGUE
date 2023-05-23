<template>
  <div id="search-section">
      <img id="movie-main-image" :src="`http://127.0.0.1:8000/media/버스.jpg`" alt="">
    <div id="search-headers">
      <div id="search">
        <input id="search-input" 
        type="text" placeholder="작품명을 검색해보세요." 
        v-model="searchInput" 
        @input="search(searchInput, movies)"
        >
      </div>
      <div id="search-body">
        <div id = "search-result">
          <div id="search-recommend-section" v-if="!searchInput">
            <RecommendList/>
          </div>
          <router-link id="search-recommend-list-item" :to="{ name : 'moviedetail', params : { id: movie.id, movie: movie } }" v-for="movie in searchResult.slice(0, 5)" :key="movie.id" :class="{ 'focus': index === focus }" @keyup.enter="selectResult(movie.title)">
            <div id="poster">
              <div id="search-movie-title">
                <h5>{{ movie.title }} </h5>
                <p id="runtime">{{ movie.runtime }}분</p>
                <p id="recommend_overview">{{ movie.overview.slice(0, 66) }}...</p>
              </div>
              <img id="poster-img" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
            </div>
          </router-link>
          </div>
        </div>
      </div>
    <div id="search-collection-section">
      <p>이런 컬렉션은 어때요? </p>
      <CollectionList/>
    </div>
  </div>
</template>

<script>
import CollectionList from '@/components/CollectionList'
import RecommendList from '@/components/RecommendList'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'SearchView',
  data() {
    return {
      movies: [],
      searchResult: [],
      searchInput: "",
      focus: null,
    }
  },
  components: {
    RecommendList,
    CollectionList,
  },
  methods: {
    Back(){
      this.$router.go(-1)
    },
    search(wordToMatch, movies) {
      const value = wordToMatch.trim()
      const movieMatchDataList = value ? movies.filter(movie => movie.title.includes(value)) : []
      this.searchResult = movieMatchDataList
    },
    selectResult(title) {
      this.searchInput = title
    }
  },
    created() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/all_movies`
    })
    .then((res) => {
      this.movies = res.data
    })
    .catch(err => console.log(err))
  }
}
</script>

<style>
  #search-section {
  }
    
  #search-headers{
    display: flex;
    flex-direction: column;
    align-content: space-between;
    width: 100%px;
    margin-top: 80px;
    margin-left: 50px;
  }

  #search {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    position: relative;
    width: 300px;
  }

  #search-body {
    display: flex;
    flex-direction: column;
    justify-content: start;
  }

  #search-input {
    display: flex;
    padding: 10px;
    margin-top: 10px;
    margin-bottom: 45px;
    width: 230px;
    height: 20px;
    border: 1px solid #bbb;
    border-radius: 8px;
    font-size: 14px;
  }

  #search-input:hover {
    border: 1px solid #008cff;
    transition-duration: 0.3s;
  }

  #search-result{
    display: flex;
    align-items: center;
    width: 100vw;
    height: 400px;
  }

  #search-result-item{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-top: 5px;
  }

  #search-collection-section{
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  #search-recommend-section {
    display: flex;
    align-items: flex-end;
    height: 440px;
    display: flex;
    margin-top: 20px;
    overflow: auto;
    white-space: nowrap;
  }

  #search-recommend-list-item {
    display: flex;
    position: relative;
    flex-direction: column;
    text-decoration: none;
    height: 410px;
    margin-right: 30px;
  }

  #search-recommend-list-item:hover {
    height: 422px;
  }

  #search-movie-title {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    white-space: normal;
    padding: 28px;
    position: absolute;
    font-size: 30px;
    width: 174px;
    height: 294px;
    color: rgba(255, 255, 255, 0);
    background-color: rgba(0, 0, 0, 0);
  }

  #search-movie-title:hover{
    position: absolute;
    bottom: 17%;
    transition-duration: 0.2s;
    color: white;
    background-color: rgba(0, 0, 0, 0.795);
  }
</style>