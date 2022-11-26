import { useSelector } from "react-redux";
import { selectDetailsResponse } from "../store/details/details.selector";
const AuthorDetails = ()=>{
    const details = useSelector(selectDetailsResponse)
    return(
        <>
    {
       details==='No co-authors'? <h1>no co-authors</h1>:details.map((coAuthor)=>{
            return(
                <div>
                <h1>
                {coAuthor.name}</h1></div>
            )
        })
    }
    </>
    )
}

export default AuthorDetails;