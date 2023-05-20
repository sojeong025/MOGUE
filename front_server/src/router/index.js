import Vue from 'vue'
import VueRouter from 'vue-router'

// 1. basic router
import HomeView from '@/views/HomeView'
import LoginView from '@/views/accounts/LoginView'
import SignupView from '@/views/accounts/SignupView'
import ProfileView from '@/views/accounts/ProfileView'


// 2.Movie Router
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView'
import CollectionDetailView from '@/views/movies/CollectionDetailView'

// 3.Community Router
import CommunityView from '@/views/community/CommunityView'



Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/movie/:id',
    name: 'moviedetail',
    component: MovieDetailView
  },
  {
    path: '/movie/collection/:id',
    name: 'collectiondetail',
    component: CollectionDetailView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
