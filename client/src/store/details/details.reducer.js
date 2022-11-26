import { DETAILS_ACTION_TYPE } from "./details.type"
const INITIAL_STATE = {
    response:{}
}

export const detailsReducer = (state = INITIAL_STATE, action)=>{
    const {type, payload} = action

    switch(type){
        case DETAILS_ACTION_TYPE.GET_DETAILS_DATA:
            return{
                ...state,
                ...payload
            }
            default: return state
    }
    
}