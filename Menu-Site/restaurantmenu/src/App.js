import React from "react";
import { Routes,Route, Link } from "react-router-dom";
import MainPage from "./Pages/MainPage";
import MenuPage from "./Pages/MenuPage";
import axios from "axios";
import { API_URL } from "./config";
import { AppBar, Box, Button, Toolbar, Typography } from "@mui/material";

function App() {
  const [categories,setCategories] = React.useState([])

  React.useEffect(()=>{
    fetchCategories()
  },[])

  function fetchCategories() {
    axios.get(`${API_URL}/categories`).then(response=>{
      setCategories(response.data)
    })
  }

  return (
    <div>
      <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" className="black">
        <Toolbar>
          <img src={process.env.PUBLIC_URL + "/logo.png"} alt="#" height='62em' width='125em'/>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1,marginLeft:'65vh'}}>
            The Bites of Python
          </Typography>
                <Button 
                  color="inherit"
                  component={Link}
                  to={'/menu'}
                >
                 Menu
                </Button>
          <Button 
          color="inherit"
          component={Link}
          to={'/'}
          >Home</Button>
        </Toolbar>
      </AppBar>
    </Box>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path="/menu" element={<MenuPage categories={categories}/>}/>
        <Route path="/category/:id" element={<MenuPage categories={categories}/>}/>
      </Routes>
    </div>
  );
}

export default App;
