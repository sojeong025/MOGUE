<template>
  <div>
    <h3>RecommendListItem</h3>
    <router-link :to="{ name : 'moviedetail', params : { id: movie.id, movie: movie } }">
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
      <p>{{ movie.title }}</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'RecommendListItemView',
  props: {
    movie: Object,
  }
}
</script>

<style>

</style>