const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      token: null,
      message: null,
      demo: [
        {
          title: "FIRST",
          background: "white",
          initial: "white",
        },
        {
          title: "SECOND",
          background: "white",
          initial: "white",
        },
      ],
    },
    actions: {
      // Use getActions to call a function within a fuction
      exampleFunction: () => {
        getActions().changeColor(0, "green");
      },
      syncTokenFromLocalStorage: () => {
        const token = localStorage.getItem("token");
        console.log("App just loaded, syncing the local storage token.");
        if (token && token != "" && token != undefined)
          setStore({ token: token });
      },
      logout: () => {
        const token = localStorage.removeItem("token");
        console.log("Logging out.");
        setStore({ token: null });
      },
      // if you return something in an async fx, that will translate into a .then when used on the login page
      login: async (email, password) => {
        const opts = {
          method: "POST",
          headers: {
            "content-type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        };
        try {
          const resp = await fetch(
            "https://3001-jessicabrin-jwtauthreac-1p1yby95osh.ws-us87.gitpod.io/api/token",
            opts
          );
          if (resp.status != 200) {
            alert("There has been some error.");
            return false;
          }
          const data = await resp.json();
          console.log("this came from backend: ", data);
          localStorage.setItem("token", data.access_token);
          // login view will refresh after store is set because it is hooked to context API, rerendering the component
          setStore({ token: data.access_token });
          return true;
        } catch (error) {
          console.error("There has been an error logging in.");
        }
      },
      getMessage: async () => {
        const store = getStore();
        // add token to all requests from here on out
        const opts = {
          headers: {
            Authorization: "Bearer " + store.token,
          },
        };
        try {
          // fetching data from the backend
          const resp = await fetch(
            //process.env.BACKEND_URL ?? changed it to the written out version
            "https://3001-jessicabrin-jwtauthreac-1p1yby95osh.ws-us87.gitpod.io/api/hello",
            opts
          );
          const data = await resp.json();
          setStore({ message: data.message });
          // don't forget to return something, that is how the async resolves
          return data;
        } catch (error) {
          console.log("Error loading message from backend", error);
        }
      },
      changeColor: (index, color) => {
        //get the store
        const store = getStore();

        //we have to loop the entire demo array to look for the respective index
        //and change its color
        const demo = store.demo.map((elm, i) => {
          if (i === index) elm.background = color;
          return elm;
        });

        //reset the global store
        setStore({ demo: demo });
      },
    },
  };
};

export default getState;
