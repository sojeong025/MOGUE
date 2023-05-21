<template>
  <div>
    <h2>UserArticle</h2>
    <UserArticleListItem
    v-for="user_article in user_articles" :key="user_article.id" :user_article="user_article" @delete="article_delete"/>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import UserArticleListItem from '@/components/UserArticleListItem'

export default {
  name: 'UserArticleList',
  components: {
    UserArticleListItem,
  },
  data() {
    return {
      user_articles: [],
    }
  },
  created() {
    this.getUserArticles()
  },
  methods: {
    getUserArticles(){
      axios({
        method: 'get',
        url: `${API_URL}/community/user_articles`
      })
      .then((res) => {
        this.user_articles = res.data
      })
      .catch(err => console.log(err))
    },
    delete(user_article) {
      this.user_article.pop(user_article)
    }
  },
}
</script>

<style>

</style>