<template>
  <div id="community-section">
    <div class="header-section">
      <h1>Community</h1>
      <router-link :to="{ name: 'articlecreate', params: { method: 'post'} }" v-if="token">[CREATE]</router-link>
      <router-link :to="{ name: 'login' }" v-else>[CREATE]</router-link>
    </div>
    <div class="content-section">
      <div class="editor-article-section">
        <EditorArticleList/>
      </div>
      <hr>
      <div class="user-article-section">
        <UserArticleList/>
      </div>
    </div>
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
#community-section {
  margin-top: 130px;
  text-align: center;
}
.header-section {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 10px;
}
.content-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.editor-article-section {
  width: 40%;
  padding: 10px;
  margin-bottom: 20px;
}

.user-article-section {
  width: 60%;
  padding: 10px;
}
</style>
