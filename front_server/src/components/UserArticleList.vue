<template>
  <div class="collection-list">
    <div class="top">
      <div class="collection">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[1].id, user_article: user_articles[1] } }">
          <div class="collection-thumbnail">
            <img class="user-article-img" v-if="user_articles[1]?.img" :src="`http://127.0.0.1:8000${user_articles[1]?.img}/`" alt="img">
          </div>
          <div class="title">
            <p>{{ user_articles[1].title }}</p> <span>➝ more</span>
            <p>{{ user_articles[1].created_at}}</p>
          </div>
        </router-link>
      </div>
      <div class="collection">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[2].id, user_article: user_articles[2]} }">
          <div class="collection-thumbnail">
            <img class="user-article-img" v-if="user_articles[2]?.img" :src="`http://127.0.0.1:8000${user_articles[2]?.img}/`" alt="img">
          </div>
          <div class="title">
            <div>{{ user_articles[2].title }}</div> <span>➝ more</span>
            {{ user_articles[2].created_at}}
          </div>
        </router-link>
      </div>
      <div class="collection">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[3].id, user_article: user_articles[3]} }">
          <div class="collection-thumbnail">
            <img class="user-article-img" v-if="user_articles[3]?.img" :src="`http://127.0.0.1:8000${user_articles[3]?.img}/`" alt="img">
          </div>
          <div class="title">
            <div>{{ user_articles[3].title }}</div> <span>➝ more</span>
            <!-- {{ user.articles[3].created_at }} -->
          </div>
        </router-link>
      </div>
    </div>
    <div class="bottom">
      <div class="collection">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[4].id, user_article: user_articles[4]} }">
          <div class="collection-thumbnail">
            <img class="user-article-img" v-if="user_articles[4]?.img" :src="`http://127.0.0.1:8000${user_articles[4]?.img}/`" alt="img">
          </div>
          <div class="title">
            <div>{{ user_articles[4].title }}</div> <span>➝ more</span>
          </div>
        </router-link>
      </div>
      <div class="collection">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[0].id, user_article: user_articles[0]} }">
          <div class="collection-thumbnail">
            <img class="user-article-img" v-if="user_articles[0]?.img" :src="`http://127.0.0.1:8000${user_articles[0]?.img}/`" alt="img">
          </div>
          <div class="title">
            <div>{{ user_articles[0].title }}</div> <span>➝ more</span>
          </div>
        </router-link>
      </div>
      <div class="collection">
        <router-link :to="{ name: 'userarticledetail', params: {id: user_articles[5].id, user_article: user_articles[5]} }">
          <div class="collection-thumbnail">
            <img class="user-article-img" v-if="user_articles[5]?.img" :src="`http://127.0.0.1:8000${user_articles[5]?.img}/`" alt="img">
          </div>
          <div class="title">
            <div>{{ user_articles[5].title }}</div> <span>➝ more</span>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UserArticleList',
  data() {
    return {
      user_articles: [],
    }
  },
  // props: {
  //   page : Number,
  // },
  created() {
    this.getUserArticles()
  },
  methods: {
    getUserArticles() {
      axios({
        method: 'get',
        url: `${API_URL}/community/user_articles/`
      })
      .then((res) => {
        console.log(res.data)
        this.user_articles = res.data
      })
      .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>
.collection-list {
  display: flex;
  flex-direction: column;
}
.user-article-img {
  width: 400px;
  height: 370px;
}
.collection{
  margin: 30px;
}
.top{
  display: flex;
  justify-content: center;
}
.bottom{
  display: flex;
  justify-content: center;
}
.title{
  margin-top:10px;
  width: 370px;
  text-overflow:ellipsis ;
  overflow: hidden;
  white-space: nowrap;
}
span {
  font-size: 16px;
}
</style>
