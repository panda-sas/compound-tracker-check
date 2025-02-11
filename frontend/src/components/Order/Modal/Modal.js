import React from "react";
import "./Modal.css";

const Modal = ({ isOpen, onClose, orderDetails }) => {
  if (!isOpen) return null;

  console.log("Order Details in Modal:", orderDetails);


  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <h2>Order Details</h2>
        <p>
          <strong>Order ID:</strong> {orderDetails.OrderID}
        </p>
        <p>
          <strong>Shipment Date:</strong>{" "}
          {new Date(orderDetails.ShipmentDate).toLocaleDateString()}
        </p>

        <p>
          <strong>Comments:</strong> {orderDetails.Comments}
        </p>
        <p>
          <strong>Tracking ID:</strong> {orderDetails.TrackingID}
        </p>
        <p>
          <strong>Scientist Name:</strong> {orderDetails.ScientistName || "N/A"}
        </p>
        <p>
          <strong>Dispatcher Name:</strong>{" "}
          {orderDetails.DispatcherName || "N/A"}
        </p>

        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default Modal;
