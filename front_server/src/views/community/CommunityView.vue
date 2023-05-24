<template>
  <div id="community-section">
    <div class="community-headers">
      <img class="community-header-img" :src="`http://127.0.0.1:8000/잡지.jpg`" alt="">
    </div>
    <div class="header-section">
      <h1 class="part-title">| TODAY'S ARTICLES</h1>
    </div>
    <div class="content-section">
      <div class="editor-article-section">
        <EditorArticleList/>
        <div class="box"></div>
      </div>
        <div class="write-article">
          <router-link :to="{ name: 'articlecreate', params: { method: 'post'} }" v-if="token">Write Your Article</router-link>
          <router-link :to="{ name: 'login' }" v-else>Write Your Article</router-link>
        </div>
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

<style scoped>
#community-section {
  display: flex;
  flex-direction: column;
  word-break: keep-all;
}
.part-title{
  font-size: 28px;
  text-align: end;
}
.header-section {
  display: flex;
  padding: 20px 120px 10px;
}
.content-section {
  margin: 0px 100px 20px;
}
.editor-article-section {
  width: 100%;
  padding: 10px;
  margin-bottom: 50px;
  position:relative;
  text-align: center;
}

.box{
  width: 103.7vw;
  height: 300px;
  background-color:#dededc77;
  position:absolute;
  top:20%;
  left:-10%
}
.user-article-section {
  padding: 10px;
}
.write-article{
  width: 100%;
  height: 50px;
  background-color: #e8aa23;
  text-align: center;
  line-height : 50px;
  font-weight: 700;
}

.community-header-img {
  width: 100vw;
}
</style>
