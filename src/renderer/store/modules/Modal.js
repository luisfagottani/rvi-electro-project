const state = {
  addCameraModal: false,
  settingsModal: false,
  editCameraModal: false
}

const mutations = {
  UPDATE_MODAL_STATE (state, nameModal) {
    switch(nameModal){
      case "addCameraModal":
        state.addCameraModal = !state.addCameraModal
        break;
      case "settingsModal":
        state.settingsModal = !state.settingsModal
        break;
      case "editCameraModal":
        state.editCameraModal = !state.editCameraModal
        break;

      default:
        break;
    }
  },
}


let getters = {
  getStatusModal: (state) => (nameModal) => {
    switch(nameModal){
      case "addCameraModal":
        return state.addCameraModal;

      case "settingsModal":
        return state.settingsModal

      case "editCameraModal":
        return state.editCameraModal

      default:
        return 0;
    }
  },
}

const actions = {
  toggleModal ({ commit }, nameModal) {
    commit('UPDATE_MODAL_STATE', nameModal)
  },
  
}

export default {
  state,
  mutations,
  actions,
  getters
}
