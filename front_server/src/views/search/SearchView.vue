<template>
  <div id="search-section">
    <div id="search-headers">
      <div id="search">
        <input id="search-input" 
        type="text" placeholder="작품명을 검색해보세요." 
        v-model="searchInput" 
        @input="search(searchInput, movies)"
        @keydown="focusMove"
        >
      </div>
      <div id="search-body">
        <div id = "search-result">
          <div id="search-recommend-section" v-if="!searchInput">
            <RecommendList/>
          </div>
            <router-link id="recommend-list-item" :to="{ name : 'moviedetail', params : { id: movie.id, movie: movie } }" v-for="movie in searchResult.slice(0, 5)" :key="movie.id" :class="{ 'focus': index === focus }" @keyup.enter="selectResult(movie.title)">
              <div id="poster">
                <div id="movie-title">
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
    focusMove(event) {
      switch (event.keyCode) {
        case 38:
          if (this.focus === null) {
            this.focus = 0
          } else if (this.focus > 0) {
            this.focus--
          }
          break
        case 40:
          if (this.focus === null) {
            this.focus = 0
          } else if (this.focus < this.items.length - 1) {
            this.focus++
          }
          break;
      }
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
    margin-top: 120px;
  }
    
  #search-headers{
    display: flex;
    flex-direction: column;
    width: 800px;
    margin-bottom: 50px;
  }

  #search {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    position: relative;
    width: 300px;
  }

  #search-input {
    display: flex;
    padding: 10px;
    margin-top: 10px;
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
    align-items: flex-end;
    width: 100vw;
    height: 370px;
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
    height: 380px;
    display: flex;
    margin-top: 50px;
    overflow: auto;
    white-space: nowrap;
  }
</style>