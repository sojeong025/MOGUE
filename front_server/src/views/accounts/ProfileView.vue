<template>
<div>
  <div class="profile-section"> 
    <div class="profile-left">
      <div class="profile">
        <div class="profile-img">
          <div v-if="itsMe">
            <router-link class="edit-btn" :to="{ name: 'profile_update', params: { id: this.$route.params.id } }">
              <button id="edit-profile">
                <font-awesome-icon class="edit-icon" :icon="['fas', 'user-pen']" />
              </button>
            </router-link>
          </div>
          <img :src="`http://127.0.0.1:8000${user.profile_img}`" alt="img">
        </div>
        <p class="profile-name">{{user.nickname}}</p>
        <div class="follow-info">
          <router-link :to="{ name: 'follow', params: {  id: this.$route.params.id } }">
            <div class="follow-number">
              팔로워  {{ followers.length }}
            </div>
          </router-link>
          <router-link :to="{ name: 'follow', params: {  id: this.$route.params.id } }">
            <div class="follow-number">
              팔로잉  {{ followings.length }}
            </div>
          </router-link>
        </div>
        <div v-if="!itsMe">
          <div v-if="isFollow">
            <div @click="follow" class="follow" style="background-color: #616264; color: #fff; cursor: pointer;" > <font-awesome-icon :icon="['fas', 'user-minus']" /> 언팔로우</div>
          </div>
          <div v-else>
            <div @click="follow" class="follow" style="background-color: #448CCB; color: #fff; cursor: pointer;"> <font-awesome-icon :icon="['fas', 'user-plus']" /> 팔로우</div>
          </div>
        </div>
      </div>
    </div>
    <hr>

    <div class="profile-right">
      <div class="right-main-top">
        <p class="liked-movie-title">{{ user.nickname }}'s PICK</p>
          <div class="liked-items" v-if="liked_movies.length">
            <router-link :to="{ name: 'moviedetail', params: { id: liked_movie.id } }" v-for="liked_movie in liked_movies" :key="liked_movie.id" class="liked-item">
              <img :src="`https://image.tmdb.org/t/p/w154${liked_movie.poster_path}`" alt="">
              <p id="liked-movie-title">{{liked_movie.title}}</p>
            </router-link>
          </div>
        <p v-else class="no-liked">아직 좋아요한 영화가 없습니다.</p>
      </div>
      <div class="right-bottom">
        <div class="my-articles">
          <p class="name">MY ARTICLES</p>
          <div class="my-article" v-if="user_articles.length">
            <router-link :to="{ name: 'userarticledetail', params: { id: user_article.id } }" v-for="user_article in user_articles" :key="user_article.id" class="my-article-item">
              {{user_article.title}}
            </router-link>
          </div>
          <div v-else  class="no-my">
          <p>아직 작성한 게시글이 없습니다.</p>
          </div>
        </div>

        <div class="my-comments">
          <p class="name">MY COMMENTS</p>
          <div class="my-comment-items" v-if="user_comments.length">
            <div class="my-comment-item" v-for="comment in user_comments" :key="comment.id">
              <router-link :to="{ name:'userarticledetail', params: { id: comment.article.id } }">
                {{ comment.content }}
              </router-link>
            </div>
          </div>
          <div v-else class="no-my">
            <p>아직 작성한 댓글이 없습니다.</p>
          </div>
        </div>
      </div>
      </div>
  </div>
    <FooterSection/>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'
import FooterSection from '../../components/FooterSection'
const token = localStorage.getItem('token')


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    FooterSection,
  },
  created() {
    this.getFollowData()
    this.getUserProfile()
    this.getComments()
  },
  data(){
    return{
      user : Object,
      followers: [],
      followings: [],
      liked_movies: [],
      user_articles: [],
      user_comments: [],
      isFollow: false,
      itsMe: null,
    }
  },
  methods: {
    getUserProfile(){
      const user_id = jwtDecode(token).user_id
      const profile_id = this.$route.params.id

      const checkId = parseInt(profile_id)

      if (user_id === checkId) {
        this.itsMe = true
        console.log('본인 페이지임')
        console.log(this.itsMe)
      } else {
        this.itsMe = false
        console.log('다른 사람 페이지임')
      }

      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${profile_id}/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) =>{
        console.log(res)
        this.user = res.data.user
        this.followers = res.data.followers
        this.followings = res.data.followings
        this.liked_movies = res.data.userLikeMovies
        this.user_articles = res.data.userCreateArticles
      })
      .catch(err => console.log(err))
    },
    follow(){
      const profile_id = this.$route.params.id
      console.log(profile_id)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${this.$route.params.id}/follow/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.isFollow = res.data.follow
        this.followers = res.data.followers
        this.followings = res.data.followings
        this.getFollowData()
      })
      .catch(err => console.log(err))
    },
    getFollowData(){
      const user_id = jwtDecode(token).user_id
      const profile_id = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/accounts/${profile_id}/follow_list/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        const list = res.data.followers.filter(user => user.pk === user_id)
        if (list.length) {
          this.isFollow = true
          console.log('팔로우 중임', this.isFollow)
        } else {
          this.isFollow = false
          console.log('팔로우 취소함', this.isFollow)
        }
        this.followers = res.data.followers
        this.followings = res.data.followings
      })
      .catch(err => console.log(err))
    },
    getComments(){
      axios({
        url: `${API_URL}/community/comment/user_comments/`,
        method: 'get',
        headers: {
          Authorization: `JWT ${token}`
        }        
      })
      .then((res) => {
        this.user_comments = res.data
      })
    },
  }
}
</script>

<style scoped>
.profile-section {
  display: flex;
  margin: 80px;
  margin-right: 140px;
}
.profile-left {
  /* border: 1px solid black; */
  margin: 10px;
  padding: 30px;
  height: 700px;
  flex: 1;
  display: flex;
  justify-content: center;
  /* align-items: center; */
}

.profile-img {
  display: flex;
  flex-direction: column;
  position: relative;
  width: 200px;
  height: 200px;
  margin-bottom: 20px;
  /* border-radius: 100px; */
}

.edit-btn{
  top: 22%;
  right: 7%;
  position: absolute;
}

#profile-img > img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
  /* border-radius: 10px; */
}

#edit-profile {
  position: absolute;
  left: 14.5%;
  bottom: 71%;
  z-index: 100;
  border: none;
  border-radius: 100px;
  width: 30px;
  height: 30px;
  cursor: pointer;
  background-color: white;
}
.edit-icon {
  color: rgba(0, 0, 0, 0.63);
  margin-left: 5px;
}
.profile-name{
  text-align: center;
  margin: 20px 0;
  font-size: 25px;
  font-weight: 600;
}

.follow-info{
  display: flex;
  margin: 10px 30px 10px;
  justify-content: space-between;
}

.profile-right {
  /* border: 1px solid black; */
  width: 1500px;
  /* margin: 10px; */
  /* padding: 30px; */
  /* height: 700px; */
  flex: 6;
}
.follow {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 160px;
  height: 42px;
  border-radius: 10px;
  text-align: center;
  border: none;
}
.follow-number{
  margin: 0px -15px;
  text-align: center;
}

.right-main-top{
  /* border: 1px solid black; */
  flex:2;
  width: 1400px;
  height: 420px;
  margin: 30px;
  border-bottom: 1px solid black;
}

.liked-movie-title{
  margin: 30px;
  font-size: 25px;
  font-weight: 600;
}

.liked-items {
  display: flex;
  width: 98%;
  overflow: auto;
  white-space: nowrap;
}

.liked-item{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 10px;
}

.my-article{
  display: flex;
  flex-direction: column;
  height: 300px;
  overflow: auto;
  white-space: nowrap;
}

.my-article-item {
  padding: 0px;
  margin-bottom: 8px;
}

.no-my {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  margin-top: 20px;
  font-size: 17px;
}


.right-bottom{
  display: flex;
  /* border: 1px solid black; */
  /* flex:1; */
  width: 1400px;
  margin: 30px;
  height: 350px;
}

.my-articles{
  /* border: 1px solid black; */
  margin-left: 20px;
  margin-top: 20px;
  margin-right: 10px;
  flex:1;
}
.my-comments{
  /* border: 1px solid black; */
  margin-left: 20px;
  margin-top: 20px;
  margin-left: 20px;
  flex:1;
}

.profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.no-liked {
  margin-left: 30px;
  margin-bottom: 16px;
}

.name {
  margin-bottom: 16px;
  font-weight: 600;
  font-size: 25px;
}

.my-comment-item {
  margin-bottom: 8px;
}

.my-comment-items {
  display: flex;
  flex-direction: column;
  height: 300px;
  overflow: auto;
  white-space: nowrap;
}

#liked-movie-title {
  width: 126px;
  font-size: 18px;
  white-space: normal;
  text-align: center;
}
</style>