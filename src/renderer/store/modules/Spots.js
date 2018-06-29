const state = {
  parkingLot: [],
  canvas: {}
}

const mutations = {
  SET_CAMERA (state, camera) {
      state.parkingLot.push(camera);
  },
  SET_CANVAS (state, canvas){
      state.canvas = canvas;
  }
}

const actions = {
  addCamera ({ commit }, camera) {
    commit('SET_CAMERA', camera)
  },
  setCanvas ({ commit }, canvas) {
    commit('SET_CANVAS', canvas)
  }
  
}

export default {
  state,
  mutations,
  actions
}
