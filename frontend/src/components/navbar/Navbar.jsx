import "./navbar.scss"
import PersonIcon from '@mui/icons-material/Person';
import LogoutIcon from '@mui/icons-material/Logout';
import NotificationsIcon from '@mui/icons-material/Notifications';
import { user_data } from "../../pages/login/Login";
import { Link } from "react-router-dom"


const Navbar = () => {
  // if logged in then render
  // else go to login
  return (
    <div className="navbar">
      <div className="wrapper">
        <div className="items">
          <div className="item">
            <NotificationsIcon className="icon" />
            <div className="counter">1</div>
          </div>
          <div className="item">
            <PersonIcon className="icon" />
            <span className="itemText">{user_data.user_id}</span>
          </div>
          <div className="item">
            <LogoutIcon className="icon" />
            <span className="itemText"><Link to="/logout" style={{textDecoration:"none"}}>Logout</Link></span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Navbar