import { useState } from "react"
import { api } from "../utils/api"
import { setResponse } from "../store/profile/profile.action"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router-dom"
const SearchAuthors = ()=>{
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const [authorName, setAuthorName] = useState([])
    const getAuthorResult = async()=>{
        const response = await api().get('author',{
            params: {
                keyword: authorName
            }
        })
        console.log(response)
        dispatch(setResponse(response.data))

        navigate('/result')

        // setAuthorName(response.data.author.name)
        // setAuthorName(response.data.name)//connect to serp api
    }
    const getInput = (event)=>{
        setAuthorName(event.target.value)
    }
    
    return(

            <>
            <h1>this is authors search!</h1>
            <input placeholder="Author/Industry" onChange={getInput}></input>
            <button onClick={getAuthorResult}>search</button>
            </>
    )
}

export default SearchAuthors;