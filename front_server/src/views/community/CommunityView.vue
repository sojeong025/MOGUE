<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'articlecreate', params: { method: 'post'} }" v-if="token">[CREATE]</router-link>
    <router-link :to="{ name: 'login' }" v-else>[CREATE]</router-link>
    <EditorArticleList/><hr>
    <UserArticleList/>
  </div>
</template>

<script>
import EditorArticleList from '@/components/EditorArticleList'
import UserArticleList from '@/components/UserArticleList'

export default {
  name: 'CommunityView',
  data() {
    return{
      token: localStorage.getItem('token')
    }
  },
  components: {
    EditorArticleList,
    UserArticleList,
  }
}
</script>

<style>
  
</style>