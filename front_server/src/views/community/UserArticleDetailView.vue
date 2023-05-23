<template>
  <div>
    <h1>UserArticleDetail</h1>
    <router-link :to="{ name :'community'}">[Community]</router-link>
    <div class="container">
      <p>글 번호 : {{ user_article?.id }}</p>
      <p>작성자 : <router-link :to="{ name: 'profile', params: {id: user.pk} }">{{ user.nickname }}</router-link></p>
      <p>작성시간 : {{ user_article?.created_at }}</p>
      <p>제목 : {{ user_article?.title }}</p>
      <img v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="500px" height="500px">
      <p>내용 : {{ user_article?.content }}</p>

      <button @click="updateUserArticle">수정</button>
      <button @click="deleteUserArticle">삭제</button>
      </div>
    <div class="comment">
      <form id="comment-form" @submit.prevent="createComment">
        <label for="content"></label>
        <input id="text" cols="30" rows="10" v-model="content">
        <input type="submit" value="작성">
      </form>
    </div>
    <h3>댓글목록</h3>
    <div v-for="comment in comments" :key="comment.id">
      {{comment.content}} <button @click="deleteComment(comment.id)">X</button>
    </div> 
  </div>
</template>

<script>
import axios from 'axios'
import jwtDecode from "jwt-decode"
const API_URL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('token')

export default {
  name: 'UserArticleDetailView',
  data() {
    return {
      user_article : Object,
      user: Object,
      content : null,
      comments : [],
    }
  },
  created(){
    this.getUserArticleDetail()
  },
  methods: {
    getUserArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/user_articles/${this.$route.params.id}`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.user_article = res.data.user_article
        this.user = res.data.user_article.user
        this.comments = res.data.comments
      })
      .catch(err => console.log(err))
    },
    deleteUserArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/user_articles/${this.$route.params.id}/manage`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then(() =>{
        this.$emit('delete', this.user_article)
        this.$router.push({ name: 'community' })
      })
      .catch(err => console.log(err))
    },
    updateUserArticle() {
      this.$router.push({ name: 'articlecreate', params: { method: 'put', user_article: this.user_article}})
    },

    createComment(){
      const content = this.content
      const formData = {
        content: this.content,
        article: this.user_article.id,
        user: jwtDecode(token).user_id, 
      }
      if (!content) {
        alert('내용을 입력하세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/community/user_articles/${this.user_article.id}/comment/`,
        data: formData,
        headers: {
          Authorization: `JWT ${token}`
        } 
      })
      .then(() => {
        this.getUserArticleDetail()
        this.content = ''
      })
      .catch(err => console.log(err))
    },
    deleteComment(comment_id){
      axios({
        method: 'delete',
        url: `${API_URL}/community/comment/${comment_id}/`,
        headers: {
          Authorization: `JWT ${token}`
        } 
      })
      .then(() => {
        this.getUserArticleDetail()
      })
      .catch(err => console.log(err))
    },
  }
}
</script>

<style>

</style>