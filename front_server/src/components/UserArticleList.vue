<template>
  <div>
    <h2>UserArticle</h2>
    <UserArticleListItem
    v-for="user_article in user_articles" :key="user_article.id" :user_article="user_article"/>
  </div>
</template>

<script>
import UserArticleListItem from '@/components/UserArticleListItem'

export default {
  name: 'UserArticleList',
  components: {
    UserArticleListItem,
  },
  computed: {
    user_articles(){
      return this.$store.state.user_articles
    }
  }
}
</script>

<style>

</style>