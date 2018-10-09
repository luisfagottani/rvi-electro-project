const state = {
  showSuccess: false,
}

const mutations = {
  SET_SUCCESS_STATE(state) {
    state.showSuccess = !state.showSuccess; 
    setTimeout(function(){  state.showSuccess = !state.showSuccess }, 1500);
  }
}


let getters = {
  getStatusSuccess: (state)  => {
    return state.showSuccess;
  }
}

const actions = {
  showSuccess({
    commit
  }) {
    commit('SET_SUCCESS_STATE')
  },

}

export default {
  state,
  mutations,
  actions,
  getters
}
