<template>
  <div id="profile-section"> 
    <div id="profile-headers">
      <div class="profile-left">
        <div id="profile-img">
          <router-link :to="{ name: 'profile_update', params: { id: this.$route.params.id } }">
            <button id="edit-profile"></button>
          </router-link>
          <img :src="`http://127.0.0.1:8000${user.profile_img}`" alt="img">
        </div>
        <p class="profile-name">{{user.nickname}}님의 프로필</p>
        <div class="follow-info">
          <router-link :to="{ name: 'follow', params: {  id: this.$route.params.id } }">
            <div class="follow-number">
              팔로워 : {{ followers.length }}
            </div>
          </router-link>
          <router-link :to="{ name: 'follow', params: {  id: this.$route.params.id } }">
            <div class="follow-number">
              팔로잉 : {{ followings.length }}
            </div>
          </router-link>
        </div>
        <div v-if="!itsMe">
          <div v-if="isFollow">
            <span @click="follow" class="follow">언팔로우</span>
          </div>
          <div v-else>
            <span @click="follow" class="follow">팔로우</span>
          </div>
        </div>
      </div>
      <!-- 해야 함 -->
      <div class="profile-right">
        <p class="liked-movie-title">{{ user.nickname }}님이 좋아하는 영화 목록</p>
        <div class="favorite-items">
          <span>1card</span>
          <span>2card</span>
          <span>3card</span> 
          <span>4card</span> 
          <span>5card</span> 
        </div>
      </div>
    </div>

    <div class="profile-body">
      <div class="profile-right-body">
        <div class="write-article">
          <p>{{ user.nickname }}님이 작성한 article</p>
          <div>1card</div> <div>2card</div> <div>3card</div> <div>4card</div> <div>5card</div> 
        </div>

        <div class="my-ott">
          <p>
            <span>{{ user.nickname }}님이 구독중인 서비스</span> <button>수정</button>
          </p>
          <div class="my-ott-items">
          <div>1card</div> <div>2card</div> <div>3card</div> <div>4card</div> <div>5card</div> 
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from 'jwt-decode'
const token = localStorage.getItem('token')


const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  created() {
    this.getFollowData()
    if (localStorage.getItem('token')) {
      this.getUserProfile()
    } else {
      this.$router.push({ name: 'login' })
    }
  },
  data(){
    return{
      user : Object,
      followers: [],
      followings: [],
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
        this.user = res.data.user
        this.followers = res.data.followers
        this.followings = res.data.followings
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
        console.log(list.length)
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
    }
  }
}
</script>

<style>

#profile-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 130px;
}

#profile-headers {
  display: flex;
  justify-content: start;
  height: 350px;
}

.profile-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* border: 2px solid orange; */
  width: 380px;
  height: 410px;
}

.profile-right {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: start;
  width: 500px;
  border: 2px solid blue;
  margin-bottom: 30px;
}
.liked-movie-title{
  font-size: 25px;
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
  left: 5%;
  bottom: 78%;
  z-index: 100;
  border: none;
  border-radius: 100px;
  width: 30px;
  height: 30px;
  background-color: #ffc107;
  cursor: pointer;
}

.favorite-items {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 55px;
}

.wish-movie {
  width: 1000px;
  border: 2px solid fuchsia;
  margin-bottom: 20px;
}
.watched-movie{
  width: 1000px;
  border: 2px solid orange;
  margin-bottom: 20px;
}

.profile-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 60px;
  width: 1000px;
  height: 460px;
  padding: 20px 800px 0px 800px;
  background-color: #ffc107;
}

.write-article{
  border: 1px solid red;
  width: 300px;
}

.my-ott{
  border: 1px solid white;
  width: 300px;
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
  margin: 0px 20px;
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
  border: 2px solid blue;
}

.follow-info {
  display: flex;
  justify-content: center;
  flex-direction: row;
  width: 100%;
  margin-top: 20px;
}

.profile-name {
  font-size: 30px;
  margin-bottom: -10px;
}


</style>