<template>
  <div id="update_profile">
    <form id="update-profile-form" @submit.prevent="updateProfile">
      <h2>Update Profile</h2>
      <input type="text" placeholder="NickName" v-model="nickname" required />
      <input type="file" @change="handleImgChange" accept="image/*">
      <input type="submit" value="회원 정보 수정">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const token = localStorage.getItem('token')


export default {
  name: 'update_profile',
  data() {
    return {
      user: {
        nickname: null,
        profile_img: null,
      }
    }
  },
  methods: {
    updateProfile() {
      const formData = {
        nickname: this.nickname,
        profile_img: this.profile_img,
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/profile/${this.$route.params.id}/update/`,
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `JWT ${token}`
        }
      })
      .then(() => {
        this.$router.push({ name: 'profile' })
      })
    },
    handleImgChange(event) {
      this.profile_img = event.target.files[0]
      this.fileName = event.target.files[0].name
      // this.preview = URL.createObjectURL(this.event.target.files[0])
    },
  }
}
</script>

<style>
  #update_profile {
    margin-top: 140px;
    margin-left: 50px;
  }

  #update-profile-form {
    display: flex;
    flex-direction: column;
    width: 300px;
  }
</style>