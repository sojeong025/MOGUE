<template>
  <div>
    <h1>Profile</h1>
    <p>{{ nickname }}</p>
    <!-- <button @click="follow" class="follow">Follow</button>
    <button @click="follow" class="follow">Unfollow</button> -->
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
      userData: null,
      userId: null,
      nickname: null,
      username: null,
      follower: 0,
      following: 0,
    }
  },
  methods: {
    getUserProfile(){
      const user_id = jwtDecode(token).user_id
      const userId = this.$route.params.user_id
      console.log(user_id)
      console.log(userId)
      axios({
        method: 'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.user_id}`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
    },
    
    // follow(){
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/accounts/${this.$route.params.id}/follow/`,
    //     headers: {
    //       Authorization: `JWT ${token}`
    //     }
    //   })
    //   .then((res) => console.log(res))
    //   .catch((err) => console.log(err))
    // },
  }
}
</script>

<style>

</style>