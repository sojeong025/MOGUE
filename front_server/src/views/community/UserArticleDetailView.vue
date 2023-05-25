<template>
<div>
<div class="main-container">
  <h1>{{ user_article?.title }}</h1>
  <div class="user-article">
      <div class="user-article-content">
        <div class="user-article-left">
          <div class="left-up">
          <!-- <router-link :to="{ name :'community'}">[Community]</router-link> -->
          <p class="number">article number. {{ user_article?.id }}</p>
          <p class="writer">writer</p>
            <p><router-link class="writer" :to="{ name: 'profile', params: {id: user.pk} }">{{ user.nickname }}</router-link></p>
          <p class="date">date</p>
          <p> {{ user_article?.created_at }}</p>
          </div>
          <div class="left-down">
            <button id="button" @click="updateUserArticle">수정</button>
            <button id="button" @click="deleteUserArticle">삭제</button>
          </div>
        </div>
        
        <hr class="hr1">

        <div class="user-article-right">
          <div class="article">
            <div class="title">
            <img v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
            </div>
            <div class="content">
            <p>{{ user_article?.content }}</p>
            <!-- <i class="fa-sharp fa-solid fa-trash"></i> -->
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
                {{comment.content}} <button class="delete-button" @click="deleteComment(comment.id)">X</button>
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
  margin: 50px;
  flex: 0.5;
  margin: 30px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.user-article-left p {
  margin-bottom: 6px;
  color: #3f3e3e;
  font-size: 16px
}
.user-article-left p .writer {
  font-size: 16px;
  color: #f3a806;
}
.article{
  display: flex;
  flex-direction: row;
}
.user-article-right{
  display: flex;
  flex: 3;
  margin: 50px;
}
.user-article-right img {
  width: 500px;
  height: 100%;
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
  margin: 80px 20px;
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
#button{
  width: 47%;
  height: 35px;
  background-color: #e8aa23;
  border: none;
  margin-right:5px;
  color: white;
  cursor: pointer;
}
.comment-content{
  margin-top: 20px;
}
.comment-content button {
  width:50px;
  height: 30px;
  margin-left: 20px;
  background-color: #e8aa23;
  border: none;
  color: #fff
}
.comment{
  display: flex;
  justify-content: space-between;
}
.comment-right{
  display: flex;
  flex-direction: column;
  align-items: end;
}
</style>