import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DealershipList = () => {
    const [dealerships, setDealerships] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/dealerships')
            .then(response => setDealerships(response.data))
            .catch(error => console.log(error));
    }, []);

    return (
        <div>
            <h1>Dealerships</h1>
            <ul>
                {dealerships.map(dealership => (
                    <li key={dealership.id}>{dealership.name} - {dealership.location}</li>
                ))}
            </ul>
        </div>
    );
};

export default DealershipList;
