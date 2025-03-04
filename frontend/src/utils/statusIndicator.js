/**
 * A utility for showing status messages without triggering React re-renders
 */

// Create a container for status messages if it doesn't exist
const initializeStatusContainer = () => {
    if (!document.getElementById('global-status-container')) {
      const container = document.createElement('div');
      container.id = 'global-status-container';
      container.style.position = 'fixed';
      container.style.bottom = '20px';
      container.style.right = '20px';
      container.style.zIndex = '1000';
      document.body.appendChild(container);
    }
  };
  
  // Show a status message
  export const showStatus = (messageId, status) => {
    initializeStatusContainer();
    const container = document.getElementById('global-status-container');
    
    // Check if status element for this message already exists
    let statusElement = document.getElementById(`status-${messageId}`);
    
    if (!statusElement) {
      // Create new status element if it doesn't exist
      statusElement = document.createElement('div');
      statusElement.id = `status-${messageId}`;
      statusElement.style.backgroundColor = '#ffffff';
      statusElement.style.border = '1px solid #e0e0e0';
      statusElement.style.borderRadius = '4px';
      statusElement.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
      statusElement.style.padding = '8px 12px';
      statusElement.style.marginBottom = '8px';
      statusElement.style.fontSize = '14px';
      statusElement.style.display = 'flex';
      statusElement.style.alignItems = 'center';
      statusElement.style.opacity = '0';
      statusElement.style.transition = 'opacity 0.3s ease';
      
      container.appendChild(statusElement);
      
      // Animate in
      setTimeout(() => {
        statusElement.style.opacity = '1';
      }, 10);
    }
    
    // Set content based on status
    if (status === 'saving') {
      statusElement.innerHTML = `
        <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #5e5cff; margin-right: 8px;"></div>
        <span>Saving message #${messageId}...</span>
      `;
      statusElement.style.color = '#5e5cff';
    } else if (status === 'saved') {
      statusElement.innerHTML = `
        <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #10b981; margin-right: 8px;"></div>
        <span>Message #${messageId} saved</span>
      `;
      statusElement.style.color = '#10b981';
      
      // Remove after delay
      setTimeout(() => {
        if (statusElement.parentNode) {
          statusElement.style.opacity = '0';
          setTimeout(() => {
            if (statusElement.parentNode) {
              statusElement.parentNode.removeChild(statusElement);
            }
          }, 300);
        }
      }, 3000);
    } else if (status === 'error') {
      statusElement.innerHTML = `
        <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #e11d48; margin-right: 8px;"></div>
        <span>Error saving message #${messageId}</span>
      `;
      statusElement.style.color = '#e11d48';
      
      // Remove after delay
      setTimeout(() => {
        if (statusElement.parentNode) {
          statusElement.style.opacity = '0';
          setTimeout(() => {
            if (statusElement.parentNode) {
              statusElement.parentNode.removeChild(statusElement);
            }
          }, 300);
        }
      }, 5000);
    }
  };