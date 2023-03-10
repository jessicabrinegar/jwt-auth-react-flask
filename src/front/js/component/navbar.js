import React, { useContext, useState } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Navbar = () => {
  const { store, actions } = useContext(Context);
  return (
    <nav className="navbar navbar-light bg-light">
      <div className="container">
        <Link to="/">
          <span className="navbar-brand mb-0 h1">Home</span>
        </Link>
        <div className="ml-auto">
          {!store.token ? (
            <div>
              <Link to="/login">
                <button className="btn btn-primary">Login</button>
              </Link>
              <Link to="/register">
                <button className="btn btn-primary">Register</button>
              </Link>
            </div>
          ) : (
            <Link to="/">
              <button
                className="btn btn-primary"
                onClick={() => actions.logout()}
              >
                Logout
              </button>
            </Link>
          )}
        </div>
      </div>
    </nav>
  );
};
