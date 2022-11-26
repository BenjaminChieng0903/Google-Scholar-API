import { CreateAction } from "../../utils/createAction";
import { DETAILS_ACTION_TYPE } from "./details.type";

export const setResponse = (detailsData)=>{
    return CreateAction(DETAILS_ACTION_TYPE.GET_DETAILS_DATA,
        {
            response: detailsData
        })
}