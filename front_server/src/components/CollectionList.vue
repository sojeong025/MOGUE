<template>
  <div class="collection-list">
    <div class="left">
      <div class="collection1">
        <router-link :to="{ name: 'collectiondetail', params: {id: collections[1].id, collection: collections[1]} }">
          <div class="collection1-title">
            <h1 class="font">{{collections[1].title}}</h1>
          </div>
          <img class="collection-left-thumbnail" :src="`http://127.0.0.1:8000/${collections[1].thumbnail}`" alt="">
        </router-link>
      </div>
    </div>
    <div class="right">
      <div class="collection2">
        <router-link :to="{ name: 'collectiondetail', params: {id: collections[1].id, collection: collections[0]} }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[0].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p class="collection-right-title-line">{{collections[0].title}}</p>
            <span class="collection-item" v-for="(index, movie) in collections[0].movies.slice(0, 4)" :key="index"> 
              #{{ collections[0].movies[movie] }}
            </span>
          </div>
        </router-link>
      </div>
      <div class="collection3">
        <router-link :to="{ name: 'collectiondetail', params: {id: collections[2].id, collection: collections[2]} }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[2].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p class="collection-right-title-line" >{{collections[2].title}}</p>
            <span class="collection-item" v-for="(index, movie) in collections[2].movies.slice(0, 4)" :key="index"> 
              #{{ collections[2].movies[movie] }}
            </span>
          </div>
        </router-link>
      </div>
      <div class="collection4">
        <router-link :to="{ name: 'collectiondetail', params: {id: collections[3].id, collection: collections[3]} }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[3].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p class="collection-right-title-line">{{collections[3].title}}</p>
            <span class="collection-item" v-for="(index, movie) in collections[3].movies.slice(0, 4)" :key="index"> 
              #{{ collections[3].movies[movie] }}
            </span>
          </div>
        </router-link>
      </div>
      <div class="collection5">
        <router-link :to="{ name: 'collectiondetail', params: {id: collections[4].id, collection: collections[4]} }">
          <div class="collection-right-thumbnail">
            <img :src="`http://127.0.0.1:8000/${collections[4].thumbnail}`" alt="">
          </div>
          <div class="collection-right-title">
            <p class="collection-right-title-line">{{collections[4].title}}</p>
            <span class="collection-item" v-for="(index, movie) in collections[4].movies.slice(0, 4)" :key="index"> 
              #{{ collections[4].movies[movie] }}
            </span>
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
  .font{
    font-size: 28px;
    word-break: keep-all;
  }
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
    width: 1300px;
    height: 690px;
  }

  .left{
    display: flex;
    margin-right: 50px;
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
    /* color: #fff; */
    position: absolute;
  }

  .collection1-title h1 {
    margin-top: 50px;
    margin-left: 50px;
    font-weight: 300;
    color: #fff;
  }

  .collection2 {
    display: flex;
    flex-wrap: wrap;
    margin-right: 25px;
    margin-bottom: 40px;
    /* border: solid 1px purple; */
    width: 360px;
    height: 330px;
  }

  .collection3 {
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 40px;
    /* border: solid 1px purple; */
    width: 360px;
    height: 330px;
  }

  .collection4 {
    display: flex;
    flex-wrap: wrap;
    margin-right: 25px;
    /* border: solid 1px purple; */
    width: 360px;
    height: 330px;
  }

  .collection5 {
    display: flex;
    flex-wrap: wrap;
    /* border: solid 1px purple; */
    width: 360px;
    height: 330px;
  }

  .collection-right-title {
    font-size: 22px;
    margin-top: 20px;
    margin-bottom: 2px;
  }
  .collection-right-title-line{
    margin-bottom: 0px;
  }
  .collection-right-title-line:hover{
    border-bottom: 1px solid black;
    
  }

  .collection-item {
    font-size: 14px;
    color: rgb(61, 61, 61);
    margin-right: 6px;
  }
</style>