import React, { useState } from 'react';
import SearchBrowsePill from './SearchBrowsePill';
import SearchBar from './SearchBar';

const App = () => {
  const [activeTab, setActiveTab] = useState('search');

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8 text-center">
          <SearchBrowsePill activeTab={activeTab} setActiveTab={setActiveTab} />
          
          <div className="mt-4">
            {activeTab === 'search' ? (
              <SearchBar />
            ) : (
              <div className="browse-content">
                <h3>Browse Acronyms</h3>
                <p>Browse functionality will be implemented here.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;