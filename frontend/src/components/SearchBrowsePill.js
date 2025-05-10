import React from 'react';

const SearchBrowsePill = ({ activeTab, setActiveTab }) => {
  return (
    <div className="nav-pills-container">
      <ul className="nav nav-pills justify-content-center">
        <li className="nav-item">
          <button 
            className={`nav-link ${activeTab === 'search' ? 'active' : ''}`}
            onClick={() => setActiveTab('search')}
          >
            Search
          </button>
        </li>
        <li className="nav-item">
          <button 
            className={`nav-link ${activeTab === 'browse' ? 'active' : ''}`}
            onClick={() => setActiveTab('browse')}
          >
            Browse
          </button>
        </li>
      </ul>
    </div>
  );
};

export default SearchBrowsePill;