import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000/";

export const api = () => axios.create({
    baseURL: BASE_URL,
    headers:{
        'Access-Control-Allow-Origin': "*",
        'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',
    }
 });