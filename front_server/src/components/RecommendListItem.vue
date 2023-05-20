<template>
  <div>
    <h3>RecommendListItem</h3>
    <router-link :to="{ name : 'moviedetail', params : { id: movie.id } }">
    <img :src="movie.poster_path" alt="poster">
    <p>{{ movie.title }}</p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'RecommendListItemView',
}
</script>

<style>

</style>