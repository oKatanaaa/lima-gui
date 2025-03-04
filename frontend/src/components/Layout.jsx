import React from 'react';
import { Link } from 'react-router-dom';

// SVG Icons Components
const PlusIcon = () => (
  <svg className="icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <line x1="12" y1="5" x2="12" y2="19"></line>
    <line x1="5" y1="12" x2="19" y2="12"></line>
  </svg>
);

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

const CopyIcon = () => (
  <svg className="icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
  </svg>
);

const Layout = ({ children }) => {
  return (
    <div className="app">
      <Header />
      <div className="container">
        {children}
      </div>
    </div>
  );
};

const Header = () => {
  return (
    <header className="header">
      <div className="logo-container">
        <span className="app-title">LIMA-GUI</span>
      </div>
      <div className="header-buttons">
        <button className="primary-button">Import</button>
        <button className="primary-button">Export</button>
        <button className="secondary-button">Settings</button>
      </div>
    </header>
  );
};

export const ChatList = ({ chats, selectedChatId, onSelectChat, onCreateChat }) => {
  return (
    <div className="left-sidebar">
      <div className="sidebar-header">
        <h2 className="sidebar-title">Chats</h2>
        <button className="new-chat-button" onClick={onCreateChat}>
          + New Chat
        </button>
      </div>
      
      <div className="search-container">
        <input 
          type="text" 
          className="search-input" 
          placeholder="Search chats..." 
        />
      </div>
      
      <div className="chat-list">
        {chats.map(chat => (
          <div 
            key={chat.id} 
            className={`chat-item ${chat.id === selectedChatId ? 'active' : ''}`} 
            onClick={() => onSelectChat(chat.id)}
          >
            <div className="chat-header">
              <span className="chat-title">{chat.name || 'Untitled Chat'}</span>
              <span className="chat-lang">{chat.language || 'en'}</span>
            </div>
            <div className="chat-stats">
              <span>{chat.message_count || 0} messages</span>
              <span>{chat.tokens || 0} tokens</span>
            </div>
            {chat.tags && chat.tags.length > 0 && (
              <div className="chat-tags">
                {chat.tags.map((tag, idx) => (
                  <span key={idx} className="tag">{tag}</span>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export const ChatHeader = ({ chat, onChangeName, onChangeLanguage }) => {
  return (
    <div className="chat-header-bar">
      <input 
        type="text" 
        className="chat-name-input" 
        value={chat?.name || 'Untitled Chat'} 
        onChange={(e) => onChangeName(e.target.value)}
      />
      <div className="chat-options">
        <div className="chat-option-group">
          <span className="chat-option-label">Language:</span>
          <select 
            className="language-select" 
            value={chat?.language || 'en'} 
            onChange={(e) => onChangeLanguage(e.target.value)}
          >
            <option value="en">English</option>
            <option value="ru">Russian</option>
          </select>
        </div>
        <div className="chat-option-group">
          <span className="chat-option-label">Tokens: {chat?.tokens || 0}</span>
        </div>
        <button className="action-button" title="Add Message">
          <PlusIcon />
        </button>
        <button className="action-button" title="Copy Chat">
          <CopyIcon />
        </button>
        <button className="action-button" title="Delete Chat">
          <DeleteIcon />
        </button>
      </div>
    </div>
  );
};

export const MessageArea = ({ messages, onAddMessage, onUpdateMessage, onDeleteMessage, onGenerateMessage }) => {
  return (
    <div className="messages-container">
      {messages && messages.map(message => (
        <Message 
          key={message.id} 
          message={message} 
          onUpdate={(content) => onUpdateMessage(message.id, content)}
          onDelete={() => onDeleteMessage(message.id)}
          onGenerate={() => onGenerateMessage(message.id)}
        />
      ))}
      
      <div className="add-message">
        <select className="role-select role-new-message">
          <option value="user">user</option>
          <option value="assistant">assistant</option>
          <option value="system">system</option>
          <option value="function">function</option>
        </select>
        <button 
          className="add-message-button"
          onClick={(e) => {
            const select = e.target.previousElementSibling;
            onAddMessage(select.value);
          }}
        >
          Add Message
        </button>
      </div>
    </div>
  );
};

const Message = ({ message, onUpdate, onDelete, onGenerate }) => {
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
  
  return (
    <div className="message">
      <div className="message-header">
        <select 
          className={`role-select ${getRoleClass(message.role)}`} 
          value={message.role}
          onChange={(e) => onUpdate({ ...message, role: e.target.value })}
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
          className="content-editable" 
          contentEditable={true}
          onBlur={(e) => onUpdate({ ...message, content: e.target.innerText })}
          suppressContentEditableWarning={true}
        >
          {message.content}
        </div>
      </div>
    </div>
  );
};

export const RightSidebar = ({ chat, onAddTag, onRemoveTag, onAddTool, onDeleteTool, onGenerate }) => {
  return (
    <div className="right-sidebar">
      <div className="sidebar-section">
        <h3 className="sidebar-section-title">Tags</h3>
        <div className="tags-container">
          {(chat?.tags || []).map((tag, index) => (
            <div key={index} className="tag-item">
              <span className="tag">{tag}</span>
              <button 
                className="tag-remove" 
                onClick={() => onRemoveTag(tag)}
                title="Remove Tag"
              >
                ×
              </button>
            </div>
          ))}
          <button className="add-tag-button" onClick={() => onAddTag()}>
            + Add tag
          </button>
        </div>
      </div>

      <div className="sidebar-section">
        <h3 className="sidebar-section-title">Tools/Functions</h3>
        {(chat?.tools || []).map((tool, index) => (
          <div key={index} className="tool-item">
            <div className="tool-header">
              <span className="tool-name">{tool.name}</span>
              <div className="tool-actions">
                <button 
                  className="message-action"
                  title="Edit Tool"
                >
                  <EditIcon />
                </button>
                <button 
                  className="message-action delete-action"
                  title="Delete Tool"
                  onClick={() => onDeleteTool(tool.name)}
                >
                  <DeleteIcon />
                </button>
              </div>
            </div>
            <div className="tool-description">{tool.description || 'No description'}</div>
          </div>
        ))}
        <button className="add-tool-button" onClick={onAddTool}>
          + Add Tool
        </button>
      </div>

      <div className="sidebar-section">
        <h3 className="sidebar-section-title">Model Generation</h3>
        <select className="model-select">
          <option value="gpt-3.5-turbo">gpt-3.5-turbo</option>
          <option value="gpt-4o-mini" selected>gpt-4o-mini</option>
          <option value="mixtral-8x7B">mixtral-8x7B</option>
          <option value="llama-3-70B">llama-3-70B</option>
        </select>
        
        <div className="temperature-control">
          <span className="temp-label">Temperature:</span>
          <input
            type="range"
            min="0"
            max="1"
            step="0.1"
            className="temp-slider"
            defaultValue="0.7"
          />
        </div>
        
        <button className="generate-button" onClick={onGenerate}>
          Generate Selected
        </button>
      </div>
    </div>
  );
};

export default Layout;