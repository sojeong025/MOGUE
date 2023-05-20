<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'articlecreate' }">[CREATE]</router-link>
    <EditorArticleList/><hr>
    <UserArticleList/>
  </div>
</template>

<script>
import EditorArticleList from '@/components/EditorArticleList'
import UserArticleList from '@/components/UserArticleList'

export default {
  name: 'CommunityView',
  components: {
    EditorArticleList,
    UserArticleList,
  }
}
</script>

<style>
  
</style>