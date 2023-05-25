<template>
  <div class="collection-list">
    <div class="right">
      <div class="collection2">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[1].id, user_article: user_articles[1] } }">
          <div class="collection-right-thumbnail">
            <img class="user-article-img" v-if="user_articles[1]?.img" :src="`http://127.0.0.1:8000${user_articles[1]?.img}/`" alt="img" width="300px" height="300px">
          </div>
          <div class="coq-right-title">
            {{ user_articles[1].title }}
          </div>
        </router-link>
      </div>
      <div class="collection3">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[2].id, user_article: user_articles[2]} }">
          <div class="collection-right-thumbnail">
            <img class="user-article-img" v-if="user_articles[2]?.img" :src="`http://127.0.0.1:8000${user_articles[2]?.img}/`" alt="img" width="300px" height="300px">
          </div>
          <div class="coq-right-title">
            {{ user_articles[2].title }}
          </div>
        </router-link>
      </div>
      <div class="collection4">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[3].id, user_article: user_articles[3]} }">
          <div class="collection-right-thumbnail">
            <img class="user-article-img" v-if="user_articles[3]?.img" :src="`http://127.0.0.1:8000${user_articles[3]?.img}/`" alt="img" width="300px" height="300px">
          </div>
          <div class="coq-right-title">
            {{ user_articles[3].title }}
          </div>
        </router-link>
      </div>
      <div class="collection5">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[4].id, user_article: user_articles[4]} }">
          <div class="collection-right-thumbnail">
            <img class="user-article-img" v-if="user_articles[4]?.img" :src="`http://127.0.0.1:8000${user_articles[4]?.img}/`" alt="img" width="300px" height="300px">
          </div>
          <div class="coq-right-title">
            {{ user_articles[4].title }}
          </div>
        </router-link>
      </div>
    </div>
    <div class="left">
      <div class="collection1">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[0].id, user_article: user_articles[0]} }">
          <div class="collection1-title">
            <h1>{{ user_articles[0].title }}</h1>
          </div>
          <img class="collection-left-thumbnail" v-if="user_articles[0]?.img" :src="`http://127.0.0.1:8000${user_articles[0]?.img}/`" alt="img">
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UserArticleList',
  data() {
    return {
      user_articles: [],
    }
  },
  props: {
    page : Number,
  },
  created() {
    this.getUserArticles()
  },
  methods: {
    getUserArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/community/user_articles/pages/${this.page}/`
      })
      .then((res) => {
        console.log(res.data)
        this.user_articles = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
  a {
    padding: 0px;
    width: 100%;
    height: 100%;
  }

  .collection-left-thumbnail {
    width: 100%;
    height: 100%;
  }

  .collection-right-thumbnail {
    width: 100%;
    height: 70%;
  }

  .collection-right-thumbnail img {
    width: 100%;
    height: 100%;
  }

  .collection-list {
    /* border: 1px solid blue; */
    display: flex;
    margin-top: 0px;
    width: 1260px;
    height: 690px;
  }

  .left{
    display: flex;
    margin-right: 25px;
    height: 100%;
  }

  .right {
    display: flex;
    flex-wrap: wrap;
    height: 100%;
  }

  .collection1 {
    display: flex;
    position: relative;
    flex-wrap: wrap;
    /* border: 1px solid red; */
    width: 500px;
    height: 100%;
  }

  .collection1-title {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.219);
    color: white;
    position: absolute;
  }

  .collection1-title h1 {
    margin-top: 600px;
    margin-left: 40px;
    font-weight: 100;
  }

  .collection2 {
    display: flex;
    flex-wrap: wrap;
    margin-right: 25px;
    margin-bottom: 40px;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection3 {
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 40px;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection4 {
    display: flex;
    flex-wrap: wrap;
    margin-right: 25px;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection5 {
    display: flex;
    flex-wrap: wrap;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection-right-title {
    font-size: 22px;
    margin-top: 20px;
  }

  .collection-item {
    font-size: 14px;
    color: rgb(61, 61, 61);
    margin-right: 6px;
  }
</style>
