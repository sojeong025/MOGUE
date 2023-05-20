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
const API_URL = 'http://127.0.0.1:8000'

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
      const title = this.title
      const content = this.content

    if (!title) {
      alert('제목 입력')
      return
    } else if (!content) {
      alert('내용 입력')
      return
    }

    const formData = new FormData()
    formData.append('title', title)
    formData.append('content', content)
    formData.append('img', this.img)
    formData.append('user', this.$localStorage.user)

    axios({
      method: this.method,
      url : this.url,
      data: formData,
      headers:{
        'Content-Type': 'multipart/form-data',
        Authorization: `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      this.$router.push({name: 'userarticledetail', params: {id: res.data.id, user_article: res.data} })
    })
    .catch((err) => console.log(err))
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