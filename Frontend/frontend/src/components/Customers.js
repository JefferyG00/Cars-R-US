import React, { useState, useEffect } from "react";
import axios from "axios";

const Customers = () => {
    const [customers, setCustomers] = useState([]);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');

    useEffect(() => {
        fetchCustomers();
    }, []);

    const fetchCustomers = async () => {
        const response = await axios.get('http://localhost:5000/customers');
        setCustomers(response.data);  
    };

    const addCustomer = async () => {
        const response = await axios.post('http://localhost:5000/customers', { name, email });
        setCustomers([...customers, response.data]);
        setName('');
        setEmail('');
    };

    return (
        <div>
            <h1>Customers</h1>
            <ul>
                {customers.map(customer => (
                    <li key={customer.id}>{customer.name} - {customer.email}</li>
                ))}
            </ul>
            <input
                type="text"
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <button onClick={addCustomer}>Add Customer</button>
        </div>
    );
};

export default Customers