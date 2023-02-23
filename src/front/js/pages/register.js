import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
// import { useHistory } from "react-router-dom";
import "../../styles/home.css";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import * as yup from "yup";

export const Register = () => {
  // const { register, handleSubmit } = useForm();
  const { store, actions } = useContext(Context);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  // const [confirmPassword, setConfirmPassword] = useState("");
  // const history = useHistory();
  // dont need this since you have it in store now (see return)
  // const token = localStorage.getItem("token");

  const onSubmit = (data) => {
    console.log(data);
    // actions.register(email, username, password);
  };

  const handleClick = () => {
    // if the login was successful (returned true), the .then will be called
    actions.register(name, email, username, password); //.then(() => {
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
        <form onSubmit={handleSubmit(onSubmit)}>
          <input
            type="text"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          ></input>
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
          {/* <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          ></input> */}
          <Link to="/login">
            /* <button onClick={handleClick}>Submit</button>
          </Link>
          {/* <input type="submit"></input> */}
        </form>
      )}
    </div>
  );
};
