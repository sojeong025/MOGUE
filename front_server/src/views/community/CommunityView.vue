<template>
  <div id="community-section">
    <div class="header-section">
      <h1 class="part-title">TODAY'S ARTICLES</h1>
    </div>
    <div class="content-section">
      <div class="editor-article-section">
        <EditorArticleList/>
      </div>
      <hr>
      <div class="user-article-section">
        <router-link :to="{ name: 'articlecreate', params: { method: 'post'} }" v-if="token">[게시글 작성]</router-link>
        <router-link :to="{ name: 'login' }" v-else>[게시글 작성]</router-link>
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
  display: flex;
  flex-direction: column;
  margin-top: 180px;
  word-break: keep-all;
}
.part-title{
  font-size: 28px;
  text-align: end;
}
.header-section {
  display: flex;
  padding: 20px 50px 10px;
}
.content-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.editor-article-section {
  display: flex;
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  background-color: #e8aa23;
}

.user-article-section {
  padding: 10px;
}
</style>
