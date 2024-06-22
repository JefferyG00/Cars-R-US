import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CarList = () => {
    const [cars, setCars] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/cars')
            .then(response => setCars(response.data))
            .catch(error => console.log(error));
    }, []);

    return (
        <div>
            <h1>Cars</h1>
            <ul>
                {cars.map(car => (
                    <li key={car.id}>{car.make} {car.model} ({car.year}) - ${car.price}</li>
                ))}
            </ul>
        </div>
    );
};

export default CarList;
