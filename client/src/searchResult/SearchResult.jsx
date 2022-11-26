import "./SearchResult.style.scss"
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import { styled } from '@mui/material/styles';
import { useSelector } from "react-redux";
import { selectProfileResponse } from "../store/profile/profile.selector";
import { useState } from "react";
import { Pagination, PaginationItem } from "@mui/material";
import AuthorDetails from "./authorDetails";
import { useDispatch } from "react-redux"
import { setResponse } from "../store/details/details.action";
import { api } from "../utils/api";
const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(8),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));
const SearchResult = ()=>{
    const dispatch = useDispatch()
    const [currentPage, setCurrentPage] = useState(1)
    const [perPageAmount, setPerPageAmount] = useState(4)
    const [clickDetails, setClickDetails] = useState(false)
    const response = useSelector(selectProfileResponse)
    const LastItemIndex = currentPage*perPageAmount
    const FirstItemIndex = LastItemIndex - perPageAmount
    const curentPageResult = response.slice(FirstItemIndex, LastItemIndex)


      const pageNumber = [];
      for(let i =1; i<= Math.ceil(response.length/perPageAmount);i++){
        pageNumber.push(i)
      }
 
      const getCoAuthorResult = async(item_id)=>{
        const coAuthorResponse = await api().get('coAuthor',{
          params:{
            author_id:item_id
          }
        })
      console.log(coAuthorResponse.data)
      dispatch(setResponse(coAuthorResponse.data))

    }
    return(
      <>
        <div className="pagination">
          <input placeholder='New query'></input>
          <Pagination color="secondary" count={pageNumber.length} onChange={(event,page)=>setCurrentPage(page)}></Pagination>
          </div>
        <div className="layout">          
        <Box sx={{ width: 400 }}>
      <Stack  spacing={0} sx = {{display:'flex', flexDirection:'row'}}>
        {
         curentPageResult.map((item)=>{
          //search co-authors by author_id right here is more benifical than 
          //sending requests whenever click the profile card.
            return(
            <Item key={item.author_id} className="profile-card" onClick={
              ()=>{ 
                getCoAuthorResult(item.author_id)
                setClickDetails(true)
              }} sx={{  display:'flex', alignContent:'space-evenly',flexDirection:'column',borderColor:'black', backgroundColor:'cornsilk'}}>

            <div className="profile">
            <img  width='60px' height='60px' src = {item.thumbnail}/>
              <label><a>Name: {item.name}</a> <br></br>
             Email: {item.email}</label>
              </div>
              <div className="interest">
               <a>Interests:</a>
              {item.interests&&item.interests.map((interest)=>{
                return(
                <p>
                  {interest.title}
                  </p>
                  )
              })}
              </div>
              </Item>
            
            )
            
          })
        }
        
      </Stack>

    </Box>

        </div>
       { clickDetails? <AuthorDetails/>:<Box className="details" sx={{}}>
        <p >Select a professor to see their co-authors and works...</p>
        </Box>
        }
        </>
    )
}

export default SearchResult