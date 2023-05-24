<template>
  <div class="user-article-list">
    <div class="card" v-for="user_article in user_articles[page]" :key="user_article.id">
      <div class="left">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
          <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
          <p class="user-article-title">{{ user_articles[0+page].title }}</p>
        </router-link>
      </div>

      <div class="right">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
          <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
          <p class="user-article-title">{{ user_articles[0+page].title }}</p>
        </router-link>
      </div>

      <div class="center">
        <ul>
          <div>
            <li>
              <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
                <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
                <p class="user-article-title">{{ user_articles[0+page].title }}</p>
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
                <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
                <p class="user-article-title">{{ user_articles[0+page].title }}</p>
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
                <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
                <p class="user-article-title">{{ user_articles[0+page].title }}</p>
              </router-link>
            </li>
            <li>
              <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
                <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="300px" height="300px">
                <p class="user-article-title">{{ user_articles[0+page].title }}</p>
              </router-link>
            </li>
          </div>
        </ul>
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
        url: `${API_URL}/community/user_articles`
      })
      .then((res) => {
        this.user_articles = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
.main-container {
  display: flex;
}
.user-article-title{
  text-align: center;
}
.user-article-img{
  width:300px;
  height:300px;
}

.user-article-list{
  display: flex;
  justify-content: space-between;
}
.left{
  justify-items: center;
  align-content: center;
}
.left li {
  width: 400px;
  height: 442px;
  border: 1px solid black;
  list-style: none;
}
.center {
  display: flex;
  flex-direction: row;
}
.center li {
  width: 400px;
  height: 220px;
  border: 1px solid black;
  list-style: none;
}
.right li {
  width: 400px;
  height: 442px;
  border: 1px solid black;
  list-style: none;
}
</style>
