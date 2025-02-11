import React, { useState, useEffect } from 'react';

const Orders = () => {
    const [orders, setOrders] = useState([]);
    const [loading, setLoading] = useState(true);
    
    // Fetch orders from the backend when the component mounts
    useEffect(() => {
      fetch('http://127.0.0.1:8000/orders') // Change to FastAPI URL
          .then(response => response.json())
          .then(data => {
              setOrders(data);
              setLoading(false);
          })
          .catch(error => console.error('Error fetching orders:', error));
  }, []);
    if (loading) {
        return <p>Loading...</p>;
    }

    return (
        <div>
            <h2>Orders List</h2>
            <ul>
                {orders.map(order => (
                    <li key={order.id}>
                        {order.name} - {order.status}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Orders;
