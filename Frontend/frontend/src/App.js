import React, { useState, } from 'react';
import axios from 'axios';
import './components/styles.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dealerships from './components/Dealerships';
import Cars from './components/Cars';
import Customers from './components/Customers';
import Sales from './components/Sales';
import ServiceAppointments from './components/ServiceAppointments';
import Cart from './components/Cart';

const App = () => {
  const [services] = useState([
    { name: 'Oil Change', description: 'Change the oil in your car', price: 29.99 },
    { name: 'Tire Rotation', description: 'Rotate your tires', price: 19.99 },
    { name: 'Car Wash', description: 'Exterior and interior car wash', price: 14.99 }
  ]);

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
        <div>
          <Navbar />
          <Routes>
            <Route path="/dealerships" element={<Dealerships />} />
            <Route path="/cars" element={<Cars />} />
            <Route path="/customers" element={<Customers />} />
            <Route path="/sales" element={<Sales />} />
            <Route path="/ServiceAppointments" element={<ServiceAppointments services={services} addToCart={addToCart} />} />
            <Route path="/cart" element={<Cart cartItems={cartItems} removeFromCart={removeFromCart} />} />
            <Route path="/" element={<h1>Welcome to Cars-R-Us</h1>} />
          </Routes>
        </div>
      </Router>
    );
  };

export default App;
