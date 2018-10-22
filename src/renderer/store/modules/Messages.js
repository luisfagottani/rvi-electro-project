const state = {
  showSuccess: false,
  loadingState: false,
  alertMessage: "",
  showAlert: false
};

const mutations = {
  SET_SUCCESS_STATE(state) {
    state.showSuccess = !state.showSuccess;
    setTimeout(function() {
      state.showSuccess = !state.showSuccess;
    }, 1800);
  },
  SET_LOADING_STATE(state, status) {
    state.loadingState = status;
  },
  SET_MESSAGE_ALERT(state, message) {
    state.alertMessage = message;
    state.showAlert = true;
    setTimeout(() => {
      state.showAlert = false;
    }, 3000);
  }
};

let getters = {
  getStatusSuccess: state => {
    return state.showSuccess;
  },
  getLoadingState: state => {
    return state.loadingState;
  },
  getMessageAlert: state => {
    return state.alertMessage;
  },
  getShowAlert: state => {
    return state.showAlert;
  }
};

const actions = {
  showSuccess({ commit }) {
    commit("SET_SUCCESS_STATE");
  },
  setLoading({ commit }, status) {
    commit("SET_LOADING_STATE", status);
  },
  setMessageAlert({ commit }, message) {
    commit("SET_MESSAGE_ALERT", message);
  }
};

export default {
  state,
  mutations,
  actions,
  getters
};
