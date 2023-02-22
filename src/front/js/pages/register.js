import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
// import { useHistory } from "react-router-dom";
import "../../styles/home.css";
import { Link } from "react-router-dom";

export const Register = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  // const history = useHistory();
  // dont need this since you have it in store now (see return)
  // const token = localStorage.getItem("token");

  const handleClick = () => {
    // if the login was successful (returned true), the .then will be called
    actions.register(email, username, password); //.then(() => {
    //history.push("/");
    //});
  };
  // anytime it finds a token, it will take the user out of the login
  // if (store.token && store.token != "" && store.token != undefined)
  //   history.push("/");

  return (
    <div className="text-center mt-5">
      <h1>Register</h1>
      {store.token && store.token != "" && store.token != undefined ? (
        "You are registered."
      ) : (
        <div>
          <input
            type="text"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          ></input>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          ></input>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          ></input>
          <Link to="/login">
            <button onClick={handleClick}>Login</button>
          </Link>
        </div>
      )}
    </div>
  );
};
