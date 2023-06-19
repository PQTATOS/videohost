import React from 'react';
import ReactDom from "react-dom"
import App from './App';

import {UserProvider}  from "./context/UserContext";

ReactDom.render(
    <UserProvider>
        <App />{" "}
    </UserProvider>,
    document.getElementById("root")
)
