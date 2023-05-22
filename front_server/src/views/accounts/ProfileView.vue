<template>
  <div> 
    <h1>Profile</h1>
    <div class="profile-left">
      <p>{{user.username}}님의 프로필</p>
      <p>{{user.profile_img}} 지금은 이미지 없음</p>
      <div v-if="isFollow">
        <button @click="follow" class="follow">언팔로우</button>
      </div>
      <div v-else>
      <button @click="follow" class="follow">팔로우</button>
      </div>
      <span class="follower-number">팔로워 : {{ followings.length }}</span>
      <span class="following-number">팔로잉 : {{ followers.length }}</span>
    </div>
    <div class="profile-right">
      <div class="favorite-movie">
        <p>{user.nickname}님이 좋아하는 영화 목록</p>
        <span>1card</span> <span>2card</span> <span>3card</span> <span>4card</span> <span>5card</span> 
      </div>
      <div class="wish-movie">
        <p>{user.nickname}님이 보고싶은 영화 목록</p>
        <span>1card</span> <span>2card</span> <span>3card</span> <span>4card</span> <span>5card</span> 
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
    }
  },
  methods: {
    getUserProfile(){
      const user_id = jwtDecode(token).user_id
      const userId = this.$route.params.id
      console.log(user_id)
      console.log(userId)
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${userId}/`,
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
          this.isFollow = !this.isFollow
          console.log('팔로우 중임', this.isFollow)
        } else {
          this.isFollow = !this.isFollow
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

.profile-left {
  border: 2px solid orange;
  margin: 20px;
  height: 200px;
}
.profile-right {
  border: 2px solid blue;
  margin: 20px;
}
.favorite-movie{
  border: 2px solid greenyellow;
  margin: 10px;
}
.wish-movie {
  border: 2px solid fuchsia;
  margin: 10px;
}
.follower-number {
  border: 2px solid blueviolet;
  border-radius: 20px;
}
.following-number {
  border: 2px solid blueviolet;
  border-radius: 20px;
}
</style>