import { CreateAction } from "../../utils/createAction";
import { PROFILE_ACTION_TYPE } from "./profile.type";

export const setResponse = (responseData)=>{
    return CreateAction(PROFILE_ACTION_TYPE.GET_RESPONSE_DATA,
        {
            response: responseData
        })
}