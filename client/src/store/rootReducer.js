import { profileReducer } from "./profile/profile.reducer";
import { combineReducers } from "redux";
import { detailsReducer } from "./details/details.reducer";
export const rootReducer = combineReducers({
   profile:profileReducer,
   details:detailsReducer
})
