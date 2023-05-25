<template>
  <div class="follow-section">
    <div class="follow-container">
      <div class="toolbar">
        <div class="followToggle" :class="{ 'underbar': isFollower }" @click="selectFollow">
          FOLLOWER
        </div>
        <div class="followToggle" :class="{ 'underbar': !isFollower }" @click="selectFollowing">
          FOLLOWING
        </div>
      </div>
      <div class="follow-list-box" v-if="isFollower">
        <router-link class="follow-list-item" :to="{ name: 'profile', params: {id: follower.pk } }" v-for="follower in followers" :key="follower.pk">
          <img class="img" :src="`http://127.0.0.1:8000${follower.profile_img}`" alt="follower-profile">
          {{ follower.nickname }}
        </router-link>
      </div>
      <div class="follow-list-box" v-else>
        <router-link class="follow-list-item" :to="{ name: 'profile', params: {id: following.pk } }" v-for="following in followings" :key="following.pk">
          <img class="img" :src="`http://127.0.0.1:8000${following.profile_img}`" alt="following-profile">
          {{ following.nickname }}
        </router-link>
      </div>
    </div>
    <FooterSection/>
  </div>
</template>

<script>
import axios from 'axios'
import FooterSection from '../../components/FooterSection'
const token = localStorage.getItem('token')
import jwtDecode from 'jwt-decode'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FollowView',
  components: {
    FooterSection,
  },
  data(){
    return{
      followers: [],
      followings: [],
      follow_id: null,
      user: Object,
      itsMe: null,
      isFollower: true,
      isFollow: null,
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
        console.log(this.followings)
        console.log(this.followers)
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
    selectFollow() {
      this.isFollower = true
    },
    selectFollowing() {
      this.isFollower = false
    },
  },
  created() {
    this.getFollowData()
    this.getUserInfo()
  },
}
</script>

<style scoped>
.follow-container {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  margin-top: 30px;
  width: 100%;
  height: 547px;
}

.toolbar {
  display: flex;
  justify-content: space-around;
  width: 500px;
  margin-bottom: 20px;
}

.followToggle {
  cursor: pointer;
}

.underbar {
  border-bottom: 1px black solid;
}

.follow-list-box {
  width: 500px;
  height: 100%;
  overflow: auto;
  white-space: nowrap;
  /* border: 1px solid red; */
}

.follow-list-box img {
  width: 50px;
  height: 50px;
}

.follow-list-item {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.follow-list-item img {
  margin-right: 16px;
}
</style>