<template>
  <div>
    <h1>UserArticleDetail</h1>
    <router-link :to="{ name :'community'}">[Community]</router-link>
    <div class="container">
      <p>글 번호 : {{ user_article?.id }}</p>
      <p>작성자 : {{ user_article?.username}}</p>
      <p>작성시간 : {{ user_article?.created_at }}</p>
      <p>제목 : {{ user_article?.title }}</p>
      <img v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="100px" height="100px">
      <p>내용 : {{ user_article?.content }}</p>
      <p>작성시간 : {{ user_article?.created_at }}</p>
      <router-link :to="{ name: 'articlecreate', params: { user_article: user_article } }"><button>수정</button></router-link>
      <button @click="deleteUserArticle">삭제</button>
      </div>
    <div class="comment">
      <form id="comment-form" @keyup.enter="createComment" @submit.prevent="createComment">
        <label for="content"></label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
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
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UserArticleDetailView',
  data() {
    return {
      user_article : Object,
      content : null,
      method: null,
      comments : [],
    }
  },
  created(){
    this.method = 'get'
    this.getUserArticleDetail()
    this.getCommentList()
  },
  methods: {
    getUserArticleDetail() {
      axios({
        method: this.method,
        url: `${API_URL}/community/user_articles/${this.$route.params.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        if (res.status === 204) {
          this.$router.push({name: 'community'})
        } else {
          this.user_article = res.data
        }
      })
      .catch((err) => {
        if (err.response.status === 400) {
          alert('니꺼 아니다')
        }
      })
    },
    deleteUserArticle() {
      this.method = 'delete'
      this.getUserArticleDetail()
    },
    getCommentList(){
      axios({
        method: 'get',
        url: `${API_URL}/community/${this.$route.params.id}/comments`,
      })
      .then((res) => {
        this.comments = res.data
      })
      .catch(err => console.log(err))
    },
    createComment(){
      const content = this.content

      if (!content) {
        alert('내용 입력')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/user_article/${this.user_article.id}/comments`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        } 
      })
      .then((res) => {
        this.comments.push(res.data)
        this.content = ''
      })
      .catch(err => console.log(err))
    },
    deleteComment(comment_id){
      axios({
        method: 'delete',
        url: `${API_URL}/community/comment/${comment_id}`,
      })
      .then((res) => {
        this.comments.pop(res.data)
      })
      .catch(err => console.log(err))
    },
  }
}
</script>

<style>

</style>