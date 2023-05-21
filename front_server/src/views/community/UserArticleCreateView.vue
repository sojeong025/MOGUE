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


export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title : null,
      content : null,
      img : null,
      method: this.$route.params.method,
      url: `${API_URL}/community/user_articles/create/`,
    }
  },
  methods: {
    createArticle() {
      const token = localStorage.getItem('token')
      const formData = {
        user: jwtDecode(token).user_id, // 초기값은 null로 설정합니다.
        movie: 38,
        title: this.title,
        content: this.content,
        img: this.img
      }
      console.log(formData.user)
      if (formData.title && formData.content) {
        console.log(this.method)
        if (this.method === 'post') {
          axios({
            method: 'post',
            url: `${API_URL}/community/user_articles/create/`,
            data: formData,
            headers: {
              'Content-Type': 'multipart/form-data',
              Authorization: `JWT ${token}`
            }
          })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'userarticledetail', params: {id: res.data.id, user_article: res.data}})
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
        } else if (this.method === 'put') {
          axios({
            method: 'put',
            url: `${API_URL}/community/user_articles/${this.$route.params.user_article.id}/manage/`,
            data: formData,
            headers: {
              'Content-Type': 'multipart/form-data',
              Authorization: `JWT ${token}`
            }
          })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'userarticledetail', params: {id: res.data.id, user_article: res.data}})
          })
          .catch(err => {
            console.log(err)
            console.log('실패')
          })
        }
      }
    },
    handleImgChange(event) {
      this.img = event.target.files[0]
    },
  },
  created() {
    if (this.$route.params.method === 'put') {
      this.title = this.$route.params.user_article.title
      this.content = this.$route.params.user_article.content
    }
  }
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