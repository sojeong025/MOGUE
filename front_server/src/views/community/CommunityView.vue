<template>
  <div>
    <h1>Community</h1>
    <EditorArticleList/>
    <UserArticleList/>
  </div>
</template>

<script>
import EditorArticleList from '@/components/EditorArticleList'
import UserArticleList from '@/components/UserArticleList'

export default {
  name: 'CommunityView',
  component: {
    EditorArticleList,
    UserArticleList,
  }
}
</script>

<style>
  
</style>