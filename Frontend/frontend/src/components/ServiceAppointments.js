import React from 'react';

const ServiceAppointments = ({ services, addToCart }) => {
  return (
    <div>
      <h2>ServiceAppointments</h2>
      <ul>
        {services.map((service, index) => (
          <li key={index}>
            <h3>{service.name}</h3>
            <p>{service.description}</p>
            <p>Price: ${service.price}</p>
            <button onClick={() => addToCart(service)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ServiceAppointments;
