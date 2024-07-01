import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Customers = () => {
    const [customers, setCustomers] = useState([]);
    const [selectedCustomer, setSelectedCustomer] = useState(null);
    const [reviews, setReviews] = useState([]);
    const [newReview, setNewReview] = useState({ comment: '', rating: 1 });

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

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewReview({ ...newReview, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`http://localhost:5000/customers/${selectedCustomer.id}/reviews`, newReview);
            setReviews([...reviews, response.data.review]);
            setNewReview({ comment: '', rating: 1 });
        } catch (error) {
            console.error('Error adding review:', error);
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
                                <p><strong>{review.customer_name}</strong> ({review.rating} stars)</p>
                                <p>{review.comment}</p>
                            </li>
                        ))}
                    </ul>

                    <form onSubmit={handleSubmit}>
                        <h2>Leave a Review</h2>
                        <div>
                            <label>Comment:</label>
                            <textarea
                                name="comment"
                                value={newReview.comment}
                                onChange={handleInputChange}
                                required
                            />
                        </div>
                        <div>
                            <label>Rating:</label>
                            <select
                                name="rating"
                                value={newReview.rating}
                                onChange={handleInputChange}
                                required
                            >
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                            </select>
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </div>
            )}
        </div>
    );
};

export default Customers;