<template>
  <div>
    <img :src="editor_article.thumbnail" alt="thumbnail">
    <router-link :to="{ name: 'editorarticledetail', params: {id: editor_article.id, editor_article: editor_article} }"><p>{{ editor_article.title }}</p></router-link>
  </div>
</template>

<script>
export default {
  name : 'EditorArticleListItem',
  props: {
    editor_article : Object,
  }
}
</script>

<style>

</style>