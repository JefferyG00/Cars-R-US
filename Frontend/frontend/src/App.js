import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dealerships from './components/Dealerships';
import Cars from './components/Cars';
import Customers from './components/Customers';
import Sales from './components/Sales';
import ServiceAppointments from './components/ServiceAppointments';
import Cart from './components/Cart';
import './styles.css';

const App = () => {


  const [cartItems, setCartItems] = useState([]);

  const addToCart = (service) => {
    setCartItems([...cartItems, service]);
  };

  const removeFromCart = (index) => {
    const newCartItems = cartItems.filter((_, i) => i !== index);
    setCartItems(newCartItems);
  };


  return (
    <Router>
      <div className="container">
        <Navbar />
        <Routes>
          <Route path="/dealerships" element={<Dealerships />} />
          <Route path="/cars" element={<Cars />} />
          <Route path="/customers" element={<Customers />} />
          <Route path="/sales" element={<Sales />} />
          <Route path="/ServiceAppointments" element={<ServiceAppointments addToCart={addToCart} />} />
          <Route path="/cart" element={<Cart cartItems={cartItems} removeFromCart={removeFromCart} />} />
          <Route path="/" element={<h1>Welcome to Cars-R-Us</h1>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
