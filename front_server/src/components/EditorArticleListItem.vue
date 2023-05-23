<template>
  <div class="editor-article">
    <div class="card">
      <router-link :to="{ name: 'editorarticledetail', params: { id: editor_article.id, editor_article: editor_article } }">
        <img :src="editor_article.thumbnail" class="card-img" alt="thumbnail">
        <div class="card-content">
          <h5 class="card-title"><span>{{ editor_article.title }}</span></h5>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EditorArticleListItem',
  props: {
    editor_article: Object,
  },
};
</script>

<style scoped>
.card{
  flex-basis: 150px;
  margin: 0 10px;
}
.card-content{

}
</style>
