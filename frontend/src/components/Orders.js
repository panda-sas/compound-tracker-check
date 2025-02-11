import React, { useState, useEffect } from "react";
import Modal from './Modal';
import "./Orders.css";

function Orders() {
  const [orders, setOrders] = useState([]);
  const [selectedOrder, setSelectedOrder] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/orders")
      .then((response) => response.json())
      .then((data) => setOrders(data))
      .catch((error) => console.error("Error fetching orders:", error));
  }, []);

  const openModal = (order) => {
    setSelectedOrder(order);
  };

  const closeModal = () => {
    setSelectedOrder(null);
  };

  return (
    <div className="orders-container">
      <h1>Orders</h1>
      {orders.map((order) => (
        <div key={order.OrderID} className="order-card">
          <h2>Order ID: {order.OrderID}</h2>
          <p>Order Date: {new Date(order.ShipmentDate).toLocaleDateString()}</p>
          <span className={`order-status ${order.isComplete ? 'completed' : 'pending'}`}>
            {order.isComplete ? 'Completed' : 'Pending'}
          </span>
          <button className="view-details-btn" onClick={() => openModal(order)}>
            View Details
          </button>
        </div>
      ))}

      {selectedOrder && (
        <Modal order={selectedOrder} onClose={closeModal} />
      )}
    </div>
  );
}

export default Orders;
