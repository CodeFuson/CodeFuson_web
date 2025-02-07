import React, { useState } from 'react';
import '../assets/HomePage.css';

const HomePage = () => {
  const [inputText, setInputText] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!inputText.trim()) {
      alert("Empty");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/api/ai/generate-code/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: inputText }),
      });

      if (!response.ok) {
        throw new Error(`HTTP hiba! Státusz: ${response.status}`);
      }

      const data = await response.json();
      console.log("Backend:", data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="chat-container">
      <form onSubmit={handleSubmit}>
        <div className="input-wrapper">
          <input
            type="text"
            className="chat-input"
            placeholder="Írd be az üzeneted..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
          <button type="submit" className="submit-button">
            <svg className="submit-arrow" viewBox="0 0 24 24">
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"></path>
            </svg>
          </button>
        </div>
      </form>
    </div>
  );
};

export default HomePage;
