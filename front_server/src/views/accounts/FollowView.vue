<template>
  <div>
    <h1>Follow 정보</h1>
    
    <div>
      <h3>Followers:</h3>
      <ul>
        <li v-for="follower in followers" :key="follower.id">
          <router-link :to="{ name: 'profile', params: {id: follower.pk } }">
            {{ follower.profile_img }}
            {{ follower.nickname }}
          </router-link>
        </li>
      </ul>
    </div>

    <div>
      <h3>Following:</h3>
      <ul>
        <li v-for="following in followings" :key="following.id">
          <router-link :to="{ name: 'profile', params: {id: following.pk } }">
            {{ following.profile_img }}
            {{ following.nickname }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const token = localStorage.getItem('token')
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FollowView',
  data(){
    return{
      followers: [],
      followings: [],
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
        // console.log(res.data.followings)
        // console.log(res.data.followers)
      })
    }
  },
  created() {
    this.getFollowData()
  },
}
</script>

<style>

</style>