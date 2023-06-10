import axios from 'axios'
import React from 'react'
import Dish from '../Dish'
import { useParams } from 'react-router-dom'
import { API_URL } from '../config'
import { useNavigate } from 'react-router-dom'
import './MenuPage.css'

function MenuPage({categories}) {
  const [dishes,setDishes] = React.useState([])
  const [cat,setCat] = React.useState(null)
  const params = useParams()
  const navigate = useNavigate()

  React.useEffect(()=>{
    if (params.id === undefined) {
      setDishes([])
    } else {
      filterByCategory(params.id)
      setCat(categories.find(category => parseInt(category.id) === parseInt(params.id)))
    }
  },[params.id,categories])

  function filterByCategory(category_id) {
    axios.get(`${API_URL}/dishes?category_id=${category_id}`).then(response=>{
      setDishes(response.data)
    })
  }

  return (
    <div>
      <div className="row">
        <div className="col s2 scrollable" style={{ height: '100vh' }}>
          {/* <!-- Grey navigation panel --> */}
          <h3>Category</h3>
            <hr/><br/>
          
            {categories.map((category) => (
              <div className="col s12" key={category.id}>
                <div className="row" style={{width:'75%',marginLeft:'5vh'}}>
                <div 
                  className="card small red lighten-4 clickable" 
                  style={{borderRadius:'10px',height:'auto'}}
                  onClick={() => navigate(`/category/${category.id}`)}>
                  <div className="card-image">
                    <img src={category.imageUrl} alt="#" style={{ maxHeight: '45vh',borderRadius:'10px' }} />
                  </div>
                  <div className="card-content" style={{minHeight:'60px',wordWrap: 'break-word'}}>
                    <p style={{textAlign:'center',fontWeight:'bold',fontSize:'12px'}}>{category.name}</p>
                  </div>
                </div>
              </div>
          </div>
            ))}
        </div>

      <div className="col s8 scrollable" style={{ direction: 'rtl', height: '100vh' }}>
        {/* <!-- Teal page content  --> */}
        {params.id === undefined ? (
        categories.map(category => (
        <div>
              <h3 style={{textAlign:'center'}}>{category.name}</h3>
              <hr/> <br/>
            {category.dishes.map(dish => (
              <div className='row red lighten-4' style={{border:'1px solid black',borderRadius:'12px'}}>
                <ul className='collection'  style={{border:'none'}}>
                <li key={dish.id}>
                <Dish 
                name={dish.name} 
                description={dish.description} 
                price={dish.price} 
                imageUrl={dish.imageUrl}
                isGlutenFree={dish.is_gluten_free}
                isVegeterian={dish.is_vegeterian}/>
                </li>
               </ul>
              </div>
            ))}
        </div>
        ))
      ) : (
        <ul>
          {cat && (
              <div>
                <h3 style={{textAlign:'center'}}>{cat.name}</h3>
                <hr/> <br/>
              </div>
          )}
          {dishes.map(dish => (
            <div className='row red lighten-4' style={{border:'1px solid black',borderRadius:'12px'}}>
              <li key={dish.id} >
              <Dish 
              name={dish.name} 
              description={dish.description} 
              price={dish.price} 
              imageUrl={dish.imageUrl}
              isGlutenFree={dish.is_gluten_free}
              isVegeterian={dish.is_vegeterian}/>
              </li>
            </div>
          ))}
        </ul>
      )}
      </div>
      <div className='col s2 scrollable' style={{height:'100vh'}} >
        <h3>Sales</h3>
        <hr/>
        <ul>
          {/* first sale */}
          <li>
          <div className="card red lighten-4">
            <div className="card-content black-text">
              <span className="card-title" style={{fontWeight:'bold',fontStyle:"oblique"}}>Pizza Time</span>
                 <p style={{fontSize:'18px'}}>2 of our best pizza's for only 60$ <br/>
                 Are we doing this or what ?
                 </p>
           </div>
      </div>
          </li>
          {/* second sale */}
          <li>
          <div className="card red lighten-4">
            <div className="card-content black-text">
              <span className="card-title" style={{fontWeight:'bold',fontStyle:"oblique"}}>Burger Challenge!</span>
                 <p style={{fontSize:'18px'}}>Triple Burger for only 60$ <br/>
                 But if you finish it.. It's Free!
                 </p>
           </div>
      </div>
          </li>
          {/* third sale */}
          <li>
          <div className="card red lighten-4">
            <div className="card-content black-text">
              <span className="card-title" style={{fontWeight:'bold',fontStyle:"oblique"}}>Tiramisu SALE</span>
                 <p style={{fontSize:'18px'}}>Only for this week, our sweet Tiramisu for only 17$ <br/>
                 </p>
           </div>
      </div>
          </li>
          {/* fourth sale */}
          <li>
          <div className="card red lighten-4">
            <div className="card-content black-text">
              <span className="card-title" style={{fontWeight:'bold',fontStyle:"oblique"}}>3 Coctails Day</span>
                 <p style={{fontSize:'18px'}}>Get 3 coctails of your choice and pay only 30$ <br/>
                 What are you waiting for ?
                 </p>
           </div>
      </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
  )
}

export default MenuPage