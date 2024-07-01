import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Customers = () => {
    const [customers, setCustomers] = useState([]);
    const [selectedCustomer, setSelectedCustomer] = useState(null);
    const [reviews, setReviews] = useState([]);

    useEffect(() => {
        fetchCustomers();
    }, []);

    useEffect(() => {
        if (selectedCustomer) {
            fetchReviews(selectedCustomer.id);
        }
    }, [selectedCustomer]);

    const fetchCustomers = async () => {
        try {
            const response = await axios.get('http://localhost:5000/customers');
            setCustomers(response.data);
        } catch (error) {
            console.error('Error fetching customers:', error);
        }
    };

    const fetchReviews = async (customerId) => {
        try {
            const response = await axios.get(`http://localhost:5000/customers/${customerId}/reviews`);
            setReviews(response.data);
        } catch (error) {
            console.error('Error fetching reviews:', error);
        }
    };

    return (
        <div>
            <h1>Customers</h1>
            <ul>
                {customers.map((customer) => (
                    <li key={customer.id} onClick={() => setSelectedCustomer(customer)}>
                        {customer.name}
                    </li>
                ))}
            </ul>

            {selectedCustomer && (
                <div>
                    <h2>Reviews for {selectedCustomer.name}</h2>
                    <ul>
                        {reviews.map((review) => (
                            <li key={review.id}>
                                <p><strong>Rating:</strong> {review.rating}</p>
                                <p>{review.comment}</p>
                                <p><em>Created At: {review.created_at}</em></p>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default Customers;
