import { Link, Outlet } from "react-router-dom";
import "./NaviBar.style.scss"
const NaviBar = ()=>{
    return( 
        <>
    <div className="navigation">
    <Link className="logo-container" to={'/'}>Home</Link>
    <div className="nav-links-container">
    <Link className="nav-link" to='/keywords'>SearchKeywords</Link>
    <Link className="nav-link" to='/authors'>SearchAuthors</Link>
    </div>
    </div>
    <Outlet/>
    </>
    )
}

export default NaviBar;