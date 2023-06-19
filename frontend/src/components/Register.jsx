import React, {useContext, useState} from "react";

import {UserContext} from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";

const Register = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [username, setUsername] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [, setToken] = useContext(UserContext);

    const submitRegistration = async () => {
        const requestOptions = {
            method: "POST",
            headers: {"Content-Type": "application/json",},
            body: JSON.stringify({email: email, username: username, password: password}),
        };
        const response = await fetch("https://videohost-back.onrender.com/auth/signup", requestOptions);
        const data = await response.json();

        if (!response.ok) {
            setErrorMessage(data.detail);
        }
        else {
            setToken(data.access_token);
        }
    };

    const  handleSubmit = (e) => {
        e.preventDefault();
        if (password.length > 8)
        {
            submitRegistration();
        }
        else setErrorMessage("Error in Registration")
    }

    return (
        <div className="column">
            <form onSubmit={handleSubmit}>
                <h1>Register</h1>
                <div className="field">
                    <label>Email address</label>
                    <div>
                        <input
                            type="email"
                            placeholder="Enter email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="input"
                            required/>
                    </div>
                </div>
                  <div className="field">
                    <label>Username</label>
                    <div>
                        <input
                            type="username"
                            placeholder="Enter username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            className="input"
                            required/>
                    </div>
                </div>
                <div className="field">
                    <label>Password</label>
                    <div>
                        <input
                            type="password"
                            placeholder="Enter password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="input"
                            required/>
                    </div>
                </div>
                <ErrorMessage message={errorMessage}/>
                <button type="submit">Register</button>
            </form>
        </div>
    )
};

export default Register;