import {useParams} from "react-router-dom";
import React, {useContext, useEffect, useState} from "react";
import ReactPlayer from "react-player";
import {UserContext} from "../context/UserContext";

const ViewVideo = () => {
    const {video_id} = useParams();
    const [video, setVideo] = useState({});
    const [isLiked, setIsLiked] = useState({});
    const [comments, setComments] = useState([]);
    const [com, setCom] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [token , setToken] = useContext(UserContext);

    const getVideo = async () => {
        const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json", },
        }

        const response = await fetch(`http://127.0.0.1:8000/video/watch?video_id=${video_id}`, requestOptions)
        const data = await response.json()

        if(!response.ok) {
            setErrorMessage(data.detail);
        }
        else {
            setVideo(data);
        }
    };

    const getComments = async () => {
        const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json", },
        }

        const response = await fetch(`http://127.0.0.1:8000/video/comments?video_id=${video_id}`, requestOptions)
        const data = await response.json()

        if(!response.ok) {
            setErrorMessage(data.detail);
        }
        else {
            setComments(data);
        }
    };

    const getLike = async  () => {
        const requestOptions = {
            method: "GET",
            headers: {"Content-Type": "application/x-www-form-urlencoded",
             Authorization: "Bearer " + token},
        };
        const response = await fetch(`http://127.0.0.1:8000/video/like?video_id=${video_id}`, requestOptions);
        const data = await response.json()

        setIsLiked(data)
    };

    const submitComment = async  () => {
        const requestOptions = {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded",
             Authorization: "Bearer " + token},
            body: `content=${com}`,
        };
        await fetch(`http://127.0.0.1:8000/video/comment?video_id=${video_id}`, requestOptions);
    };

    const submitLike = async () => {
        const requestOptions = {
            method: "POST",
            headers: { Authorization: "Bearer " + token},
        };
        await fetch(`http://127.0.0.1:8000/video/like?video_id=${video_id}`, requestOptions);
    };

    const handleSubmitCom = (e) => {
        e.preventDefault();
        submitComment()
        setCom("")
    }

    const handleSubmitLike = (e) => {
        submitLike();
    }


    useEffect(() => {
        getVideo();
        getComments();
        getLike();
    }, []);

    return (
        <div>
        <div>
            <ReactPlayer
                controls
                playing
                url={video.link}/>
            <h1>{video.title}</h1>
            <p>{video.description}</p>
            <p>{video.user_id}     {video.created_at}</p>
        </div>
            <div>
                <div>Is Video liked: {isLiked.isLiked ? ("True") : ("False")}</div>
                <button onClick={handleSubmitLike}>LIKE</button>
            </div>
        <div>
            <div>
                <form onSubmit={handleSubmitCom}>
                    <input type="comment"
                           placeholder="Enter your comment"
                           value={com}
                           onChange={(e) => setCom(e.target.value)}
                    />
                    <button type="submit">Send</button>
                </form>
            </div>
            {comments.map((comment) => (
                <div style={{backgroundColor: "gray", marginTop: "20px"}}>
                    <p>{comment.user_id} {comment.published_at}</p>
                    <p>{comment.text}</p>
                </div>
            ))}
        </div>
    </div>
    )

}

export default ViewVideo