<template>
  <div class="editor-article-list">
    <ul class="editor-articles">
      <li class="editor-article">
        <EditorArticleListItem
          v-for="editor_article in editor_articles"
          :key="editor_article.id"
          :editor_article="editor_article"
        />
      </li>
    </ul>
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
  methods: {
    getEditorArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/community/editor_articles`
      })
        .then((res) => {
          this.editor_articles = res.data
        })
        .catch(err => console.log(err))
    }
  },
  created(){
    this.getEditorArticles()
  }
}
</script>

<style>
.editor-article-list {
  display: flex;
  justify-content: center;
  align-items: center;
}
li {
  list-style-type: none;
}
.editor-article {
  background-color: aqua ;
  display: flex;
  justify-content: center;
}
</style>