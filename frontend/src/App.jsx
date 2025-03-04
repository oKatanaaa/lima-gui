import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useParams, useNavigate } from 'react-router-dom';
import { Header, ChatList, ChatHeader, MessageArea, RightSidebar } from './components'; // Import all components from index
import './main.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainApp />} />
        <Route path="/chat/:id" element={<MainApp />} />
      </Routes>
    </Router>
  );
}

function MainApp() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [chats, setChats] = useState([]);
  const [selectedChat, setSelectedChat] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Load chats on component mount
  useEffect(() => {
    fetchChats();
  }, []);

  // Load selected chat when ID changes
  useEffect(() => {
    if (id) {
      fetchChatDetails(id);
    }
  }, [id]);

  // Fetch all chats
  const fetchChats = async () => {
    try {
      setLoading(true);
      const response = await fetch('/chats');
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      const data = await response.json();
      setChats(data);
      
      // If there's a selected ID in the URL, don't change it
      // Otherwise, select the first chat if available
      if (!id && data.length > 0) {
        navigate(`/chat/${data[0].id}`);
      }
      
      setError(null);
    } catch (err) {
      console.error('Failed to fetch chats:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Fetch chat details
  const fetchChatDetails = async (chatId) => {
    try {
      setLoading(true);
      const response = await fetch(`/chat/${chatId}`);
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      const data = await response.json();
      setSelectedChat(data);
      setError(null);
    } catch (err) {
      console.error(`Failed to fetch chat ${chatId}:`, err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Create a new chat
  const handleCreateChat = async () => {
    try {
      const response = await fetch('/chats', { method: 'POST' });
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      const newChat = await response.json();
      setChats([...chats, newChat]);
      navigate(`/chat/${newChat.id}`);
    } catch (err) {
      console.error('Failed to create chat:', err);
      setError(err.message);
    }
  };

  // Select a chat
  const handleSelectChat = (chatId) => {
    navigate(`/chat/${chatId}`);
  };

  // Update chat name
  const handleChangeName = async (newName) => {
    if (!selectedChat) return;
    
    try {
      await fetch(`/chat/${selectedChat.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...selectedChat, name: newName })
      });
      
      setSelectedChat({ ...selectedChat, name: newName });
      
      // Update the name in the chats list too
      setChats(chats.map(chat => 
        chat.id === selectedChat.id ? { ...chat, name: newName } : chat
      ));
    } catch (err) {
      console.error('Failed to update chat name:', err);
      setError(err.message);
    }
  };

  // Update chat language
  const handleChangeLanguage = async (newLanguage) => {
    if (!selectedChat) return;
    
    try {
      await fetch(`/chat/${selectedChat.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...selectedChat, language: newLanguage })
      });
      
      setSelectedChat({ ...selectedChat, language: newLanguage });
      
      // Update the language in the chats list too
      setChats(chats.map(chat => 
        chat.id === selectedChat.id ? { ...chat, language: newLanguage } : chat
      ));
    } catch (err) {
      console.error('Failed to update chat language:', err);
      setError(err.message);
    }
  };

  // Add a message
  const handleAddMessage = async (role) => {
    if (!selectedChat) return;
    
    try {
      const response = await fetch(`/chat/${selectedChat.id}/message`, {
        method: 'POST'
      });
      
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      
      const newMessage = await response.json();
      
      // Update role if different from default
      if (role && role !== 'user') {
        await fetch(`/chat/${selectedChat.id}/message/${newMessage.id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ role })
        });
        
        newMessage.role = role;
      }
      
      // Update the selected chat with the new message
      setSelectedChat({
        ...selectedChat,
        messages: [...(selectedChat.messages || []), newMessage]
      });
    } catch (err) {
      console.error('Failed to add message:', err);
      setError(err.message);
    }
  };

  // Update a message
  const handleUpdateMessage = async (messageId, updates) => {
    if (!selectedChat) return;
    
    try {
      await fetch(`/chat/${selectedChat.id}/message/${messageId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updates)
      });
      
      // Update the message in the local state
      setSelectedChat({
        ...selectedChat,
        messages: (selectedChat.messages || []).map(msg => 
          msg.id === messageId ? { ...msg, ...updates } : msg
        )
      });
    } catch (err) {
      console.error('Failed to update message:', err);
      setError(err.message);
    }
  };

  // Delete a message
  const handleDeleteMessage = async (messageId) => {
    if (!selectedChat) return;
    
    try {
      await fetch(`/chat/${selectedChat.id}/message/${messageId}`, {
        method: 'DELETE'
      });
      
      // Remove the message from the local state
      setSelectedChat({
        ...selectedChat,
        messages: (selectedChat.messages || []).filter(msg => msg.id !== messageId)
      });
    } catch (err) {
      console.error('Failed to delete message:', err);
      setError(err.message);
    }
  };

  // Generate message content
  const handleGenerateMessage = async (messageId) => {
    if (!selectedChat) return;
    
    // Mark message as generating
    setSelectedChat({
      ...selectedChat,
      messages: (selectedChat.messages || []).map(msg => 
        msg.id === messageId ? { ...msg, generating: true } : msg
      )
    });
    
    try {
      // This is a placeholder - you'll need to implement the actual API call
      // based on your backend's generation endpoint
      const response = await fetch(`/generate/${selectedChat.id}/message/${messageId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'gpt-4o-mini',
          temperature: 0.7
        })
      });
      
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      
      const result = await response.json();
      
      // Update the message with the generated content
      setSelectedChat({
        ...selectedChat,
        messages: (selectedChat.messages || []).map(msg => 
          msg.id === messageId ? { ...msg, content: result.content, generating: false } : msg
        )
      });
    } catch (err) {
      console.error('Failed to generate message:', err);
      setError(err.message);
      
      // Remove generating flag on error
      setSelectedChat({
        ...selectedChat,
        messages: (selectedChat.messages || []).map(msg => 
          msg.id === messageId ? { ...msg, generating: false } : msg
        )
      });
    }
  };

  // Add a tag
  const handleAddTag = async () => {
    if (!selectedChat) return;
    
    const newTag = prompt('Enter a tag name:');
    if (!newTag || !newTag.trim()) return;
    
    const updatedTags = [...(selectedChat.tags || []), newTag.trim()];
    
    try {
      await fetch(`/chat/${selectedChat.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tags: updatedTags })
      });
      
      setSelectedChat({ ...selectedChat, tags: updatedTags });
    } catch (err) {
      console.error('Failed to add tag:', err);
      setError(err.message);
    }
  };

  // Remove a tag
  const handleRemoveTag = async (tagToRemove) => {
    if (!selectedChat) return;
    
    const updatedTags = (selectedChat.tags || []).filter(tag => tag !== tagToRemove);
    
    try {
      await fetch(`/chat/${selectedChat.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tags: updatedTags })
      });
      
      setSelectedChat({ ...selectedChat, tags: updatedTags });
    } catch (err) {
      console.error('Failed to remove tag:', err);
      setError(err.message);
    }
  };

  // Add a tool
  const handleAddTool = async () => {
    if (!selectedChat) return;
    
    try {
      const response = await fetch(`/chat/${selectedChat.id}/tools`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: 'new_tool',
          description: 'Tool description',
          parameters: {
            type: 'object',
            properties: {},
            required: []
          }
        })
      });
      
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
      
      // Reload chat details to get updated tools
      fetchChatDetails(selectedChat.id);
    } catch (err) {
      console.error('Failed to add tool:', err);
      setError(err.message);
    }
  };

  // Delete a tool
  const handleDeleteTool = async (toolName) => {
    if (!selectedChat) return;
    
    try {
      await fetch(`/chat/${selectedChat.id}/tools/${toolName}`, {
        method: 'DELETE'
      });
      
      // Remove the tool from local state
      setSelectedChat({
        ...selectedChat,
        tools: (selectedChat.tools || []).filter(tool => tool.name !== toolName)
      });
    } catch (err) {
      console.error('Failed to delete tool:', err);
      setError(err.message);
    }
  };

  return (
    <div className="app">
      <Header /> {/* Use the new Header component */}
      
      <div className="container">
        <ChatList 
          chats={chats} 
          selectedChatId={selectedChat?.id} 
          onSelectChat={handleSelectChat}
          onCreateChat={handleCreateChat}
        />
        
        {selectedChat ? (
          <>
            <div className="main-content">
              <ChatHeader 
                chat={selectedChat}
                onChangeName={handleChangeName}
                onChangeLanguage={handleChangeLanguage}
              />
              
              <MessageArea 
                messages={selectedChat.messages || []}
                onAddMessage={handleAddMessage}
                onUpdateMessage={handleUpdateMessage}
                onDeleteMessage={handleDeleteMessage}
                onGenerateMessage={handleGenerateMessage}
              />
            </div>
            
            <RightSidebar 
              chat={selectedChat}
              onAddTag={handleAddTag}
              onRemoveTag={handleRemoveTag}
              onAddTool={handleAddTool}
              onDeleteTool={handleDeleteTool}
              onGenerate={() => alert('Please select a message to generate')}
            />
          </>
        ) : (
          <div className="main-content empty-state">
            <h2>Select a chat or create a new one</h2>
            <p>Choose an existing chat from the list or click the "New Chat" button to get started</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;