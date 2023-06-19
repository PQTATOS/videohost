import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";

const  VideosPage = () => {

        const [errorMessage, setErrorMessage] = useState("");
        const [videos, setVideos] = useState([])

    const getVideos = async () => {
        const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    }

    const response = await fetch("http://127.0.0.1:8000/video/", requestOptions);
        const data = await response.json();

        if(!response.ok) {
            setErrorMessage(data.detail);
        }
        else {
            setVideos(data);
        }
    };

    useEffect(() => {
    getVideos();
  }, []);

    return (
        <div>
            <div style={{marginBottom: "50px"}}>
                <Link style={{color: "red"}} to="/upload">Upload video</Link>
            </div>
        <div>
        <table>
                <tbody>
                {videos.map((video) =>
                    (
                        <Link to={`/watch/${video.id}`}>
                            <div><tr>
                            <td>{video.title}</td>
                            <td>{video.link}</td>
                            <td>{video.user_id}</td>
                            <td>{video.published_at}</td>
                            </tr></div>
                    </Link>
                    ))}
                </tbody>
            </table>
        </div>
        </div>)

}

export default VideosPage