import React, {useEffect, useState} from "react";

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
                <a style={{color: "red"}} href="http://localhost:3000/upload">Upload video</a>
            </div>
        <div>
        <table>
                <tbody>
                {videos.map((video) =>
                    (
                        <a href={`http://localhost:3000/watch/${video.id}`}>
                            <div><tr>
                            <td>{video.title}</td>
                            <td>{video.link}</td>
                            <td>{video.user_id}</td>
                            <td>{video.published_at}</td>
                            </tr></div>
                    </a>
                    ))}
                </tbody>
            </table>
        </div>
        </div>)

}

export default VideosPage