import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dealerships from './components/Dealerships';
import Cars from './components/Cars';
import Customers from './components/Customers';
import Sales from './components/Sales';
import ServiceAppointments from './components/ServiceAppointments';

const App = () => {
    return (
      <Router>
        <div>
          <Navbar />
          <Routes>
            <Route path="/dealerships" element={<Dealerships />} />
            <Route path="/cars" element={<Cars />} />
            <Route path="/customers" element={<Customers />} />
            <Route path="/sales" element={<Sales />} />
            <Route path="/ServiceAppointments" element={<ServiceAppointments />} />
            <Route path="/" element={<h1>Welcome to Cars-R-Us</h1>} />
          </Routes>
        </div>
      </Router>
    );
  };

export default App;
