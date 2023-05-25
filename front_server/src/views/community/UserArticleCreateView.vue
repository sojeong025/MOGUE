<template>
  <div >
    <form class="write-page" @submit.prevent="createArticle">
      <div id="article-form-left" >
        <h1>Write Your Article</h1>
          <hr>
          <h3>title</h3><br>
          <input type="text" id="title" v-model="title" placeholder="기사 제목을 작성하세요"><br>
          <div class="filebox">
            <input class="upload-name" disabled v-model="fileName" value="첨부파일" placeholder="첨부파일">
            <label for="file">파일찾기</label>
            <input type="file" id="file" @change="handleImgChange" accept="image/*" multiple>
          </div>
      </div>
      <hr class="hr2">
      <div id="article-form-right" >
        <div class="content">
          <h3>Content</h3><br>
          <textarea id="content" cols="50" rows="11" v-model="content" placeholder="기사 내용을 작성하세요"></textarea><br>
        </div>
          <input type="submit" id="submit" value="SUBMIT">
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
      // preview: '',
      fileName: '첨부파일',
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
        img: this.img,
        // preview: this.preview,
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
      this.fileName = event.target.files[0].name
      // this.preview = URL.createObjectURL(this.event.target.files[0])
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

<style scoped>
.write-page {
  padding: 0px;
  margin: 70px auto;
  margin-top: 100px;
  width: 1400px;
  height: 700px;
  display: flex;
  flex-direction: row;
  box-shadow: 8px 8px 20px #62646469;
}
#article-form-left {
  margin: 40px;
  width: 40%;
}
#article-form-left h1 {
  margin: 30px 20px 10px;
  font-size: 30px;
}
#article-form-left hr{
  width: 50%;
  background-color:#e8aa23;
  height: 4px;
  border: 0;
  margin-left: 20px;
}
#article-form-left input#title{
  margin: 0px 20px 20px;
  border: 0;
  width: 400px;
  height: 30px;
  padding: 5px;
  border-bottom:1px solid black;
  font-size: 20px;
}
#article-form-left input#img{
  margin: 10px 30px 20px;
}
.filebox .upload-name {
  display: inline-block;
  height: 40px;
  padding: 0 10px;
  vertical-align: middle;
  border: 1px solid #dddddd;
  margin-left: 20px;
  width: 60%;
  color: #999999;
}
.filebox label {
  display: inline-block;
  padding: 10px 20px;
  color: #fff;
  vertical-align: middle;
  background-color: #999999;
  cursor: pointer;
  height: 22px;
  margin-left: 10px;
}
.filebox input[type="file"] {
  position: absolute;
  width: 0;
  height: 0;
  padding: 0;
  overflow: hidden;
  border: 0;
}

#article-form-left input:focus {
  outline: none;
}
#article-form-left h3 {
  margin-left: 20px;
  margin-top: 50px
}
.hr2{
  background-color:#faf5db;
  width: 2px;
  border: 0;
}
#article-form-right { 
    width: 60%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
#article-form-right h3{
  margin: 50px 70px 0px;
}
#article-form-right textarea{
  margin-left: 70px;
  font-size: 20px;
  border: 0;
  resize: none;
  line-height: 35px;
  white-space: pre-line;
  word-break: keep-all;
}
#article-form-right textarea:focus {
  outline: none;
}
#submit {
  margin-bottom: 0;
  height: 50px;
  width: 100%;
  border: 0;
  background-color :#e8aa23;
  font-size: 20px;
} 
</style>