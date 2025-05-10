import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './components/App';

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('react-app');
  if (container) {
    const root = createRoot(container);
    root.render(<App />);
  }
});