const worksModule = {
    firestorePath: 'tasks',
    firestoreRefType: 'collection', // or 'doc'
    moduleName: 'worksModule',
    statePropName: 'data',
    namespaced: true, // automatically added
  
    // this object is your store module (will be added as '/myModule')
    // you can also add state/getters/mutations/actions
    state: {},
    getters: {        
        getTasks(state){
        return state.data;
    }},
    mutations: {},
    actions: {},
  }
  
  export default worksModule