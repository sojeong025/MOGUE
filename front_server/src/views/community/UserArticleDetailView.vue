<template>
  <div>
    <h1>UserArticleDetail</h1>
    <router-link :to="{ name :'community'}">[Community]</router-link>
    <div class="container">
      <p>글 번호 : {{ user_article?.id }}</p>
      <p>작성자 : {{ user_article?.user.nickname}}</p>
      <p>작성시간 : {{ user_article?.created_at }}</p>
      <p>제목 : {{ user_article?.title }}</p>
      <img v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="100px" height="100px">
      <p>내용 : {{ user_article?.content }}</p>

      <button>수정</button>
      <button @click="deleteUserArticle">삭제</button>
      </div>
    <!-- <div class="comment">
      <form id="comment-form" @keyup.enter="createComment" @submit.prevent="createComment">
        <label for="content"></label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
        <input type="submit" value="작성">
      </form>
    </div>
    <h3>댓글목록</h3>
    <div v-for="comment in comments" :key="comment.id">
      {{comment.content}} <button @click="deleteComment(comment.id)">X</button>
    </div>  -->
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
const token = localStorage.getItem('token')

export default {
  name: 'UserArticleDetailView',
  data() {
    return {
      user_article : Object,
      // content : null,
      // method: null,
      // comments : [],
    }
  },
  created(){
    this.getUserArticleDetail()
    // this.getCommentList()
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
        this.user_article = res.data
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
        this.$router.push({ name: 'community' })
      })
      .catch(err => console.log(err))
    },
  //   getCommentList(){
  //     axios({
  //       method: 'get',
  //       url: `${API_URL}/community/${this.$route.params.id}/comments`,
  //     })
  //     .then((res) => {
  //       this.comments = res.data
  //     })
  //     .catch(err => console.log(err))
  //   },
  //   createComment(){
  //     const content = this.content

  //     if (!content) {
  //       alert('내용 입력')
  //       return
  //     }
  //     axios({
  //       method: 'post',
  //       url: `${API_URL}/user_article/${this.user_article.id}/comments`,
  //       data: { content },
  //       headers: {
  //         Authorization: `Token ${this.$store.state.token}`
  //       } 
  //     })
  //     .then((res) => {
  //       this.comments.push(res.data)
  //       this.content = ''
  //     })
  //     .catch(err => console.log(err))
  //   },
  //   deleteComment(comment_id){
  //     axios({
  //       method: 'delete',
  //       url: `${API_URL}/community/comment/${comment_id}`,
  //     })
  //     .then((res) => {
  //       this.comments.pop(res.data)
  //     })
  //     .catch(err => console.log(err))
  //   },
  }
}
</script>

<style>

</style>