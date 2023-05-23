<template>
  <div id="community-section">
    <div class="header-section">
      <h1>Community</h1>
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
  margin-top: 180px;
  text-align: center;
  font-family: 'SUITE-Regular';
  align-items: center;
  justify-content: center;
  word-break: keep-all;
}
.header-section {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
}
.header-section h1 {
  text-align: center;
  padding-bottom: 20px;
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
