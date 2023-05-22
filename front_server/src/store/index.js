import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    token: null,
    textWhite: false,
  },
  getters: {
  },
  mutations: {
    SET_LOGIN(state, isLogin) {
      state.isLogin=isLogin
    },
    TEXT_WHITE(state, textWhite) {
      state.textWhite = textWhite
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
    },
    checkTextWhite({ commit }, name) {
      if (name === 'home') {
        commit('TEXT_WHITE', true)
      } else {
        commit('TEXT_WHITE', false)
      }
    }
  },
  modules: {
  }
})
