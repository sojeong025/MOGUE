<template>
  <div>
    <router-link :to="{ name: 'userarticledetail', params: {id: user_article.id, user_article: user_article} }">
    <p> 제목 : {{ user_article.title }}</p>
    </router-link>
    <p> 내용 : {{ user_article.content }}</p><hr>
  </div>
</template>

<script>
export default {
  name: 'UserArticleListItem',
  props: {
    user_article : Object,
  }
}
</script>

<style>

</style>