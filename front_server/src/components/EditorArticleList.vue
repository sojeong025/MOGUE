<template>
  <div class="editor-article-list">
    <ul class="editor-articles">
      <li class="editor-article" v-for="editor_article in editor_articles" :key="editor_article.id">
        <div class="card">
          <router-link :to="{ name: 'editorarticledetail', params: { id: editor_article.id, editor_article: editor_article } }">
            <img :src="editor_article.thumbnail" class="card-img" alt="thumbnail">
            <div class="card-content">
              <h5 class="card-title"><span>{{ editor_article.title }}</span></h5>
            </div>
          </router-link>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'EditorArticleList',
  data() {
    return {
      editor_articles: [],
    }
  },
  methods: {
    getEditorArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/community/editor_articles/random/`,
        params: {
          count: 9,
        }
      })
      .then((res) => {
        this.editor_articles = res.data
      })
      .catch(err => console.log(err))
    }
  },
  created() {
    this.getEditorArticles()
  }
}
</script>

<style scoped>
.editor-article-list {
  display: flex;
  width: 100%;
  font-family: 'SUITE-Regular';
}
li {
  list-style-type: none;
}
.editor-article {
  display: flex;
  width: 400px;
  justify-content: center;
  flex-direction: row;

}

.editor-articles {
  display: flex;
  flex-wrap: wrap;
}

.card {
  flex-basis: 150px;
  margin: 0 10px;
}

</style>
