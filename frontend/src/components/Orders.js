import React, { useState, useEffect } from "react";
import Modal from "./Modal";
import "./Orders.css";

function Orders() {
  const [orders, setOrders] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedOrder, setSelectedOrder] = useState(null);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/order-details");
        const data = await response.json();
        console.log("Fetched Orders Data:", data);  // Debugging line
        setOrders(data);
      } catch (error) {
        console.error("Error fetching orders:", error);
        setOrders([]);  // Ensure orders is always an array
      }
    };
  
    fetchOrders();
  }, []);
  

   

  const openModal = async (order) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/order-details/${order.OrderID}`);
      const data = await response.json();
      console.log("Fetched Order Details:", data); // Debugging Log
      setSelectedOrder(data);
      setIsModalOpen(true);
    } catch (error) {
      console.error("Error fetching order details:", error);
    }
  };
  

  const closeModal = () => {
    setIsModalOpen(false);
    setSelectedOrder(null);
  };

  

  return (
    <div className="orders-container">
      <h1>Orders</h1>
      {orders.map((order) => (
        <div key={order.OrderID} className="order-card">
          <h2>Order ID: {order.OrderID}</h2>
          <p>Shipment Date: {new Date(order.ShipmentDate).toLocaleDateString()}</p>
          <span
            className={`order-status ${
              order.isComplete ? "completed" : "pending"
            }`}
          >
            {order.isComplete ? "Completed" : "Pending"}
          </span>
          <button onClick={() => openModal(order)}>View Details</button>
        </div>
      ))}

      <Modal
        isOpen={isModalOpen}
        onClose={closeModal}
        orderDetails={selectedOrder}
      />
    </div>
  );
}

export default Orders;
