<template>
  <div id="editor-article-detail">
    <div class="editor-article-left">
      <h3>영화 기사</h3>
      <h5>number. {{editor_article.id}}</h5>
      <font-awesome-icon :icon="['fas', 'heart']" />
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
      <div v-for="article in editor_articles" :key="article.id" @click="getEditorArticleDetail">
        <router-link class="thumbnail-title" :to="{ name: 'editorarticledetail', params: { id: article.id, article: article } }">
            <img :src="article.thumbnail" width="130px" height="120px" alt="thumbnail">
            <h4 class="title">{{ article.title }}</h4>
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
        url: `${API_URL}/community/editor_articles/${this.$route.params.id}/`,
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
  margin: 100px 300px;
  display: flex;
  flex-direction: row;
}
.editor-article-left{
  flex:0.5;
  margin-right: 40px;
  /* border: 1px solid black; */
}
.editor-article-left h3{
  font-size: 15px;
  padding: 10px 0;
}
.editor-article-left h5{
  color: #626464;
  font-size: 12px;
  font-weight: 300;
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
  margin-left: 40px;
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
}
.title{
  font-size: 17px;
  font-weight: 400;
  margin-left:10px;
  align-self: center;
  line-height: 30px;
  word-break: keep-all;
}
</style>