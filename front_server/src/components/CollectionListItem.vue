<template>
  <div>
      <div id="collection-item">
        <router-link :to="{ name: 'collectiondetail', params: {id: collection.id, collection: collection} }">
          <img :src="`http://127.0.0.1:8000/media/겨울.png`" alt="thumbnail">
          <p>{{ collection.title }}</p>
        </router-link>
      </div>
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
    width: 280px;
    margin: 20px;
    
  }
</style>