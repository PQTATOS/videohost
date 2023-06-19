import {useContext, useState} from "react";
import {UserContext} from "../context/UserContext";
import Register from "./Register";
import Login from "./Login";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import VideosPage from "./VideosPage";
import ViewVideo from "./ViewVideo";
import UploadVideo from "./UploadVideo";

const Router = () => {
    const [token,] = useContext(UserContext);

    return(
        <>
            { !token ? (
                <div>
                    <Register />
                    <br></br>
                    <Login />
                </div>
            ) : (
                <BrowserRouter>
                    <Routes>
                        <Route element={<VideosPage />} path='/'/>
                        <Route element={<ViewVideo />} path='/watch/:video_id'/>
                        <Route element={<UploadVideo />} path='/upload'/>
                    </Routes>
                </BrowserRouter>
            )
            }
        </>
    )
}

export default Router