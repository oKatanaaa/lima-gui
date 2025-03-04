import React from 'react';

const ChatList = ({ chats, selectedChatId, onSelectChat, onCreateChat, onDeleteChat }) => {
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
          >
            <div 
              className="chat-item-content"
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
            <button 
              className="delete-chat-button"
              onClick={(e) => {
                e.stopPropagation(); // Prevent chat selection when clicking delete
                if (window.confirm(`Are you sure you want to delete "${chat.name || 'Untitled Chat'}"?`)) {
                  onDeleteChat(chat.id);
                }
              }}
              title="Delete Chat"
            >
              <svg className="icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <polyline points="3 6 5 6 21 6"></polyline>
                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
              </svg>
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChatList;