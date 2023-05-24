<template>
  <div id="collection-list">
    <CollectionListItem
    v-for="collection in collections" :key="collection.id" :collection="collection" />
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import CollectionListItem from './CollectionListItem'

export default {
  name: 'CollectionList',
  components: {
    CollectionListItem,
  },
  data(){
    return {
      collections: [],
    }
  },
  created(){
    this.getCollections()
  },
  methods: {
    getCollections(){
      axios({
        method: 'get',
        url: `${API_URL}/movies/collections/`
      })
      .then((res) => {
        this.collections = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style>
  #collection-list {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    margin-top: 0px;
    width: 800px;
    display: flex;
    flex-wrap: wrap;
  }
</style>