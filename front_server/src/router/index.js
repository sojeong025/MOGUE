import Vue from 'vue'
import VueRouter from 'vue-router'

// 1. basic router
import HomeView from '@/views/HomeView'
import LoginView from '@/views/accounts/LoginView'
import SignupView from '@/views/accounts/SignupView'
import ProfileView from '@/views/accounts/ProfileView'
import UpdateProfileView from '@/views/accounts/UpdateProfileView'
import FollowView from '@/views/accounts/FollowView'


// 2.Movie Router
import MovieView from '@/views/movies/MovieView'
import MovieDetailView from '@/views/movies/MovieDetailView'
import CollectionDetailView from '@/views/movies/CollectionDetailView'


// 3.Community Router
import CommunityView from '@/views/community/CommunityView'
import EditorArticleDetailView from '@/views/community/EditorArticleDetailView'
import UserArticleDetailView from '@/views/community/UserArticleDetailView'
import UserArticleCreateView from '@/views/community/UserArticleCreateView'

// 4. Search Router
import SearchView from '@/views/search/SearchView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
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
    path: '/profile/:id',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/profile/:id/update',
    name: 'profile_update',
    component: UpdateProfileView
  },
  {
    path: '/profile/:id/follow',
    name: 'follow',
    component: FollowView
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
  },
  {
    path: '/community/editor_articles/:id',
    name: 'editorarticledetail',
    component: EditorArticleDetailView
  },
  {
    path: '/community/user_articles/:id',
    name: 'userarticledetail',
    component: UserArticleDetailView
  },
  {
    path: '/community/create',
    name: 'articlecreate',
    component: UserArticleCreateView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
