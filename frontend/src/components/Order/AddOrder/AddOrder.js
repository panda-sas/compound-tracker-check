import React, { useState, useEffect } from "react";
import './AddOrder.css'; // Ensure you have this imported CSS

const AddOrder = ({ onAdd }) => {
  const [order, setOrder] = useState({
    shipmentDate: "",
    comments: "",
    trackingID: "",
    scientistName: "",
    dispatcherName: "",
  });
  
  const [scientists, setScientists] = useState([]);
  const [dispatchers, setDispatchers] = useState([]);
  const [isFormVisible, setIsFormVisible] = useState(false); // Toggle visibility of form

  useEffect(() => {
    // Fetch scientist names from the backend
    fetch("http://localhost:8000/scientists/")
      .then((response) => response.json())
      .then((data) => setScientists(data))
      .catch((error) => console.error("Error fetching scientists:", error));

    // Fetch dispatcher names from the backend
    fetch("http://localhost:8000/dispatchers/")
      .then((response) => response.json())
      .then((data) => setDispatchers(data))
      .catch((error) => console.error("Error fetching dispatchers:", error));
  }, []);

  const handleChange = (e) => {
    setOrder({ ...order, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd(order);
    setOrder({
      shipmentDate: "",
      comments: "",
      trackingID: "",
      scientistName: "",
      dispatcherName: "",
    });
    setIsFormVisible(false); // Hide the form after submission
  };

  return (
    <div className="add-order-container">
      <div className="content-container">
        {/* Icon button to toggle form visibility */}
        <button
          onClick={() => setIsFormVisible(!isFormVisible)}
          className="add-button"
        >
          ➕ {/* Plus sign icon */}
        </button>

        {/* Show form only if isFormVisible is true */}
        {isFormVisible && (
          <div className="form-container">
            <form onSubmit={handleSubmit} className="add-order-form">
              <h2>Add Order</h2>
              <div className="form-group">
                <label>Shipment Date</label>
                <input
                  type="date"
                  name="shipmentDate"
                  value={order.shipmentDate}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Comments</label>
                <input
                  type="text"
                  name="comments"
                  placeholder="Comments"
                  value={order.comments}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Tracking ID</label>
                <input
                  type="text"
                  name="trackingID"
                  placeholder="Tracking ID"
                  value={order.trackingID}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label>Scientist Name</label>
                <select
                  name="scientistName"
                  value={order.scientistName}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select Scientist</option>
                  {scientists.map((scientist) => (
                    <option key={scientist.ScientistID} value={scientist.ScientistName}>
                      {scientist.ScientistName}
                    </option>
                  ))}
                </select>
              </div>
              <div className="form-group">
                <label>Dispatcher Name</label>
                <select
                  name="dispatcherName"
                  value={order.dispatcherName}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select Dispatcher</option>
                  {dispatchers.map((dispatcher) => (
                    <option key={dispatcher.DispatcherId} value={dispatcher.DispatcherName}>
                      {dispatcher.DispatcherName}
                    </option>
                  ))}
                </select>
              </div>
              <div className="form-group">
                <button type="submit" className="submit-button">Add Order</button>
              </div>
            </form>
          </div>
        )}
      </div>
    </div>
  );
};

export default AddOrder;
