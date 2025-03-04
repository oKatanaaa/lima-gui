import React, { useRef, useState } from 'react';
import Settings from './Settings';

const Header = () => {
  const fileInputRef = useRef(null);
  const [showSettings, setShowSettings] = useState(false);

  const handleImportClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    // Check if file is a JSONL file
    if (!file.name.endsWith('.jsonl')) {
      alert('Please select a JSONL file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/import', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const result = await response.json();
      alert(`Successfully imported ${result.chats_added} chats!`);
      
      // Reload the page to refresh the chat list
      window.location.reload();
    } catch (error) {
      console.error('Import failed:', error);
      alert(`Failed to import file: ${error.message}`);
    }

    // Clear the file input
    event.target.value = null;
  };

  const handleExportClick = async () => {
    try {
      // Create the filename with the current date
      const filename = `lima-chats-${new Date().toISOString().slice(0, 10)}.jsonl`;
      
      // Use fetch with the correct URL (need to account for proxy)
      const response = await fetch(`/export?filename=${encodeURIComponent(filename)}`, {
        method: 'GET',
      });
      
      if (!response.ok) {
        throw new Error(`Server responded with status: ${response.status}`);
      }
      
      // Get the response as a blob
      const blob = await response.blob();
      
      // Create a downloadable link and trigger click
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      
      // Clean up
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (error) {
      console.error('Export failed:', error);
      alert(`Failed to export chats: ${error.message}`);
    }
  };

  const handleSettingsClick = () => {
    setShowSettings(true);
  };

  return (
    <header className="header">
      <div className="logo-container">
        <span className="app-title">LIMA-GUI</span>
      </div>
      <div className="header-buttons">
        <button className="primary-button" onClick={handleImportClick}>Import</button>
        <input
          type="file"
          ref={fileInputRef}
          style={{ display: 'none' }}
          accept=".jsonl"
          onChange={handleFileChange}
        />
        <button className="primary-button" onClick={handleExportClick}>Export</button>
        <button className="secondary-button" onClick={handleSettingsClick}>Settings</button>
      </div>
      
      {showSettings && (
        <Settings onClose={() => setShowSettings(false)} />
      )}
    </header>
  );
};

export default Header;