// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/HomePage';  // Győződj meg róla, hogy a Home.js itt van

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />  {/* Home oldal renderelése */}
      </Routes>
    </Router>
  );
}

export default App;
