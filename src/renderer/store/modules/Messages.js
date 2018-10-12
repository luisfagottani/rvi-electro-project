const state = {
  showSuccess: false,
  loadingState: false
}

const mutations = {
  SET_SUCCESS_STATE(state) {
    state.showSuccess = !state.showSuccess;
    setTimeout(function () {
      state.showSuccess = !state.showSuccess
    }, 1800);
  },
  SET_LOADING_STATE(state, status) {
    state.loadingState = status
  }
}


let getters = {
  getStatusSuccess: (state) => {
    return state.showSuccess;
  },
  getLoadingState: (state) => {
    return state.loadingState
  }
}

const actions = {
  showSuccess({
    commit
  }) {
    commit('SET_SUCCESS_STATE')
  },
  setLoading({
    commit,
  }, status) {
    commit('SET_LOADING_STATE', status)
  },

}

export default {
  state,
  mutations,
  actions,
  getters
}
