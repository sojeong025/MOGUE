<template>
  <div class="header">
    <div class="main-container">
      <div class="card" v-for="user_article in user_articles" :key="user_article.id">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
          <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}`" alt="img" width="500px" height="500px">
          <p class="user-article-title">{{ user_article.title }}</p>
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
.card {
  flex: 1;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: center;
}
.user-article-title{
  text-align: center;
}
.user-article-img{
  width:400px;
  height:400px;
}
</style>
