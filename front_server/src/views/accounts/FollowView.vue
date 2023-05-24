<template>
  <div id="follow-section">
    <h1 class="user">
      {{user.nickname}}
    </h1>
    <div class="follow-information">
      <div class="followers">
        <h3>팔로워</h3>
        <ul class="followers-content">
          <li v-for="follower in followers" :key="follower.id">
            <router-link :to="{ name: 'profile', params: {id: follower.pk } }">
              <img class="img" :src="`http://127.0.0.1:8000${follower.profile_img}`" alt="follower-profile">
              {{ follower.nickname }}
            </router-link>
            <div v-if="itsMe">
              <span @click="follow" class="follow">삭제</span>
            </div>
          </li>
        </ul>
      </div>
      <hr>
      <div class="follwings">
        <h3>팔로잉</h3>
        <ul class="follwings-content">
          <li v-for="following in followings" :key="following.pk">
            <router-link :to="{ name: 'profile', params: {id: following.pk } }">
              <img class="img" :src="`http://127.0.0.1:8000${following.profile_img}`" alt="following-profile">
              {{ following.nickname }}
            </router-link>
            <div v-if="!itsMe" :follow_id="following.id">
              <div>
                <span @click="follow(following.pk)" class="follow">팔로우</span>
              </div>
              <div>
                <span @click="follow(following.pk)" class="follow">언팔로우</span>
              </div>
            </div>
          </li>
        </ul>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
const token = localStorage.getItem('token')
import jwtDecode from 'jwt-decode'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FollowView',
  data(){
    return{
      followers: [],
      followings: [],
      follow_id: null,
      user: Object,
      itsMe: null,
      
    }
  },
  methods: {
    getFollowData(){
    const profile_id = this.$route.params.id
    axios({
      method: 'get',
      url: `${API_URL}/accounts/${profile_id}/follow_list/`,
      headers: {
        Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        this.followers = res.data.followers
        this.followings = res.data.followings
      })
    },
    getUserInfo(){
      const user_id = jwtDecode(token).user_id
      const profile_id = this.$route.params.id
      const checkId = parseInt(profile_id)

      if (user_id === checkId) {
        this.itsMe = true
      } else {
        this.itsMe = false
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
    follow(user_id){
      console.log(user_id)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/${user_id}/follow/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        this.isFollow = res.data.follow
        this.followers = res.data.followers
        this.followings = res.data.followings
        this.getFollowData()
      })
      .catch(err => console.log(err))
    },
  },
  created() {
    this.getFollowData()
    this.getUserInfo()
  },
}
</script>

<style scoped>
#follow-section {
  margin-top: 180px;
  text-align: center;
}
.user{
  margin-bottom: 30px;
  font-size: 30px;
}
.follow-information {
  display: flex;
  justify-content: center;
}
.followers{
  margin: 0 15px 0 30px;
  width: 500px;
  height: 500px;
  /* border:1px solid black; */
}
.follwings{
  margin: 0 30px 0 15px;
  width: 500px;
  height: 500px;
  /* border:1px solid black; */
}
.img {
  border-radius: 50%;
  width: 35px;
  height: 35px;
}
li {
  list-style-type: none;
}
h3 {
  margin: 10px 0 30px;
  background-color: #e8aa23;
  padding: 8px
}
hr {
  margin-top: 10px;
  width: 2px;
  background-color: #d1d1cf;
  border: none;
}
.followers-content{
  display: flex;
  justify-content: center;
}
.follwings-content{
  display: flex;
  justify-content: center;
}
</style>