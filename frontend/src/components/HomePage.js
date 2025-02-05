import React, { useState, useCallback } from 'react';
import axios from 'axios';
import '../assets/home_page.css';

const API_ENDPOINT = 'http://localhost:8000/api/ai/generate-code/';

const HomePage = () => {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = useCallback(async () => {
    if (!message.trim()) {
      setError('Please enter a valid message.');
      return;
    }

    setIsLoading(true);
    setError(null);
    try {
      console.log('Sending data:', { prompt: message });
      const result = await axios.post(
        API_ENDPOINT,
        { prompt: message },
        { headers: { 'Content-Type': 'application/json' } }
      );
      console.log('Server response:', result.data);
      setResponse(result.data.code);
      setMessage('');
    } catch (err) {
      console.error('Axios error:', err.response?.data || err.message);
      setError('An error occurred while processing your request.');
    } finally {
      setIsLoading(false);
    }
  }, [message]);

  const handleInputChange = (e) => {
    setMessage(e.target.value);
    setError(null);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div className="chat-container">
      <input
        type="text"
        className="chat-input"
        placeholder="Type your message..."
        value={message}
        onChange={handleInputChange}
        onKeyDown={handleKeyPress}
        disabled={isLoading}
      />

      {isLoading && <div className="loading">Loading...</div>}
      {error && <div className="error">{error}</div>}
      {response && (
        <div className="ai-response">
          <pre>{response}</pre>
        </div>
      )}
    </div>
  );
};

export default HomePage;
