import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ServiceAppointments = ({ addToCart }) => {
  const [services, setServices] = useState([]);

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const response = await axios.get('http://localhost:5000/serviceappointments');
        setServices(response.data);
      } catch (error) {
        console.error('Error fetching services:', error);
      }
    };

    fetchServices();
  }, []);

  return (
    <div>
      <h2>Available Services</h2>
      <ul>
        {services.map((service) => (
          <li key={service.id}>
            <div>{service.description}</div>
            <div>${service.price}</div>
            <button onClick={() => addToCart(service)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ServiceAppointments;
