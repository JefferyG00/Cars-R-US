import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">Cars-R-Us</Link>
      </div>
      <div className="navbar-links">
        <Link to="/dealerships">Dealerships</Link>
        <Link to="/cars">Cars</Link>
        <Link to="/customers">Customers</Link>
        <Link to="/sales">Sales</Link>
        <Link to="/serviceAppointments">Service Appointments</Link>
        <Link to="/cart">Cart</Link>
      </div>
    </nav>
  );
};

export default Navbar;
