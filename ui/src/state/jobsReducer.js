
export default (state, action) =>{
   switch (action.type){
       case 'GET_JOBS':
           return {...state, jobs: [], loading: true, error: null}
       case 'GET_JOBS_RES':
           return {...state, jobs: action.payload, loading: false, error: null}
       case 'GET_JOBS_ERR':
           return {...state, jobs: [], loading: false, error: action.payload}
       default:
           return state
   }

}