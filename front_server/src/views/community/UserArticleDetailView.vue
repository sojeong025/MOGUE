<template>
<div>
<div class="main-container">
  <div class="main-title">
    <router-link id="to-index" :to="{ name: 'community' }">목록으로</router-link>
    <h1>{{ user_article?.title }}</h1>
  </div>
  <div class="user-article">
      <div class="user-article-content">
        <div class="user-article-left">
          <div class="left-up">
          <p id="number">User Article No. {{ user_article?.id }}</p>
          <p class="writer">
            <span>작성자</span>
            <router-link :to="{ name: 'profile', params: {id: user.pk} }">
              <font-awesome-icon :icon="['fas', 'hashtag']" />
              {{ user.nickname }}
            </router-link>
          </p>
          <p class="date"><span id="date">{{ user_article?.created_at }}</span> </p>
          </div>
          <div class="left-down">
            <button class="button" @click="updateUserArticle">수정</button>
            <button class="button" @click="deleteUserArticle">삭제</button>
          </div>
        </div>
        
        <hr class="hr1">

        <div class="user-article-right">
          <div class="article">
            <div >
              <img class="img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
              <p>{{ user_article?.content }}</p>
            </div>

          </div>
        </div>
        </div>


          <div class="comment">
            <div class="comment-left">
              <span>comment</span>
              <form id="comment-form" @submit.prevent="createComment">
                <label for="content"></label>
                <input id="text" v-model="content" placeholder="댓글을 작성하세요">
                <input id="submit" type="submit" value="작성">
              </form>
            </div><hr class="hr">
            <div class="comment-right">
              <div class="comment-content" v-for="comment in comments" :key="comment.id">
                <div>{{comment.content}}</div> <button class="delete-button" @click="deleteComment(comment.id)">X</button>
              </div> 
            </div>
          </div>

    </div>
    </div>
    <FooterSection/>
  </div>
</template>

<script>
import FooterSection from '../../components/FooterSection'

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
  components:{
    FooterSection,
  },
  created(){
    this.getUserArticleDetail()
  },
  methods: {
    getUserArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/community/user_articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        this.user_article = res.data.user_article
        this.user = res.data.user_article.user
        this.comments = res.data.comments
      })
      .catch(err => console.log(err))
    },
    deleteUserArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/community/user_articles/${this.$route.params.id}/manage/`,
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

<style scoped>
.main-container{
  margin: 100px auto;
  width: 1600px;
  /* text-align: center; */
  align-items: center;
  justify-content: center;
}
.main-container h1{
  text-align: center;
  margin: 15px;
  color:#3f3f3f;
  margin-bottom: 30px;  
}
.user-article{
  display: flex;
  flex-direction: column;
  word-break: keep-all;
}
.user-article-content{
  display: flex;
  flex-direction: row;
    /* align-items: center; */
  border-top : 1px solid rgb(187, 184, 184);
  border-bottom : 1px solid rgb(187, 184, 184);
}
.user-article-left{
  margin: 40px;
  flex: 0.5;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.user-article-left p {
  margin-bottom: 6px;
  color: #3f3e3e;
  font-size: 16px
}
.writer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  color: #f3a806;
  padding: 0px;
}

.writer a {
  font-size: 16px;
  color: #f3a806;
  padding: 0px;
}
/* .user-article-left p .writer:hover {
  border-bottom: 1px solid black;
} */
.article{
  display: flex;
  flex-direction: row;
}
.user-article-right{
  display: flex;
  flex: 3;
  margin-top: 20px;
  margin-left: 30px;
  margin-bottom: 20px;
}
.user-article-right img {
  width: 300px;
  height: 300px;
  margin-right: 20px
  /* outline: none; */
}
.user-article-right img:hover {
  transform: scale(1.05);
  transition: .3s ease-in-out;
}
.user-article-right p{
  margin: 10px;
  font-size: 19px;
  line-height: 35px;
  white-space: pre-line;
  word-break: keep-all;
}
.comment {
  margin-left: 20px;
  margin-top: 40px;
}
#text{
  margin-top: 10px;
  padding-left: 0px;
  width: 500px;
  height: 30px;
  border-bottom: 2px solid #e8aa23;
  border :0;
  font-size: 15px
;}
#text:focus{
  outline: none;
  border-bottom:  2px solid #e8aa23;
  background-color: none;
}
#submit{
  margin-left: 8px;
  width: 60px;
  height: 35px;
  background-color: #e8aa23;
  border: none;
  color: white;
  cursor: pointer;
}

.button{
  width: 100px;
  height: 38px;
  background-color: #e8aa23;
  border: none;
  font-size: 16px;
  color: white;
  cursor: pointer;
  justify-content: space-between;
}
.comment-content{
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-left: 30px;
  margin-top: 16px;
}
.comment-content button { 
  width:50px;
  height: 30px;
  margin-left: 20px;
  background-color: #e8aa23;
  border: none;
  color: #fff;
  cursor: pointer;
}
.comment{
  display: flex;
  justify-content: space-between;
}
.comment-left{
  flex: 1;
}
.comment-right{
  display: flex;
  justify-content: space-between;
  flex: 1;
  flex-direction: column;
  align-items: end;
  margin-left: 30px;
  margin-top: 14px;
}
.img{
  float: left;
  padding: 20px;
}

.left-up {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.left-up p{
  font-size: 18px;
}

.date {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

#date {
  font-size: 14px;
}

.left-down {
  display: flex;
  justify-content: space-between;
  width: 220px;
}

#comment-form {
  display: flex;
  justify-content: space-between;
  margin-right: 30px;
  align-items: flex-end;
}

#comment-form input {
  margin-right: 90px;
}

.delete-button {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 50px;
  width: 60px;
  height: 35px;
}

#number {
  margin-bottom: 36px;
}

#to-index {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #e8aa23;
  color: white;
  margin-left: 30px;
  font-weight: 100;
  font-size: 16px;
  width: 60px;
  height: 38px;
}

</style>