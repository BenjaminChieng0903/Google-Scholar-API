import './App.css';
import{Route, Routes} from'react-router-dom'
import NaviBar from './route/navibar/NaviBar';
import Home from './route/homepage/Home';
import SearchAuthors from './searchauthors/SearchAuthors';
import SearchKeywords from './searchkeywords/SearchKeywords';
import SearchResult from './searchResult/SearchResult'
function App() {
  return (
    <div className="App">
      <Routes>
      <Route path='/' element = {<NaviBar/>}>
        <Route index element = {<Home/>}></Route>
        <Route path ='keywords'element = {<SearchKeywords/>}></Route>
        <Route path ='authors' element = {<SearchAuthors/>}></Route>
        <Route path = 'result' element = {<SearchResult/>}></Route>
      </Route>
      </Routes>
    </div>
  );
}

export default App;
