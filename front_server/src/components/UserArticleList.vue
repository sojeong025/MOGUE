<template>
  <div class="collection-list">
    <div class="collection" v-for="user_article in user_articles" :key="user_article.id">
      <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article } }">
        <div class="collection-thumbnail">
          <img class="user-article-img" v-if="user_article?.img" :src="`http://127.0.0.1:8000${user_article?.img}/`" onerror="this.src='http://127.0.0.1:8000/default_thumbnail.png/'">
        </div>
        <div class="title">
          <p>{{ user_article.title }}</p>
        </div>
        <div class="article-info">
          <span>{{ user_article.created_at}}</span> 
          <span class="view-detail">VIEW DETAIL ></span>
        </div>
      </router-link>
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
  // props: {
  //   page : Number,
  // },
  created() {
    this.getUserArticles()
  },
  methods: {
    getUserArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/community/user_articles/`
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
.collection-list {
  display: flex;
  flex-wrap: wrap;
  width: 1400px;
}
.user-article-img {
  width: 400px;
  height: 370px;
}
.collection{
  margin: 30px;
}
.top{
  display: flex;
  justify-content: center;
}
.bottom{
  display: flex;
  justify-content: center;
}
.title{
  margin-top:10px;
  width: 370px;
  text-overflow:ellipsis ;
  margin-left: 8px;
  overflow: hidden;
  white-space: nowrap;
}
.article-info {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-top: 5px;
  margin-left: 10px;
  margin-right: 10px;
  font-size: 16px;
}

.article-info span {
  margin-bottom: 20px;
}

.view-detail {
  width: 122px;
  border-bottom: 1px solid gray;
}
</style>
