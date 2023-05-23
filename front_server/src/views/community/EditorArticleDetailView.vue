<template>
  <div id="editor-article-detail">
    <div class="editor-article-left">
      <h3>일단 자리 잡기</h3>
      <h5>뭐적지?</h5>
    </div>
    <div class="editor-article-center">

      <div v-if="editor_article">
        <div class="article-title">
          <h1>{{ editor_article.title }}</h1>
        </div>

        <div class="article-content">
          <p v-html="editor_article.rawHTML"></p>
        </div>

      </div>
    </div>

    <div class="editor-article-right">
      <h3>더 볼만한 기사</h3>
      <div v-for="article in editor_articles" :key="article.id" class="thumbnail-title" @click="getEditorArticleDetail">
        <router-link :to="{ name: 'editorarticledetail', params: { id: article.id, article: article } }">
          <div class="thumbnail">
            <img :src="article.thumbnail" width="130px" height="120px" alt="thumbnail">
          </div>
          <div class="title">
            <h4 class="title">{{ article.title }}</h4>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'EditorArticleDetailView',
  data(){
    return {
      editor_article : '',
      editor_articles : [],
      id: this.$route.params.id,
    }
  },
  created(){
    this.getEditorArticleDetail()
  },
  methods: {
    getEditorArticleDetail(){
      this.getEditorArticles()
      axios({
        method: 'get',
        url: `${API_URL}/community/editor_articles/${this.$route.params.id}`,
      })
      .then((res) => {
        this.editor_article = res.data
        console.log(res)
      })
      .catch((err) => console.log(err))
    },
    getEditorArticles(){
      axios({
        method: 'get',
        url: `${API_URL}/community/editor_articles/random/`,
        params: {
          count: 5,
        }
      })
      .then((res)=> {
        this.editor_articles = res.data
        console.log(res)
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
#editor-article-detail {
  margin: 200px 100px;
  display: flex;
  flex-direction: row;
}
.editor-article-left{
  flex:0.5;
  /* border: 1px solid black; */
}
.editor-article-left h3{
  font-size: 18px;
  padding: 10px 0;
}
.editor-article-center {
  flex:2;
  /* border: 1px solid black; */
  margin: 0 50px 0;
}
.editor-article-center h1{
  font-weight:900;
  font-size: 35px;
  margin-bottom: 30px;
}
.article-content {
  line-height: 30px;
}
.editor-article-right{
  flex:1.5;
  /* border: 1px solid black; */
}
.editor-article-right h3{
  border-top: 1px solid black;
  border-bottom: 1px solid black ;
  padding: 10px 0;
  font-size: 18px;
  margin-bottom: 20px;
}
.thumbnail-title{
  margin-bottom: 20px ;
  display: flex;
  align-items: center;
  flex-direction: row;
}
.title{
  font-size: 15px;
  font-weight: 400;
  margin-left:10px
}
</style>