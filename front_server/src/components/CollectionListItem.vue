<template>
      <router-link :to="{ name: 'collectiondetail', params: {id: collection.id, collection: collection} }" id="collection-item">
        <div id="color-box"></div>
        <div id="collection-title">
          <h2 id="collection-title-text">{{ collection.title }}</h2>
        </div>
        <img id="collection-thumbnail" :src="`http://127.0.0.1:8000${collection.thumbnail}`" alt="thumbnail">
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
@font-face {
    font-family: 'ghanachoco';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/ghanachoco.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
  #collection-item {
    border-radius: 8px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 320px;
    margin: 20px;
    box-shadow: 10px 10px 10px 0px rgba(128, 128, 128, 0.336);
  }

  #color-box {
    /* border-radius: 8px; */
    position:absolute;
    width: 320px;
    height: 320px;
    background-color: rgba(0, 0, 0, 0.37);
  }
  #collection-item:hover {
    filter: brightness(0.5);
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
    /* word-spacing: 8px; */
    line-height: 50px;
  }

  #collection-title-text {
    display: flex;
    justify-content: center;
    word-break: keep-all;
    text-align: center;
    align-items: center;
    font-family: 'ghanachoco';
  }


  #collection-thumbnail {
    /* border-radius: 8px; */
    width: 320px;
    height: 320px;
  }
</style>