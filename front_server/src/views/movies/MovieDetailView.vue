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
        <button class="likeBtn" v-if="liked" @click="likeMovie">UnLike</button>
        <button class="likeBtn" v-else @click="likeMovie">Like</button>
      </div>
    </div>

    <div id="review-section" class="yellow">
      <form @submit.prevent="createReview" id="review-input-section">
        <input id="review-input" type="text" placeholder="리뷰를 작성해보세요" v-model="content">
        <div class="rating">
          <star-rating
            :show-rating="false"
            inactive-color="#21f1ff"
            active-color="#ffffff"
            :star-size=35
            v-model="rating"
          ></star-rating>
        </div>
        <input id="submit-btn" type="submit" value="작성">
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
        console.log(res.data.movie)
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
    margin-top: 200px;
    font-size: 20px;
  }

  #poster-img {
    display: flex;
    width: 300px;
    height: 480px;
  }

  #movie-section {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 130px;
    margin-left: 35px;
    margin-right: 35px;
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
    margin-top: 30px;
    height: 500px;
  }

  #review-box {
    margin-top: 20px;
    margin-left: 14px;
  }

  #reviews {
    display: flex;
    justify-content: space-between;
    width: 500px;
    margin-top: 14px;
  }

  #review-input-section{
    display: flex;
    align-items: center;
  }

  #review-input {
    margin-right: 10px;
    width: 400px;
    height: 35px;
    padding-left: 10px;
    border-radius: 5px;
    border: none;
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
</style>