<template>
  <div id="movie-detail-section">
    <div id="movie-section">
      <div class="detail-left">
        <img id="poster-img" :src="`https://image.tmdb.org/t/p/w780/${movie.poster_path}`" alt="poster">
        <div id="detail-info">
          <h1 id="detail-title">{{ movie.title }} <span id="movie-runtime">{{ movie.runtime }}분</span></h1>
          <p id="detail-overview">{{ movie.overview.slice(0, 150) }}...</p>
        </div>
      </div>
      <div class="detail-right">
        <button class="likeBtn" v-if="liked" @click="likeMovie"><font-awesome-icon :icon="['fas', 'heart']" size="lg" :style="{ color: 'red' }" /></button>
        <button class="likeBtn" v-else @click="likeMovie"><font-awesome-icon :icon="['far', 'heart']" size="lg" :style="{ color: 'red' }" /></button>
        <div class="ott-items">
          <div class="ott-item" v-for="ott in otts" :key="ott.id">
            <img class="ott-item" :src="`https://image.tmdb.org/t/p/w45${ott.logo_path}`" alt="">
          </div>
        </div>
      </div>
    </div>
    <hr class="review-hr">
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
            <span>{{ review.star }}</span> |
            <span id="deleteBtn" @click="deleteReview(review.id)">X</span>
            </div>
          </div>
          <hr id="review-hr">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
import jwtDecode from "jwt-decode"
const API_URL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('token')

export default {
  name: 'MovieDetailView',
  components: {
    StarRating
  },
  data() {
    return {
      movie: Object,
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
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        this.movie = res.data.movie
        this.reviews = res.data.reviews
        console.log(res)
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
    }
  },
  created() {
    this.getMovieDetail()
  }
}
    
</script>

<style scoped>
  #movie-detail-section {
    margin-top: 0px;
    font-size: 20px;
  }

  #poster-img {
    display: flex;
    width: 380px;
    height: 600px;
  }

  #movie-section {
    display: flex;
    justify-content: space-between;
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
    margin-left: 20px;
    height: 500px;
  }

  #review-box {
    margin-top: 20px;
    margin-left: 14px;
  }

  #reviews {
    display: flex;
    justify-content: space-between;
    font-size: 24px;
    width: 500px;
    margin-top: 14px;
  }

  #review-input-section{
    display: flex;
    align-items: center;
  }

  #review-input {
    font-size: 20px;
    margin-right: 40px;
    width: 400px;
    height: 35px;
    padding: 6px;
    padding-left: 14px;
    border-radius: 5px;
    border: none;
  }

  #review-input:hover {
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
    cursor: pointer;
  }

  .likeBtn {
    width: 80px;
    height: 80px;
    border: none;
    border-radius: 100px;
    font-size: 20px;
    cursor: pointer;
  }

  .detail-left {
    display: flex;
    align-items: flex-end;
  }

  .detail-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-right: 25px;
  }

  .ott-items {
    display: flex;
    margin-top: 20px;
  }

  .ott-item {
    margin-left: 10px;
  }

  .review-hr {
    background-color: black;
    border: none;
    height: 1px;
    margin-top: 20px;
    margin-left: 35px;
    width: 1230px;
  }
</style>