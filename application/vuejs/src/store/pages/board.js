import camelcaseKeys from 'camelcase-keys';


const state = {
  boardData: {
    pipeLineList: [],
  },
};


const getters = {
  getSocket(state, getters, rootState) {
    return rootState.socket;
  },
};

const actions = {
};

const mutations = {
  setBoardData(state, { boardData }) {
    state.boardData = camelcaseKeys(boardData, { deep: true });
  },
};


export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
