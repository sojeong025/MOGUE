<template>
  <div class="follow-section">
    <div class="follow-container">
      <div class="follow-nickname">{{user.nickname}}</div>
      <div class="toolbar">
        <div class="followToggle" :class="{ 'underbar': isFollower }" @click="selectFollow">
          {{ followers.length }} FOLLOWER
        </div>
        <div class="followToggle" :class="{ 'underbar': !isFollower }" @click="selectFollowing">
          {{ followings.length }} FOLLOWING
        </div>
      </div>
      <input id="search-input" 
        type="text" placeholder="검색" 
        v-model="searchInput" 
        @keydown="search(searchInput)"
      >
      <div class="follow-list-box" v-if="isFollower">
        <div v-if="!searchResult.length">
          <router-link class="follow-list-item" :to="{ name: 'profile', params: {id: follower.pk } }" v-for="follower in followers" :key="follower.pk">
            <img class="img" :src="`http://127.0.0.1:8000${follower.profile_img}`" alt="follower-profile">
            <span>{{ follower.nickname }}</span>
          </router-link>
        </div>
        <div v-else>
          <router-link class="follow-list-item" :to="{ name: 'profile', params: {id: follower.pk } }" v-for="follower in searchResult" :key="follower.pk">
            <img class="img" :src="`http://127.0.0.1:8000${follower.profile_img}`" alt="follower-profile">
            <span>{{ follower.nickname }}</span>
          </router-link>
        </div>
      </div>
      <div class="follow-list-box" v-else>
        <div v-if="!searchResult.length">
          <router-link class="follow-list-item" :to="{ name: 'profile', params: {id: following.pk } }" v-for="following in followings" :key="following.pk">
            <img class="img" :src="`http://127.0.0.1:8000${following.profile_img}`" alt="following-profile">
            <span>{{ following.nickname }}</span>
          </router-link>
        </div>
        <div v-else>
          <router-link class="follow-list-item" :to="{ name: 'profile', params: {id: following.pk } }" v-for="following in searchResult" :key="following.pk">
            <img class="img" :src="`http://127.0.0.1:8000${following.profile_img}`" alt="following-profile">
            <span>{{ following.nickname }}</span>
          </router-link>
        </div>
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
      searchInput: "",
      searchResult: [],
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
    selectFollow() {
      this.isFollower = true
    },
    selectFollowing() {
      this.isFollower = false
    },
    search(wordToMatch) {
      let list = this.followers
      if (this.isFollower) {
        list = this.followers
      } else {
        list = this.followings
      }
      const value = wordToMatch.trim()
      const movieMatchDataList = value ? list.filter(user => user.nickname.includes(value)) : []
      this.searchResult = movieMatchDataList
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
  margin-top: 60px;
  width: 100%;
  height: 820px;
}

.toolbar {
  display: flex;
  justify-content: space-around;
  width: 700px;
  margin-bottom: 6px;
}

.followToggle {
  display: flex;
  justify-content: center;
  width: 350px;
  font-size: 30px;
  padding-bottom: 12px;
  margin-bottom: 20px;
  cursor: pointer;
  border-bottom: 1px solid gray;
}

.underbar {
  border-bottom: 3px #e8aa23 solid;
}

.follow-list-box {
  width: 600px;
  height: 100%;
  overflow: auto;
  white-space: nowrap;
  /* border: 1px solid red; */
}

.follow-list-box img {
  width: 70px;
  height: 70px;
}

.follow-list-item {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 36px;
  font-size: 26px;
}

.follow-list-item img {
  margin-right: 16px;
}

.follow-list-item span {
  margin-left: 12px;
}

.follow-nickname {
  font-size: 32px;
  font-weight: 100;
  margin-bottom: 38px;
}

#search-input {
  width: 530px;
  height: 30px;
  margin-bottom: 50px;
  font-size: 22px;
  padding: 12px;
}
</style>