// src/components/Cart.js
import React, { useState, useEffect } from 'react';

function Cart({ customerId }) {
    const [cartItems, setCartItems] = useState([]);

    useEffect(() => {
        fetch(`http://localhost:5000/cart?customer_id=${customerId}`)
            .then(response => response.json())
            .then(data => setCartItems(data));
    }, [customerId]);

    const removeFromCart = (id) => {
        fetch(`http://localhost:5000/cart/${id}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(() => {
            setCartItems(cartItems.filter(item => item.id !== id));
        });
    };

    return (
        <div>
            <h1>Cart</h1>
            <ul>
                {cartItems.map(item => (
                    <li key={item.id}>
                        Service ID: {item.service_id}, Description: {item.service_description}, Quantity: {item.quantity}
                        <button onClick={() => removeFromCart(item.id)}>Remove</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Cart;
