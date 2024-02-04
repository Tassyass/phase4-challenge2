import React, { useState, useEffect } from 'react';

function App() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Fetch restaurants from the backend API
    fetch('http://localhost:5000/restaurants')
      .then(response => response.json())
      .then(data => setRestaurants(data))
      .catch(error => console.error('Error fetching restaurants:', error));
  }, []);

  return (
    <div>
      <h1>Pizza App</h1>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            <strong>{restaurant.name}</strong> - {restaurant.address}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
