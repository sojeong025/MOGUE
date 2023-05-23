<template>
    <div id="collection-item">
      <router-link :to="{ name: 'collectiondetail', params: {id: collection.id, collection: collection} }">
        <img id="collection-thumbnail" :src="`http://127.0.0.1:8000${collection.thumbnail}`" alt="thumbnail">
        <p>{{ collection.title }}</p>
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
  #collection-item {
    display: flex;
    width: 400px;
    margin: 10px;
  }

  #collection-thumbnail {
    width: 400px;
    height: 300px;
  }
</style>