<template>
  <div class="write-page">
    <form id="article-form" @submit.prevent="createArticle">
      <div>
      <h1>게시글 작성</h1>
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model="title">
      </div>
      <br>
      <div>
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
        <input type="file" name="img" id="img" @change="handleImgChange" accept="image/*">
        <input type="submit" id="submit" value="작성">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const API_URL = 'http://127.0.0.1:8000'
const token = this.$store.state.token

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title : null,
      content : null,
      img : null,
      method: 'post',
      url: `${API_URL}/community/user_articles/create/`,
    }
  },
  methods: {
    createArticle() {
      const formData = {
        user: jwtDecode(token).user_id, // 초기값은 null로 설정합니다.
        movie: 38,
        title: '제목',
        content: '내용',
        img: this.img
      }
      if (formData.title && formData.content) {
        axios({
          method: 'post',
          url: `${API_URL}/community/user_articles/create/`,
          data: formData,
          headers: {
            Authorization: `JWT ${token}`
          }
        })
        .then(res => {
          console.log(res)
          console.log('성공')
        })
        .catch(err => {
          console.log(err)
          console.log('실패')
        })
      }
    },
    handleImgChange(event) {
      this.img = event.target.files[0]
    },
  },
}
</script>

<style>
.write-page {
  padding: 0px;
  margin: 50px auto;
  width: 800px;
  height: 800px;
  border: 1px solid black;
}
#article-form {
  display: flex;

}
</style>