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
    },
    SAVE_TOKEN(state, token) {
      localStorage.setItem('token', token)
    }
  },
  actions: {
    login({ commit }, token) {
      commit('SAVE_TOKEN', token);
    },
    // 로그아웃 시 토큰 제거
    logout({ commit }) {
      commit('SAVE_TOKEN', null);
    }
  },
  modules: {
  }
})
