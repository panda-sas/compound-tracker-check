import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom"; // Use Routes instead of Switch
import Orders from "./components/Order/Orders";
import Projects from "./components/Projects";
import Navigation from "./components/Navigation";

function App() {
  return (
    <Router>
      <div>
        <h1>Compound Tracker</h1>
        <Navigation />
        <Routes> 
          <Route path="/orders" element={<Orders />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/" element={<h2>Welcome to Compound Tracker</h2>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
