import { PROFILE_ACTION_TYPE } from "./profile.type";
const INITIAL_STATE = {
    response:{}
}

export const profileReducer = (state = INITIAL_STATE, action)=>{
    const {type, payload} = action

    switch(type){
        case PROFILE_ACTION_TYPE.GET_RESPONSE_DATA:
            return{
                ...state,
                ...payload
            }
            default: return state
    }
    
}