import "./deleteSingle.scss"
import PersonIcon from '@mui/icons-material/Person';
import { user_data } from "../login/Login"
import AdminSidebar from "../../components/adminSidebar/AdminSidebar"
import AdminNavbar from "../../components/adminNavbar/AdminNavbar"
import {useEffect, useState} from "react"
import axios from "axios";
import { target_user } from "../../components/userList/UserList";
import { Navigate, useNavigate } from "react-router-dom";

const DeleteSingle = ({target_id}) => {
  // access page only if logged in and role = admin
  const isLogged = localStorage.getItem('isLogged')
  const role = localStorage.getItem('role')
  const isAdmin = (role === "Admin")?true:false

  const [data, setdata] = useState(
    {
        name: "",
        department: "",
        designation: "",
        email: "",
        role: ""
    }
  )

  const navigate = useNavigate()

  const target_user_id = localStorage.getItem("target_id")
  const url = "http://127.0.0.1:5000/Admin/dashboard/deleteuser/" + target_user_id
  let handleDelete = () =>{
    axios.post(url).then((response) => {
      if(response.status === 200){
        console.log(target_user_id)
        localStorage.removeItem('target_id')
        navigate("/admin/user/modify")
      }
    })
  }

  // useEffect(
  //   axios.get("")
  //   .then((response) => {
  //       const res = response.data
  //       if (response.status == 200) {
  //           setdata({
  //               name: res.username,
  //               department: res.department,
  //               designation: res.designation,
  //               email: res.email,
  //               role: res.role
  //           })
  //       }
  //   })
  // )

  return (
    <div className="single">{
      (!isLogged) && <Navigate to="/login" />
    }
    {
      (!isAdmin) && <Navigate to="/" />
    }
      <AdminSidebar />
      <div className="singleContainer">
        <AdminNavbar />
        <div className="top">
          <h1>Delete User</h1>
        </div>
        <div className="bottom">
          <div className="left">
            <h1 className="title">Information</h1>
            <div className="item">
              <PersonIcon className="itemImg"/>
              <div className="details">
                <h1 className="itemTitle">{data.name}</h1>
                <div className="detailItem">
                  <span className="itemKey">Department:</span>
                  <span className="itemValue">{data.department}</span>
                </div>
                <div className="detailItem">
                  <span className="itemKey">Designation:</span>
                  <span className="itemValue">{data.designation}</span>
                </div>
                <div className="detailItem">
                  <span className="itemKey">Email:</span>
                  <span className="itemValue">{data.email}</span>
                </div>
                <div className="detailItem">
                  <span className="itemKey">Role:</span>
                  <span className="itemValue">{data.role}</span>
                </div>
              </div>
            </div>
            <button onClick={handleDelete}>DELETE</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default DeleteSingle