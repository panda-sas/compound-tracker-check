import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Orders from './components/Orders';
import Compounds from './components/Compounds';
import Projects from './components/Projects';
import CheckInOut from './components/CheckInOut';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/orders" element={<Orders />} />
          <Route path="/compounds" element={<Compounds />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/checkinout" element={<CheckInOut />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
