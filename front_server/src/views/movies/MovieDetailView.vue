<template>
<div>
  <div id="movie-detail-section">
    <div id="movie-section">
      <div class="detail-left">
        <img id="poster-img" :src="`https://image.tmdb.org/t/p/w780/${movie.poster_path}`" alt="poster">
        <div id="detail-info">
          <h1 id="detail-title">{{ movie.title }} <span id="movie-runtime">{{ movie.runtime }}분</span></h1>
          <p id="detail-overview">{{ movie.overview }}...</p>
        </div>
      </div>
      <div class="detail-right">
        <button class="likeBtn" v-if="liked" @click="likeMovie"><font-awesome-icon :icon="['fas', 'heart']" size="lg" :style="{ color: 'red' }" /></button>
        <button class="likeBtn" v-else @click="likeMovie"><font-awesome-icon :icon="['far', 'heart']" size="lg" :style="{ color: 'red' }" /></button>
        <div class="ott-items">
          <div class="ott-item" v-for="ott in otts" :key="ott.id">
            <img class="ott-item" :src="`http://127.0.0.1:8000/watchprovidericon${ott.logo_path}color.png`" alt="">
          </div>
        </div>
      </div>
    </div>
    <hr class="review-hr">
    <div v-if="movieTrailer.length">
      <h1 class="trailer-section-title">{{movie.title}} Trailer</h1>
      <div class="trailer-section">
        <div v-for="trailer in movieTrailer" :key="trailer.id">
          <iframe class="trailer-item" width="560" height="315" :src="`https://www.youtube.com/embed/${trailer.key}`" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
          </iframe>
        </div>
      </div>
    </div>
    <div class="no-trailer" v-else>
      <p>{{movie.title}}의 예고편이 없어요</p>
    </div>
    <div id="review-section" class="yellow">
      <form @submit.prevent="createReview" id="review-input-section">
        <input id="review-input" type="text" placeholder="리뷰를 작성해보세요" v-model="content">
        <div class="rating">
          <star-rating
            :show-rating="false"
            inactive-color="#00000"
            active-color="#ffc107"
            :star-size=35
            v-model="rating"
          ></star-rating>
        </div>
      </form>
      <div id="review-box">
        <div v-for="review in reviews" :key="review.id">
          <div id="reviews">
            <span>{{ review.content }}</span>
            <div>
            <span>★{{ review.star }}&nbsp;</span> | <font-awesome-icon id="deleteBtn" :icon="['fas', 'trash']" @click="deleteReview(review.id)"/>
            </div>
          </div>
          <hr id="review-hr">
        </div>
      </div>
    </div>
    </div>
    <FooterSection/>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
import jwtDecode from "jwt-decode"
const API_URL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('token')
import FooterSection from '../../components/FooterSection'


export default {
  name: 'MovieDetailView',
  components: {
    StarRating,
    FooterSection,
  },
  data() {
    return {
      movie: Object,
      movieTrailer: [],
      reviews: [],
      otts: [],
      content: null,
      rating: 0,
      liked: false,
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/`,
      })
      .then((res) => {
        this.movie = res.data.movie
        this.reviews = res.data.reviews
        this.otts = res.data.otts
        if (res.data.movie.users.includes(jwtDecode(token).user_id)) {
          this.liked = true
        } else {
          this.liked = false
        }
      })
      .catch(err => console.log(err))
    },
    createReview() {
      const formData = {
        user: jwtDecode(token).user_id, // 초기값은 null로 설정합니다.
        movie: this.movie.id,
        content: this.content,
        star: this.rating
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/reviews/create/`,
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        this.reviews.push(res.data)
        this.rating = 0
        this.content = null
      })
      .catch(err => console.log(err))
    },
    deleteReview(review_id) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/reviews/${review_id}/`,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `JWT ${token}`
        }
      })
      .then(() => {
        this.getMovieDetail()
      })
      .catch(err => console.log(err))
    },
    likeMovie() {
      const formData = {
        user: jwtDecode(token).user_id, // 초기값은 null로 설정합니다.
        movie: this.movie.id,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        this.liked = res.data.liked
      })
      .catch(err => console.log(err))
    },
    getYoutubeTrailer(){
      axios({
        url: `https://api.themoviedb.org/3/movie/${this.$route.params.id}/videos?language=ko-KR`,
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTc1NzVjZGE4MzFkY2VhZWM3ZWY2ZDMxZDZjNjc5NCIsInN1YiI6IjYzZDMzOTU4NjZhZTRkMDA4YzkyYTM4OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZUxmsj6U1koqcc3GGoYrAUoSO3uh6PVngcT3O0zMxpI'
        }
      })
      .then((res) => {
        console.log(res.data.results)
        this.movieTrailer = res.data.results
      })
      .catch(err => console.log(err))
    }
  },
  created() {
    this.getMovieDetail()
    this.getYoutubeTrailer()
  }
}
    
</script>

<style scoped>
  #movie-detail-section {
    margin-top: 0px;
    margin-left: 70px;
    font-size: 20px;
  }

  #poster-img {
    display: flex;
    width: 380px;
    height: 600px;
  }

  #movie-section {
    display: flex;
    justify-content: flex-start;
    align-items: flex-end;
    margin-top: 50px;
    margin-left: 35px;
    margin-right: 35px;
    margin-bottom: 50px;
  }

  #movie-runtime {
    font-size: 16px;
  }

  #detail-title {
    font-size: 48px;
  }

  #detail-overview {
    width: 500px;
    margin-top: 30px;
    text-overflow : ellipsis;
  }

  #detail-info {
    margin-left: 18px;
  }

  #review-section {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    margin-top: 30px;
    margin-left: 50px;
    height: 500px;
  }

  #review-box {
    margin-top: 20px;
    margin-left: 14px;
  }

  #reviews {
    display: flex;
    justify-content: space-between;
    font-size: 22px;
    width: 500px;
    margin-top: 14px;
  }

  #reviews div {
    display: flex;
    align-items: center;
  }

  #reviews span {
    display: flex;
    align-items: center;
  }

  #review-input-section{
    display: flex;
    align-items: center;
  }

  #review-input {
    font-size: 24px;
    margin-right: 40px;
    width: 400px;
    height: 35px;
    padding: 6px;
    padding-left: 14px;
    border-radius: 5px;
    border: none;
    outline: none;
    border: none;
    border-radius: 0px;
    border-bottom: solid 1px;
  }

  #review-input:focus {
    outline: none;
    border: none;
    border-radius: 0px;
    border-bottom: solid 1px;
  }

  .rating_box {
    display: flex;
  }

  .rating {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    color: #ddd;
    font-size: 30px;
    text-align: center;
  }

  .rating_input {
    position: absolute;
    left: 0;
    right: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: pointer;
  }

  .rating_star {
    width: 0;
    color: #ffc107;
    position: absolute;
    left: 0;
    right: 0;
    overflow: hidden;
    pointer-events: none;
  }

  #submit-btn {
    width: 40px;
    height: 32px;
    margin-left: 12px;
    border: none;
    border-radius: 6px;
    background-color: white;
  }

  #review-hr {
    width: 500px;
    height: 1px;
    background-color: white;
    color:white;
    border: none;
  }

  #deleteBtn {
    width: 22px;
    height: 22px;
    margin-left: 5px;
    cursor: pointer;
  }

  .likeBtn {
    width: 80px;
    height: 80px;
    border: none;
    border-radius: 100px;
    background-color: transparent;
    font-size: 20px;
    cursor: pointer;
  }

  .detail-left {
    display: flex;
    align-items: flex-end;
  }

  .detail-right {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    margin-left: 100px;
  }

  .ott-items {
    display: flex;
    margin-top: 20px;
  }

  .ott-item {
    display: flex;
    flex-direction: column;
    position: relative;
    width: 45px;
    height: 45px;
    margin-bottom: 20px;
    margin-left: 10px;
  }

  #review-hr {
    background-color: black;
    border: none;
    height: 1px;
    margin-top: 10px;
    margin-bottom: 25px;
    width: 500px;
  }

  .trailer-section-title{
    margin-top: 60px;
    margin-left: 40px;
  }

  .trailer-section {
    width: 1770px;
    height: 350px;
    margin-top: 40px;
    margin-left: 40px;
    padding-right: 40px;
    display: flex;
    overflow: auto;
    white-space: nowrap;
  }

  .trailer-item {
    margin-right: 40px;
  }

  .no-trailer {
    margin-top: 30px;
    margin-left: 40px;
  }
</style>