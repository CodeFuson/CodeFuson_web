import React, {useState} from 'react';
import axios from 'axios';
import '../assets/home_page.css';

const HomePage = () => {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const handleKeyPress = async (e) => {
        if (e.key === 'Enter' && message.trim()) {
            try {
                const result = await axios.post('http://localhost:8000/api/generate-code/',
                    {prompt: message},
                    {headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}}
                );
                setResponse(result.data.code);
                setMessage('');
            } catch (error) {
                console.error('Axios hiba:', error.response?.data || error.message);
                setResponse('Hiba történt a kérés feldolgozása során');
            }
        }
    };

    return (
        <div className="chat-container">
            <input
                type="text"
                className="chat-input"
                placeholder="Type your message..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={handleKeyPress}
            />

            {/* AI válasz megjelenítése */}
            {response && (
                <div className="ai-response">
                    <pre>{response}</pre>
                </div>
            )}
        </div>
    );
};

export default HomePage;