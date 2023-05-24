<template>
  <div class="collection-list">
    <div class="left">
      <div class="collection1">
        <router-link :to="{ name: 'collectiondetail' }">
          <div class="collection1-title">
            <h1>{{collections[0].title}}</h1>
          </div>
          <img class="collection-left-thumbnail" :src="`http://127.0.0.1:8000/${collections[0].thumbnail}`" alt="">
        </router-link>
      </div>
    </div>
    <div class="right">
      <div class="collection2">
        <router-link :to="{ name: 'collectiondetail' }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[1].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p>{{collections[1].title}}</p>
          </div>
        </router-link>
      </div>
      <div class="collection3">
        <router-link :to="{ name: 'collectiondetail' }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[2].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p>{{collections[2].title}}</p>
          </div>
        </router-link>
      </div>
      <div class="collection4">
        <router-link :to="{ name: 'collectiondetail' }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[3].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p>{{collections[3].title}}</p>
          </div>
        </router-link>
      </div>
      <div class="collection5">
        <router-link :to="{ name: 'collectiondetail' }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[4].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p>{{collections[4].title}}</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

// import CollectionListItem from './CollectionListItem'

export default {
  name: 'CollectionList',
  components: {
    // CollectionListItem,
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

<style scoped>
  a {
    padding: 0px;
    width: 100%;
    height: 100%;
  }

  .collection-left-thumbnail {
    width: 100%;
    height: 100%;
  }

  .collection-right-thumbnail {
    width: 100%;
    height: 70%;
  }

  .collection-right-thumbnail img {
    width: 100%;
    height: 100%;
  }

  .collection-list {
    /* border: 1px solid blue; */
    display: flex;
    margin-top: 0px;
    width: 1260px;
    height: 690px;
  }

  .left{
    display: flex;
    margin-right: 25px;
    height: 100%;
  }

  .right {
    display: flex;
    flex-wrap: wrap;
    height: 100%;
  }

  .collection1 {
    display: flex;
    position: relative;
    flex-wrap: wrap;
    /* border: 1px solid red; */
    width: 500px;
    height: 100%;
  }

  .collection1-title {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.219);
    color: white;
    position: absolute;
  }

  .collection1-title h1 {
    margin-top: 600px;
    margin-left: 40px;
    font-weight: 100;
  }

  .collection2 {
    display: flex;
    flex-wrap: wrap;
    margin-right: 25px;
    margin-bottom: 40px;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection3 {
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 40px;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection4 {
    display: flex;
    flex-wrap: wrap;
    margin-right: 25px;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection5 {
    display: flex;
    flex-wrap: wrap;
    /* border: solid 1px purple; */
    width: 350px;
    height: 320px;
  }

  .collection-right-title {
    font-size: 20px;
    margin-top: 20px;
  }
</style>