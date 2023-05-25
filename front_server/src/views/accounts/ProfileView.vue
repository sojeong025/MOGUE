<template>
  <div id="profile-section"> 
    <div id="profile-headers">
      <div class="profile-left">
        <div id="profile-img">
          <router-link :to="{ name: 'profile_update', params: { id: this.$route.params.id } }">
            <button id="edit-profile"><font-awesome-icon class="edit-icon" :icon="['fas', 'user-pen']" /></button>
          </router-link>
          <img :src="`http://127.0.0.1:8000${user.profile_img}`" alt="img">
        </div>
        <p class="profile-name">{{user.nickname}}님의 프로필</p>
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
            <div @click="follow" class="follow" style="background-color: #616264" >언팔로우</div>
          </div>
          <div v-else>
            <div @click="follow" class="follow" style="background-color: #448CCB">팔로우</div>
          </div>
        </div>
      </div>
      <!-- 해야 함 -->
      <div class="profile-right">
        <p class="liked-movie-title">{{ user.nickname }}님이 좋아하는 영화 목록</p>
        <div class="liked-items" v-if="liked_movies.length">
          <router-link :to="{ name: 'moviedetail', params: { id: liked_movie.id } }" v-for="liked_movie in liked_movies" :key="liked_movie.id" class="liked-item">
            ○ {{liked_movie.title}}
            <!-- <img id="poster-img" :src="`https://image.tmdb.org/t/p/w92${liked_movie.poster_path}`" alt="poster"> -->
          </router-link>
        </div>
        <p v-else class="no-liked">아직 좋아요한 영화가 없습니다.</p>
      </div>
    </div>

    <div class="profile-body">
      <div class="profile-right-body">
        <div class="my-articles">
          <p>{{ user.nickname }}님이 작성한 게시글</p>
          <div class="my-article" v-if="user_articles.length">
            <router-link :to="{ name: 'userarticledetail', params: { id: user_article.id } }" v-for="user_article in user_articles" :key="user_article.id" class="my-article-item">
              {{user_article.title}}
            </router-link>
          </div>
          <div v-else  class="no-my">
          <p>
            아직 작성한 게시글이 없습니다.
          </p>
          </div>
        </div>

        <div class="my-comment">
          <p>{{ user.nickname }}님이 작성한 댓글</p>
          <div class="my-comment-items" v-if="user_comments.length">
            <div class="my-comment-item" v-for="comment in user_comments" :key="comment.id">
              {{ comment.content }}
            </div>
          </div>
          <div v-else class="no-my">
            <p>
              아직 작성한 댓글이 없습니다.
            </p>
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
    }
  }
}
</script>

<style scoped>

#profile-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 80px;
}

#profile-headers {
  display: flex;
  justify-content: flex-start;
  height: 350px;
}

.profile-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* border: 2px solid orange; */
  width: 380px;
  height: 380px;
}

.profile-right {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  width: 300px;
  padding-left: 50px;
  /* border: 2px solid blue; */
  margin-bottom: 30px;
  border-left: 1px solid black;
}

.liked-movie-title{
  width: 600px;
  margin-top: 10px;
  margin-bottom: 20px;
  margin-left: 20px;
  font-size: 25px;
  font-weight: 600;
}

.img {
  width: 100px;
}

.my-articles{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 500px;
  font-size: 25px;
}

.my-article{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: 230px;
  margin-top: 20px;
  margin-left: 15px;
  overflow: auto;
  white-space: nowrap;
}

.my-article-item {
  display: flex;
  align-items: center;
  height: 30px;
  padding: 0px 5px;
  font-size: 22px;
  margin-bottom: 10px;
}

.my-article-item:hover {
  background-color: white;
}

#profile-img {
  display: flex;
  flex-direction: column;
  position: relative;
  width: 200px;
  height: 200px;
  margin-bottom: 20px;
}

#profile-img > img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

#edit-profile {
  position: absolute;
  left: 80%;
  bottom: 78%;
  z-index: 100;
  border: none;
  border-radius: 100px;
  width: 30px;
  height: 30px;
  cursor: pointer;
  background-color: white;
}

.liked-items {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  height: 230px;
  margin-left: 25px;
  overflow: auto;
  white-space: nowrap;
}

.liked-item {
  font-size: 22px;
  padding: 0px 5px;
  margin-bottom: 10px;
}

.no-liked {
  margin-left: 25px;
  font-size: 20px;
}

.profile-body {
  border: solid 1px red;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 1000px;
  height: 378px;
  margin-top:60px;
  padding: 60px 300px 0px 620px;
}

.my-comment{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  font-size: 25px;
  width: 500px;
}

.my-comment-items {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  font-size: 22px;
  width: 300px;
  margin-top: 20px;
  margin-left: 16px;
}

.my-comment-item {
  margin-bottom: 10px;
  padding-left: 5px;
  cursor: pointer;
}

.my-comment-item:hover {
  background-color: white;
}

.follow{
  width: 100px;
  height: 50px;
  border: 1px red solid;
  margin: 10px;
  cursor: pointer;
  background-color: black;
  color: white
}

.follow-number {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 120px;
  height: 60px;
  /* border: 2px solid blueviolet; */
  border-radius: 20px;
  margin: 0px -15px;
}

.itsme{
  visibility: hidden;
}

.profile-right-headers {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100vw;
  height: 100px;
  margin-bottom: 30px;
}

.profile-right-body {
  display: flex;
  justify-content: space-around;
  height: 300px;
  width: 1000px;
  /* border: 2px solid blue; */
}

.follow-info {
  display: flex;
  justify-content: center;
  flex-direction: row;
  /* width: 100%; */
  margin-top: 20px;
}

.profile-name {
  font-size: 30px;
  margin-bottom: -10px;
}

.edit-icon {
  color: rgba(0, 0, 0, 0.63);
  margin-left: 5px;
}

.no-my {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-end;
  margin-top: 20px;
  margin-left: 8px;
  font-size: 17px;
}

.follow {
  width: 200px;
  height: 30px;
  border-radius: 10px;
  text-align: center;
  padding-top: 6px;
  border: none;
}
.follow-number{
  margin: -10px -30px;
}
</style>