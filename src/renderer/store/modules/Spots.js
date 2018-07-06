const state = {
  parkingLot: [],
  canvas: {},
  camera_id: 0
}

const mutations = {
  ADD_CAMERA (state, camera) {
      state.parkingLot.push(camera);
  },
  SET_CAMERA (state, camera_id) {
    state.camera_id = camera_id
  },
  SET_CANVAS (state, canvas){
      state.canvas = canvas;
  }
}

const actions = {
  addCamera ({ commit }, camera) {
    commit('ADD_CAMERA', camera)
  },
  setCanvas ({ commit }, canvas) {
    commit('SET_CANVAS', canvas)
  },
  setCamera({commit}, camera_id) {
    commit('SET_CAMERA', camera_id);
  }
  
}

const getters = {
  getCamera(state){
    return state.parkingLot.find(vaga => vaga.camId === state.camera_id)
  },

  getTotalSpots(state){
    const camera = state.parkingLot.find(vaga => vaga.camId === state.camera_id);
    return camera.spots.length
  }
}

export default {
  state,
  mutations,
  actions,
  getters
}
