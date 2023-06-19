import {useContext, useState} from "react";
import {UserContext} from "./context/UserContext";
import Router from "./components/Router";


const App = () => {
  const [token] = useContext(UserContext);


  return (
    <>
      <Router />
    </>
  );
};

export default App;
