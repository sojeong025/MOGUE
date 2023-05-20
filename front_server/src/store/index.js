import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false
  },
  getters: {
  },
  mutations: {
    SET_LOGIN(state, isLogin) {
      state.isLogin=isLogin
    }
  },
  actions: {
    login() {
      this.commit('SET_LOGIN', true)
    },
    logout() {
      this.commit('SET_LOGIN', false)
    }
  },
  modules: {
  }
})
