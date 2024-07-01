import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Sales = () => {
    const [sales, setSales] = useState([]);

    useEffect(() => {
        fetchSales();
    }, []);

    const fetchSales = async () => {
        try {
            const response = await axios.get('http://localhost:5000/sales');
            setSales(response.data);
        } catch (error) {
            console.error('Error fetching sales:', error);
        }
    };

    return (
        <div>
            <h1>Sales Data</h1>
            <ul>
                {sales.map(sale => (
                    <li key={sale.id}>
                        <p>Car: {sale.car.make} {sale.car.model} ({sale.car.year})</p>
                        <p>Customer: {sale.customer.name} ({sale.customer.email})</p>
                        <p>Date: {sale.date}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Sales;
