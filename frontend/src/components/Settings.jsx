import React, { useState, useEffect } from 'react';
import './Settings.css';

const Settings = ({ onClose }) => {
  const [openAIConfig, setOpenAIConfig] = useState({
    enabled: false,
    model: 'gpt-4o-mini',
    temperature: 0.7,
    api_type: 'chat',
    max_completion_tokens: 100,
    api_base: '',
    api_key: '',
    extra_body: null
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch the current OpenAI configuration
  useEffect(() => {
    const fetchConfig = async () => {
      try {
        setLoading(true);
        const response = await fetch('/settings/openai');
        if (!response.ok) {
          throw new Error(`API error: ${response.status}`);
        }
        const data = await response.json();
        setOpenAIConfig(data);
        setError(null);
      } catch (err) {
        console.error('Failed to fetch OpenAI config:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchConfig();
  }, []);

  // Handle input changes
  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target;
    
    // For checkbox inputs, use the checked value
    // For number inputs, convert to number
    // For other inputs, use the value as is
    const newValue = type === 'checkbox' ? checked :
                     type === 'number' ? parseFloat(value) : value;
    
    setOpenAIConfig({
      ...openAIConfig,
      [name]: newValue
    });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('/settings/openai', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(openAIConfig)
      });
      
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      
      alert('Settings saved successfully!');
      onClose();
    } catch (err) {
      console.error('Failed to save settings:', err);
      setError(err.message);
    }
  };

  if (loading) {
    return <div className="settings-modal loading">Loading settings...</div>;
  }

  return (
    <div className="settings-modal">
      <div className="settings-modal-content">
        <div className="settings-header">
          <h2>Settings</h2>
          <button className="close-button" onClick={onClose}>×</button>
        </div>
        
        {error && (
          <div className="error-message">
            Error: {error}
          </div>
        )}
        
        <form onSubmit={handleSubmit}>
          <div className="settings-section">
            <h3>OpenAI API Configuration</h3>
            
            <div className="form-group">
              <label>
                <input
                  type="checkbox"
                  name="enabled"
                  checked={openAIConfig.enabled}
                  onChange={handleInputChange}
                />
                Enable OpenAI API
              </label>
            </div>
            
            <div className="form-group">
              <label>API Key:</label>
              <input
                type="password"
                name="api_key"
                value={openAIConfig.api_key || ''}
                onChange={handleInputChange}
                placeholder="sk-..."
              />
            </div>
            
            <div className="form-group">
              <label>API Base URL:</label>
              <input
                type="text"
                name="api_base"
                value={openAIConfig.api_base || ''}
                onChange={handleInputChange}
                placeholder="https://api.openai.com/v1 (leave empty for default)"
              />
            </div>
            
            <div className="form-group">
              <label>Model:</label>
              <input
                type="text"
                name="model"
                value={openAIConfig.model}
                onChange={handleInputChange}
              />
            </div>
            
            <div className="form-group">
              <label>Temperature:</label>
              <input
                type="range"
                name="temperature"
                min="0"
                max="1"
                step="0.1"
                value={openAIConfig.temperature}
                onChange={handleInputChange}
              />
              <span>{openAIConfig.temperature}</span>
            </div>
            
            <div className="form-group">
              <label>API Type:</label>
              <select
                name="api_type"
                value={openAIConfig.api_type}
                onChange={handleInputChange}
              >
                <option value="chat">Chat</option>
                <option value="completion">Completion</option>
              </select>
            </div>
            
            <div className="form-group">
              <label>Max Completion Tokens:</label>
              <input
                type="number"
                name="max_completion_tokens"
                value={openAIConfig.max_completion_tokens}
                onChange={handleInputChange}
                min="1"
                max="4096"
              />
            </div>
          </div>
          
          <div className="form-actions">
            <button type="submit" className="primary-button">Save Settings</button>
            <button type="button" className="secondary-button" onClick={onClose}>Cancel</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Settings;