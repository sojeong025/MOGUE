<template>
  <div>
    <h3>CollectionListItem</h3>
    <img :src="`https://image.tmdb.org/t/p/w500/${collection.thumbnail}`" alt="thumbnail">
    <router-link :to="{ name: 'collectiondetail', params: {id: collection.id, collection: collection} }">
      {{ collection.title }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'CollectionListItem',
  props: {
    collection : Object,
  }
}
</script>

<style>

</style>