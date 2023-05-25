<template>
  <div id="search-section">
    <img id="movie-main-image" :src="`http://127.0.0.1:8000/버스.jpg`" alt="">
    <div id="search-headers">
      <div id="search">
        <input id="search-input" type="text" placeholder="작품명을 검색해보세요." v-model="searchInput" @keydown="search(searchInput, movies)">
        <div class="otts">
          <div v-for="ott in otts" :key="ott.id">
            <div class="light-box" @click="filterOtt(ott.id)"></div>
            <img v-if="isSelected[ott.id]" class="ott-item" :src="`http://127.0.0.1:8000/watchprovidericon${ott.logo_path}color.png`" alt="">
            <img v-else class="ott-item" :src="`http://127.0.0.1:8000/watchprovidericon${ott.logo_path}mono.png`" alt="">
          </div>
        </div>
      </div>
    </div>
    <div id="search-body">
      <div id="search-result">
        <div class="search-results-title">
          <h1 class="today">| MOVIES</h1>
        </div>
        <div id="search-recommend-section" v-if="!searchResult.length">
          <RecommendList/>
        </div>
        <div id="search-recommend-list" v-else>
          <router-link id="search-recommend-list-item" :to="{ name : 'moviedetail', params : { id: movie.id, movie: movie } }" v-for="movie in searchResult.slice(0, 10)" :key="movie.id" @keyup.enter="selectResult(movie.title)">
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
      <div class="section-title">
        <div id="user-search">
          <input id="search-input" type="text" placeholder="닉네임을 검색해보세요." v-model="searchUserInput" @keydown="searchUser(searchUserInput, users)">
          <div id="search-result">
            <div class="search-results-title">
              <h1 class="user-today">| USERS</h1>
            </div>
            <div id="search-user-list" v-if="userResult.length > 0">
              <router-link class="user-search-item" v-for="user in userResult" :key="user.pk" :to="{ name: 'profile', params: { id: user.pk } }">
                <div class="search-profile-box">
                  <img :src="`http://127.0.0.1:8000${user.profile_img}`" alt="img">
                </div>
                <p>{{user.nickname}}</p>
              </router-link>
            </div>
          </div>  
        </div>
      </div>
    <FooterSection/>
</div>
</template>

<script>
// import CollectionList from '@/components/CollectionList'
import RecommendList from '@/components/RecommendList'
import axios from 'axios'
import FooterSection from '../../components/FooterSection'
const API_URL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('token')


export default {
  name: 'SearchView',
  data() {
    return {
      movies: [],
      users: [],
      searchResult: [],
      ottResult: [],
      userResult: [],
      otts: [],
      isSelected: {
        '2': false,
        '3': false,
        '8': false,
        '97': false,
        '192': false,
        '337': false,
      },
      searchInput: "",
      searchUserInput: "",
      focus: null,
    }
  },
  components: {
    RecommendList,
    // CollectionList,
    FooterSection,
  },
  methods: {
    Back(){
      this.$router.go(-1)
    },
    search(wordToMatch, movies) {
      const isSelected = {
        '2': false,
        '3': false,
        '8': false,
        '97': false,
        '192': false,
        '337': false,
      }
      this.isSelected = isSelected
      const value = wordToMatch.trim()
      const movieMatchDataList = value ? movies.filter(movie => movie.title.includes(value)) : []
      this.searchResult = movieMatchDataList
    },
    searchUser(wordToMatch, users) {
      const value = wordToMatch.trim()
      const userMatchDataList = value ? users.filter(user => user.nickname.includes(value)) : []
      console.log(userMatchDataList)
      this.userResult = userMatchDataList
      console.log(this.userResult)
    },
    selectResult(title) {
      this.searchInput = title
    },
    filterOtt(ott_id) {
      if (this.isSelected[ott_id] === true) {
        this.isSelected[ott_id] = false
      } else {
        const isSelected = {
          '2': false,
          '3': false,
          '8': false,
          '97': false,
          '192': false,
          '337': false,
        }
        this.isSelected = isSelected
        this.isSelected[ott_id] = true
      }
      axios({
        method: 'get',
        url: `${API_URL}/movies/otts/${ott_id}/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        this.searchResult=res.data
      })
      .catch((err) => {console.log(err)})
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

      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/otts/',
      })
      .then((res) => {
        this.otts = res.data
      })

      axios({
        methd: 'get',
        url: `${API_URL}/accounts/all_users/`
      })
      .then((res) => {
        this.users = res.data
      })
      .catch(err => console.log(err))
  }
}
</script>

<style scoped>
  #user-search {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  #search-headers{
    display: flex;
    flex-direction: column;
    align-content: space-between;
    width: 100%;
    margin-top: 50px;
  }

  #movie-main-image {
    width: 2133px;
    height: 680px;
  }

  #search {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    width: 100vw;
  }

  #search-body {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  #search-input {
    display: flex;
    align-items: center;
    padding: 10px;
    width: 400px;
    height: 30px;
    border: none;
    border-bottom: 1px solid black;
    font-size: 20px;
  }

  #search-input:focus {
    outline: none;
  }

  #search-result{
    display: flex;
    align-items: flex-start;
    width: 100vw;
    margin-top: 80px;
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
    margin-bottom: 200px;
  }

  #search-recommend-section {
    display: flex;
    align-items: flex-start;
    height: 450px;
    display: flex;
    overflow: auto;
    white-space: nowrap;
  }

  #search-recommend-list {
    display: flex;
    align-items: flex-start;
    height: 450px;
    overflow: auto;
    white-space: nowrap;
  }

  #search-recommend-list-item {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    margin-right: 30px;
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
    transition-duration: 0.2s;
    color: white;
    background-color: rgba(0, 0, 0, 0.795);
  }

  .otts {
    display: flex;
    justify-content: space-between;
    margin-left: 20px;
  }

  .ott-item {
    width: 35px;
    height: 35px;
    padding: 5px;
    border-radius: 5px;
    margin-right: 15px;
    /* background-color: #e8ca23a8; */
    box-shadow: 0px 4px 5px 0px rgba(109, 109, 109, 0.267);
  }

  .light-box {
    position: absolute;
    width: 45px;
    height: 45px;
    background-color: rgba(255, 255, 255, 0.219);
    border-radius: 5px;
    cursor: pointer;
  }

  .light-box:hover {
    background-color: #ffffff7a;
  }

  .selected {
    box-shadow: 0px 4px 5px 0px rgba(109, 109, 109, 0.267);
  }

  .today{
    word-wrap : brek-word;
    width: 155px;
    font-weight: 100;
    font-size: 30px;
  }

  .search-results-title {
    margin-left: 40px;
  }

  #search-collection-section h1{
    font-size: 40px;
    font-weight: 100;
  }

  #search-collection-section div.section-title{
    width: 1250px;
    margin-top: 80px;
    margin-bottom: 30px;
  }

  .user-today {
    font-weight: 100;
    width: 130px;
    font-size: 30px;
  }

  #search-user-list {
    display: flex;
    align-items: flex-start;
    margin-left: 28px;
    overflow: auto;
    white-space: nowrap;
  }

  .user-search-item {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .user-search-item p {
    margin-top: 12px;
    font-size: 24px;
  }

  .search-profile-box {
    display: flex;
    flex-direction: column;
    position: relative;
    width: 200px;
    height: 200px;
    margin-bottom: 20px;
  }
</style>