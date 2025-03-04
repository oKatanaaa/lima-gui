import React, { useRef, useEffect, useState } from 'react';
import { debounce } from '../utils/debounce';
import { showStatus } from '../utils/statusIndicator';

// SVG Icon Components
const EditIcon = () => (
  <svg className="icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
  </svg>
);

const DeleteIcon = () => (
  <svg className="icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <polyline points="3 6 5 6 21 6"></polyline>
    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
  </svg>
);

const PlayIcon = () => (
  <svg className="icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <circle cx="12" cy="12" r="10"></circle>
    <polygon points="10 8 16 12 10 16 10 8"></polygon>
  </svg>
);

const Message = ({ message, onUpdate, onDelete, onGenerate }) => {
  // Create a ref for the contentEditable div
  const contentEditableRef = useRef(null);
  // Store the previous content to compare changes
  const [previousContent, setPreviousContent] = useState(message.content);
  // Store cursor position data
  const cursorPositionRef = useRef({ start: 0, end: 0 });
  
  // Create a debounced update function
  const debouncedUpdate = useRef(
    debounce((content) => {
      // Show saving status
      showStatus(message.id, 'saving');
      
      // Send the update to the server
      onUpdate({ ...message, content })
        .then(() => {
          // Show saved status
          showStatus(message.id, 'saved');
        })
        .catch(error => {
          console.error("Error saving message:", error);
          showStatus(message.id, 'error');
        });
    }, 750) // 750ms debounce delay
  ).current;

  // Get message style class based on role
  const getMessageClass = (role) => {
    switch (role) {
      case 'system': return 'system-message';
      case 'user': return 'user-message';
      case 'assistant': return 'assistant-message';
      case 'function': return 'function-message';
      default: return 'user-message';
    }
  };
  
  // Get role style class 
  const getRoleClass = (role) => {
    switch (role) {
      case 'system': return 'role-system';
      case 'user': return 'role-user';
      case 'assistant': return 'role-assistant';
      case 'function': return 'role-function';
      default: return 'role-user';
    }
  };

  // Save cursor position
  const saveCursorPosition = () => {
    if (document.activeElement !== contentEditableRef.current) return;
    
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
      const range = selection.getRangeAt(0);
      const preCaretRange = range.cloneRange();
      preCaretRange.selectNodeContents(contentEditableRef.current);
      preCaretRange.setEnd(range.startContainer, range.startOffset);
      
      cursorPositionRef.current = {
        start: preCaretRange.toString().length,
        end: preCaretRange.toString().length + range.toString().length
      };
    }
  };

  // Restore cursor position
  const restoreCursorPosition = () => {
    if (!contentEditableRef.current) return;
    
    // Only restore if we have a position to restore to and content has changed
    if (contentEditableRef.current.textContent !== previousContent) {
      setPreviousContent(contentEditableRef.current.textContent);
      return;
    }
    
    const selection = window.getSelection();
    const range = document.createRange();
    
    let charIndex = 0;
    let foundStart = false;
    let foundEnd = false;
    
    iterateTextNodes(contentEditableRef.current, (node) => {
      const nextCharIndex = charIndex + node.length;
      
      if (!foundStart && cursorPositionRef.current.start >= charIndex && cursorPositionRef.current.start <= nextCharIndex) {
        range.setStart(node, cursorPositionRef.current.start - charIndex);
        foundStart = true;
      }
      
      if (!foundEnd && cursorPositionRef.current.end >= charIndex && cursorPositionRef.current.end <= nextCharIndex) {
        range.setEnd(node, cursorPositionRef.current.end - charIndex);
        foundEnd = true;
      }
      
      if (foundStart && foundEnd) {
        return true; // Stop iteration
      }
      
      charIndex = nextCharIndex;
      return false; // Continue iteration
    });
    
    if (foundStart && foundEnd) {
      selection.removeAllRanges();
      selection.addRange(range);
    }
  };

  // Helper function to iterate through text nodes
  const iterateTextNodes = (element, callback) => {
    if (element.nodeType === Node.TEXT_NODE) {
      return callback(element);
    }
    
    for (let i = 0; i < element.childNodes.length; i++) {
      const result = iterateTextNodes(element.childNodes[i], callback);
      if (result) return true;
    }
    
    return false;
  };

  // Handle content changes
  const handleContentChange = (e) => {
    saveCursorPosition();
    const content = e.target.innerText;
    debouncedUpdate(content);
  };
  
  // Effect to restore cursor position after re-renders when content doesn't change
  useEffect(() => {
    // When the message content changes from outside, update our previousContent
    if (message.content !== previousContent) {
      setPreviousContent(message.content);
    } else {
      // When content hasn't changed externally, try to restore cursor
      restoreCursorPosition();
    }
  }, [message.content, previousContent]);
  
  return (
    <div className="message">
      <div className="message-header">
        <select 
          className={`role-select ${getRoleClass(message.role)}`} 
          value={message.role}
          onChange={(e) => {
            // Show saving status
            showStatus(message.id, 'saving');
            
            // Update role
            onUpdate({ ...message, role: e.target.value })
              .then(() => {
                showStatus(message.id, 'saved');
              })
              .catch(error => {
                console.error("Error updating role:", error);
                showStatus(message.id, 'error');
              });
          }}
        >
          <option value="system">system</option>
          <option value="user">user</option>
          <option value="assistant">assistant</option>
          <option value="function">function</option>
        </select>
        <div className="message-actions">
          {message.role === 'assistant' && (
            <button 
              className="message-action" 
              title="Generate with AI"
              onClick={onGenerate}
            >
              <PlayIcon />
            </button>
          )}
          <button className="message-action" title="Edit">
            <EditIcon />
          </button>
          <button className="message-action delete-action" title="Delete" onClick={onDelete}>
            <DeleteIcon />
          </button>
        </div>
      </div>
      <div className={`message-content ${getMessageClass(message.role)}`}>
        <div 
          ref={contentEditableRef}
          className="content-editable" 
          contentEditable={true}
          onInput={handleContentChange}
          onBlur={saveCursorPosition}
          onKeyUp={saveCursorPosition}
          onMouseUp={saveCursorPosition}
          suppressContentEditableWarning={true}
          dangerouslySetInnerHTML={{ __html: message.content }}
        />
      </div>
    </div>
  );
};

export default Message;