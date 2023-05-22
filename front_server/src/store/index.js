import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    token: null,
  },
  getters: {
  },
  mutations: {
    SET_LOGIN(state, isLogin) {
      state.isLogin=isLogin
    }
  },
  actions: {
    login({ commit }, token) {
      localStorage.setItem('token', token)
      commit('SET_LOGIN', true)
    },
    // 로그아웃 시 토큰 제거
    logout({ commit }) {
      localStorage.removeItem('token')
      commit('SET_LOGIN', false)
    },
    checkLogin({ commit }) {
      if (localStorage.getItem('token')) {
        commit('SET_LOGIN', true)
      } else {
        commit('SET_LOGIN', false)
      }
    }
  },
  modules: {
  }
})
