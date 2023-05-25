<template>
<div>
  <div id="collection-detail">
    <h1>{{ collection.title }}</h1>
    <hr class="collection-hr">
    <div id="collection-movie-list">
      <div id="collection-movie-item" v-for="movie in movies" :key="movie.id" :movie="movie">
        <router-link class="collection-detail-item" :to="{ name:'moviedetail', params: { id: movie.id } }">
          <div class="poster">
            <div id="collection-movie-title">
              <h2>{{ movie.title }}</h2>
              <p class="collection-runtime">{{ movie.runtime }}분</p>
              <p class="collection-overview">{{ movie.overview.slice(0, 66) }}</p>
            </div>
            <img id="poster-img" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="poster">
          </div>
        </router-link>
      </div>
    </div>
  </div>
  <FooterSection/>
</div>
</template>

<script>
import FooterSection from '../../components/FooterSection'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CollectionDetailView',
  data() {
    return {
      collection : Object,
      movies : [],
    }
  },
  components: {
    FooterSection,
  },
  created() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/collections/${this.$route.params.id}/`
    })
    .then((res) => {
      this.collection = res.data.collection
      this.movies = res.data.movies
    })
    .catch(err => console.log(err))
  }
}
</script>

<style>
  .collection-hr {
    margin-top: 18px;
    margin-bottom: 20px;
    width: 600px;
  }

  #collection-detail {
    margin: 100px 0 80px 130px;
  }

  .collection-detail-item {
    padding: 0px;
  }
  #collection-movie-list {
    display: flex;
    flex-wrap: wrap;
  }

  #collection-movie-item {
    margin-top: 30px;
    margin-right: 60px;
    margin-bottom: 20px;
    box-shadow: 8px 8px 10px 0px rgba(128, 128, 128, 0.253);
  }

  #collection-movie-title{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    white-space: normal;
    padding: 28px;
    position: absolute;
    width: 174px;
    height: 294px;
    color: rgba(255, 255, 255, 0);
    background-color: rgba(0, 0, 0, 0);
  }

  #collection-movie-title:hover{
    position: absolute;
    transition-duration: 0.2s;
    color: white;
    background-color: rgba(0, 0, 0, 0.795);
  }

  .poster {
    display: flex;
    position: relative;
    width: 230px;
  }

  .collection-overview {
    font-size: 16px;
  }

  .collection-runtime {
    font-size: 12px;
  }

</style>