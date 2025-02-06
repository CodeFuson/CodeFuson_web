import React, { useState } from 'react';

const HomePage = () => {
    const [inputText, setInputText] = useState("");

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch("http://localhost:8000/api/ai/generate-code/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",  // Fontos a JSON formátumhoz!
                },
                body: JSON.stringify({ prompt: inputText }),  // Küldött JSON objektum
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log("Backend válasza:", data);
        } catch (error) {
            console.error("Hiba történt:", error);
        }
    };

    return (
        <div className="chat-container">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    className="chat-input"
                    placeholder="Type your message..."
                    value={inputText}
                    onChange={(e) => setInputText(e.target.value)}
                />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default HomePage;
