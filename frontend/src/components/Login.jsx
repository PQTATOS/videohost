import React, {useContext, useState} from "react";

import {UserContext} from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [, setToken] = useContext(UserContext);

    const submintLogin = async () => {
        const requestOptins = {
            method: "POST",
            headers: {"Content-Type": "application/x-www-form-urlencoded"},
            body: JSON.stringify(
        `grant_type=&username=${email}&password=${password}&scope=&client_id=&client_secret=`
      ), };

        const response = await fetch("https://videohost-back.onrender.com/auth/login", requestOptins);
        const data = await response.json();

        if (!response.ok) {
            setErrorMessage(data.detail);
        }
        else {
            setToken(data.access_token);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        submintLogin();
    }

    return (
        <div className="column">
            <form onSubmit={handleSubmit}>
                <h1>Login</h1>
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
                <button type="submit">Login</button>
            </form>
        </div>
    )
};

export default Login;