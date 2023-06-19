import {useContext, useState} from "react";
import {UserContext} from "../context/UserContext";
import axios from "axios";


const UploadVideo = () => {
    const [token , setToken] = useContext(UserContext);
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
     const [file, setFile] = useState({});

     const uploadVideo = async (e) => {
         e.preventDefault()
         console.log(file)
         const formData = new FormData()
         formData.append("file", file)
         formData.append("title", title)
         formData.append("description", description)

        await axios.post(`https://videohost-back.onrender.com/video/upload`, formData, {headers: {"Content-Type": "multipart/form-data",
             Authorization: "Bearer " + token},})
    };

     return (
         <div>
             <form onSubmit={uploadVideo}>
                 <div><input type='file' onChange={(e) => {setFile(e.target.files[0])}}/></div>
                 <div>
                     <p>Title</p>
                     <input type="title" onChange={(e) => {setTitle(e.target.value)}}/>
                 </div>
                <div>
                     <p>Description</p>
                    <input type="description" onChange={(e) => {setDescription(e.target.value)}}/>
                </div>
                 <div><button type='submit'>Upload</button></div>
             </form>
         </div>
     )
};

export default UploadVideo