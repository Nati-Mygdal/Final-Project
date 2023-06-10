import React from 'react'
import { Button} from '@mui/material'
import { Link, useNavigate } from 'react-router-dom'
function MainPage() {
  const navigate = useNavigate()

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh',backgroundImage: "url('footer.png')"}}>
      <Button 
      variant="contained" 
      sx={{padding:'6vh 6vh 6vh 6vh',backgroundColor:'white',borderRadius:'3vh'}}
      onClick={() => {navigate('/menu')}}>
        <Link to={'/menu'} style={{fontWeight:'bolder',fontSize:'20px',textTransform:'none'}}>View Menu</Link>
      </Button>
    </div>
  )
}

export default MainPage