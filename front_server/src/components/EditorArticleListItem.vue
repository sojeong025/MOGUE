<template>
  <div class="swiper-slide">
    <div class="card">
      <router-link :to="{ name: 'editorarticledetail', params: { id: editor_article.id, editor_article: editor_article } }">
        <img :src="editor_article.thumbnail" class="card-img" alt="thumbnail">
        <div class="card-content">
          <h5 class="card-title">{{ editor_article.title }}</h5>
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
.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
  background-color: #fff;
  overflow: hidden;
}

.card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-img {
  width: 100%;
  height: auto;
  object-fit: cover;
}

.card-content {
  padding: 16px;
}

.card-title {
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 18px;
  font-weight: bold;
}
</style>
