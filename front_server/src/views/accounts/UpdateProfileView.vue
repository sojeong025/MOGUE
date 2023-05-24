<template>
  <div id="update_profile">
    <form id="update-profile-form" @submit.prevent="updateProfile">
      <h1 class="update-profile-item">Update Profile</h1>
      <hr class="update-profile-underbar">

      <div class="nickname-box">
        <h3>Nickname</h3>
      </div>
      <input class="update-profile-item nickname" type="text" placeholder="닉네임" v-model="nickname" required />

        <h3>Profile Image</h3>
      <div class="update-profile-filebox">
        <input class="update-profile-upload-name" disabled v-model="fileName" value="프로필 사진" placeholder="프로필 사진">
        <label for="file">파일찾기</label>
        <input type="file" id="file" @change="handleImgChange" accept="image/*">
      </div>
      <div class="update-submit-box">
        <input class="button" type="submit" value="회원 정보 수정">
      </div>
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
      },
      fileName: '프로필 사진',
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

<style scoped>
  #update_profile {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 900px;
    margin: 130px auto auto;
    box-shadow: 8px 8px 20px #62646465;
    padding: 40px
  }

  #update-profile-form {
    display: flex;
    flex-direction: column;
    width: 400px;
  }

  h1.update-profile-item {
    text-align: center;
  }

  .update-profile-underbar {
    align-self: center;
    width: 400px;
    height: 2px;
    border: none;
    background-color: #e8aa23;
    margin-bottom: 50px;
  }

  .update-profile-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }

  input.nickname {
    border: none;
    width: 395px;
    padding: 5px;
    padding-right: 0px;
    font-size: 20px;
    border-bottom: solid 1px black;
    margin-bottom: 40px;
  }
  input.nickname:focus{
    outline: none;
  }

  .update-profile-filebox{
    display: flex;
    justify-content: space-between;
    width: 400px;
    margin-bottom: 20px;
    margin-top:20px;
  }

  .update-profile-filebox label {
      display: inline-block;
      padding: 10px 20px;
      color: #fff;
      vertical-align: middle;
      background-color: #999999;
      cursor: pointer;
      height: 22px;
      margin-left: 10px;
  }

  .update-profile-filebox .update-profile-upload-name {
    display: inline-block;
    width: 225px;
    height: 40px;
    padding: 0 10px;
    vertical-align: middle;
    border: 1px solid #dddddd;
    color: #999999;
  }
  .update-profile-filebox input[type="file"] {
      position: absolute;
      width: 0;
      height: 0;
      padding: 0;
      overflow: hidden;
      border: 0;
  }

  .nickname-box {
    display: flex;
    width: 358px;
    margin-bottom: 20px;
  }

  .update-submit-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    justify-content: center;
  }

  .update-submit-box input {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 10px;
    width: 130px;
    height: 50px;
  }
  .button {
    background-color :#e8aa23;
    border: 0;
    font-size: 16px;
    cursor: pointer;
    font-weight: 600;
  }
</style>