<template>
      <router-link :to="{ name: 'collectiondetail', params: {id: collection.id, collection: collection} }" id="collection-item">
        <div id="color-box"></div>
        <div id="collection-title">
          <h2 id="collection-title-text">{{ collection.title }}</h2>
        </div>
        <img id="collection-thumbnail" :src="`http://127.0.0.1:8000/media${collection.thumbnail}`" alt="thumbnail">
      </router-link>
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
    border-radius: 8px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 400px;
    margin: 40px;
  }

  #color-box {
    border-radius: 8px;
    position:absolute;
    width: 360px;
    height: 360px;
    background-color: rgba(0, 0, 0, 0.37);
  }

  #collection-title {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    color: white;
    width: 300px;
    height: 250px;
    letter-spacing: 4px;
    word-spacing: 8px;
    line-height: 70px;
  }

  #collection-title-text {
    display: flex;
    justify-content: center;
    align-items: center;
  }


  #collection-thumbnail {
    border-radius: 8px;
    width: 360px;
    height: 360px;
  }
</style>