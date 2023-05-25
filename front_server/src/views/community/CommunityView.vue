<template>
  <div id="community-section">
    <div class="community-headers">
      <img class="community-header-img" :src="`http://127.0.0.1:8000/에에엥.jpg`" alt="">
    </div>
    <div class="header-section">
      <h1 class="part-title">TODAY'S ARTICLES</h1>
    </div>
    <div class="content-section">
      <div class="editor-article-section">
        <EditorArticleList/>
      <div class="box"></div>
      </div>
      <div class="write-section">
        <router-link class="write-article" :to="{ name: 'articlecreate', params: { method: 'post'} }" v-if="token">Write Your Article</router-link>
        <router-link class="write-article" :to="{ name: 'login' }" v-else>Write Your Article</router-link>
      </div>
      <div class="user-article-section">
        <!-- <UserArticleList class="user-articles" :page="page-1+page_index_plus" v-for="page in total_page" :key="page" @page_plus="pagePlus"/> -->
        <UserArticleList class="user-articles"/>
      </div>
    </div>
  </div>
</template>

<script>
import EditorArticleList from '@/components/EditorArticleList'
import UserArticleList from '@/components/UserArticleList'
// import axios from 'axios'

export default {
  name: 'CommunityView',
  data() {
    return{
      token: localStorage.getItem('token'),
      // total_page: null,
      // page_index_plus: 0,
    }
  },
  components: {
    EditorArticleList,
    UserArticleList,
  },
  // methods: {
  // },
  // created() {
  //   axios({
  //     method: 'get',
  //     url: 'http://127.0.0.1:8000/community/user_articles/'
  //   })
  //   .then((res) => {
  //     this.total_page = Math.floor(res.data.length/6)
  //   })
  // }
}
</script>

<style scoped>
#community-section {
  display: flex;
  flex-direction: column;
  word-break: keep-all;
}
.part-title{
  font-size: 32px;
  font-weight: 100;
  margin-left: 20px;
  text-align: end;
}
.header-section {
  display: flex;
  margin-top: 60px;
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
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  width: 100%;
}

.write-article{
  display: flex;
  align-items: center;
  justify-content: center;
  width: 340px;
  height: 50px;
  background-color: #e8aa23;
  line-height : 50px;
  font-weight: 700;
  margin-top: 80px;
  border-radius: 6px;
  cursor: pointer;
  color: white;
  text-align: center;
  font-size: 30px;
  font-weight: 100;
}

.write-article:hover {
  background-color: rgb(255, 190, 48);
}

.community-header-img {
  width: 2133px;
  height: 680px;
}

.user-articles {
  margin-top: 30px;
  margin-bottom: 30px;
  justify-content: center;
}

.write-section {
  display: flex;
  justify-content: center;
  width: 100%px;
}
</style>
