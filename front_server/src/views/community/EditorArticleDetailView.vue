<template>
  <div>
    <h1>EditorArticleDetail</h1>
    <router-link :to="{ name:'community' }">[community]</router-link>
    <div v-if="editor_article">
      <p v-html="editor_article.rawHTML"></p>
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
      editor_article : null,
    }
  },
  created(){
    this.getEditorArticleDetail()
  },
  methods: {
    getEditorArticleDetail(){
      axios({
        method: 'get',
        url: `${API_URL}/community/editor_articles/${this.$route.params.id}`,
      })
      .then((res) => {
        this.editor_article = res.data
      })
      .catch((err) => console.log(err))
    }
  }
}
</script>

<style>

</style>