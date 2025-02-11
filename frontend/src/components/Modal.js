// src/components/Modal.js
import React from "react";
import "./Modal.css";

function Modal({ order, onClose }) {
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <h2>Order Details</h2>
        <p><strong>Order ID:</strong> {order.OrderID}</p>
        <p><strong>Order Date:</strong> {new Date(order.ShipmentDate).toLocaleDateString()}</p>
        <p><strong>Comments:</strong> {order.Comments}</p>
        <p><strong>Number of Shipments:</strong> {order.NoOfShipments}</p>
        <p><strong>Tracking ID:</strong> {order.TrackingID}</p>
        <p><strong>Is Complete:</strong> {order.isComplete ? "Yes" : "No"}</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

export default Modal;
