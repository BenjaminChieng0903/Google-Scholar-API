import { useEffect, useState } from "react"
import { api } from "../utils/api"
const SearchKeywords = ()=>{
    const [keywordResult, setKeywordResult] = useState([])
    console.log(keywordResult)
    const getKeywordsResult = async()=>{
        const response = await api().get('query')
        // const response = await fetch('http://localhost:5000/query')
        // .then(res=>res.json())
        // console.log(response.data.organic_results)
        setKeywordResult(response.data.organic_results)
        // console.log(response.data)
    }
        return(
            <>
            <h1>this is keyword search!</h1>
            <input placeholder="keywords"></input>
            <button onClick={getKeywordsResult}>search</button>
            {
                keywordResult.map((item)=>{
                    return(
                        <h1 key={item.position}>{item.title}</h1>
                    )
                })
}
            </>
            
        )
    }
    
    export default SearchKeywords;