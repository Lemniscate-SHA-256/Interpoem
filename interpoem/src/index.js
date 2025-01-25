import React from 'react';
import ReactDOM from 'react-dom/client'; // New method in React 18 for rendering
import './index.css'; // Optional, if you want to add custom styles
import App from './App'; // Import the main App component

// Render the App component inside the root div in index.html
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
