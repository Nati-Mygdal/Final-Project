import React from 'react'

function Dish({name,description,imageUrl,price,isVegeterian,isGlutenFree}) {
  return (
    <div>
      <div className="col s5" style={{ height: 'auto' }}>
    <img src={imageUrl} width="200px" height="200px" alt='#' style={{margin:'4px',borderRadius:'20vh',maxWidth:'100%',maxHeight:'100%'}}/>
  </div>
  <div className="col s7">
    <h5 className="title">{name}</h5>
    <section>{description}
      <div>
          {isVegeterian && (
            <img src={process.env.PUBLIC_URL + '/vegan.png'} height="30px" width="30px" alt='#'/>
          )}
          {isGlutenFree && (
            <img src={process.env.PUBLIC_URL + '/noglut.png'} height="45px" width="45px" alt='#'/>
          )}
      </div>
      <h5>{price}$</h5>
    </section>
    </div>
    </div>
  )
}

export default Dish