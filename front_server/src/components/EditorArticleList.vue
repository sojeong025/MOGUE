<template>
<div class="swiper-container">
  <swiper
    class="swiper"
    :options="swiperOption">
    <swiper-slide v-for="editor_article in this.editor_articles" :key="editor_article.id">

    <ul class="editor-articles">
      <!-- <li class="editor-article" v-for="editor_article in editor_articles" :key="editor_article.id"> -->
        <div class="card">
          <router-link :to="{ name: 'editorarticledetail', params: { id: editor_article.id, editor_article: editor_article } }" class="thumbnail-box">
            <img :src="editor_article.thumbnail" width="600px" height="300px" class="card-img" alt="thumbnail">
          </router-link>
          <div class="card-content">
            <h5 class="card-title"><span>{{ editor_article.title }}</span></h5>
          </div>
        </div>
      <!-- </li> -->
    </ul>
    </swiper-slide>
    <div
        class="swiper-pagination"
        slot="pagination"
        >
    </div>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
    </swiper>
</div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'EditorArticleList',
  data() {
    return {
      editor_articles: [],
      swiperOption: { 
      slidesPerView: 5, 
      spaceBetween: 16, 
      centerInsufficientSlides: true, 

      navigation: { 
        nextEl: '.swiper-button-next', 
        prevEl: '.swiper-button-prev' 
    } 
  },
    }
  },
  components: {
      Swiper,
      SwiperSlide
  },
  methods: {
    getEditorArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/community/editor_articles/random/`,
        params: {
          count: 15,
        }
      })
      .then((res) => {
        this.editor_articles = res.data
      })
      .catch(err => console.log(err))
    }
  },
  created() {
    this.getEditorArticles()
  }
}
</script>

<style scoped>
.editor-article-list {
  display: flex;
  width: 100%;
  font-family: 'SUITE-Regular';
}

li {
  list-style-type: none;
}
.editor-article {
  display: flex;
  width: 400px;
  justify-content: center;
  flex-direction: row;

}

.editor-articles {
  display: flex;
  flex-wrap: wrap;
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex-basis: 150px;
  margin: 0 10px;
}
.card-title{
  margin-top: 16px;
  margin-left: 25px;
  font-size: 15px;
  line-height: 20px;
  font-size: 18px;
  word-break: keep-all;
  font-weight: 300;
}

.thumbnail-box {
  display: flex;
  flex-direction: column;
  position: relative;
  width: 17rem;
  height: 17rem;
}

.card-img {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-img:hover {
  transform: scale(1.03);
  transition: .3s ease-in-out;
}
</style>
