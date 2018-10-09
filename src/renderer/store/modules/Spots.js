const state = {
  parkingLot: [],
  canvas: {},
  camera_id: 0,
  client: '',
  isLoading: true
}

const mutations = {
  ADD_CAMERA(state, camera) {
    state.parkingLot.push(camera);
  },
  SET_CAMERA(state, camera_id) {
    state.camera_id = camera_id
  },
  SET_CANVAS(state, canvas) {
    state.canvas = canvas;
  },
  SET_PTYHON_API(state, client) {
    state.client = client;
  },
  SET_IS_LOADING(state) {
    state.isLoading = !state.isLoading
  }
}


let getters = {
  getCamera(state) {
    return state.parkingLot.find(vaga => vaga.camId === state.camera_id)
  },

  getAllCameras(state) {
    return state.parkingLot;
  },

  getCanvas(state) {
    return state.canvas
  },

  getClientApi(state) {
    return state.client
  },

  getIsLoading(state) {
    return state.isLoading
  }


}

const actions = {
  addCamera({
    commit
  }, camera) {
    commit('ADD_CAMERA', camera)
  },
  setCanvas({
    commit
  }, canvas) {
    commit('SET_CANVAS', canvas)
  },
  setCamera({
    commit
  }, camera_id) {
    commit('SET_CAMERA', camera_id);
  },
  setPythonApi({
    commit
  }, client) {
    commit('SET_PTYHON_API', client)
  },
  setIsLoading({
    commit
  }) {
    commit('SET_IS_LOADING')
  }

}

export default {
  state,
  mutations,
  actions,
  getters
}
