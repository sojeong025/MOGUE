<template>
  <div>
    <h1>EditorArticleList</h1>
    <EditorArticleListItem
    v-for="editor_article in editor_articles" :key="editor_article.id" :editor_article="editor_article"/>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import EditorArticleListItem from '@/components/EditorArticleListItem'

export default {
  name: 'EditorArticleList',
  components: {
    EditorArticleListItem,
  },
  data() {
    return {
      editor_articles: [],
    }
  },
  created() {
    this.getEditorArticles()
  },
  methods: {
    getEditorArticles(){
      axios({
        method: 'get',
        url: `${API_URL}/community/editor_articles`
      })
      .then((res) => {
        this.editor_articles = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>

</style>