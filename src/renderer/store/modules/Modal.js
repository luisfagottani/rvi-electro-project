const state = {
  showConfigurationState: false,
}

const mutations = {
  CHANGE_STATE_CONFIGURATION_MODAL (state) {
    state.showConfigurationState = !state.showConfigurationState
  },
}


let getters = {
  getStatusConfiguration(state){
    return state.showConfigurationState
  }
}

const actions = {
  handleConfigurationModal ({ commit }) {
    commit('CHANGE_STATE_CONFIGURATION_MODAL')
  },
  
}

export default {
  state,
  mutations,
  actions,
  getters
}
