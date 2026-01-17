import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    if (!input.trim()) return;

    // Add user message
    setMessages(prev => [...prev, { role: "user", text: input }]);
    setLoading(true);

    const question = input;
    setInput("");

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
      });

      // If backend returns JSON: { answer: "..." }
      const data = await res.json();
      console.log(data)  
      const answer = data || "No answer received.";

      // Add bot message
      setMessages(prev => [...prev, { role: "bot", text: answer }]);
    } catch (error) {
      console.error("API Error:", error);
      setMessages(prev => [
        ...prev,
        { role: "bot", text: "❌ Error connecting to server." }
      ]);
    }

    setLoading(false);
  }

  return (
    <div style={{ maxWidth: "500px", margin: "40px auto", fontFamily: "Arial" }}>
      <h2>🤖 RAG Chatbot</h2>

      {/* Chat Box */}
      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          height: "350px",
          overflowY: "auto",
          marginBottom: "10px",
          borderRadius: "5px"
        }}
      >
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: "8px" }}>
            <b>{msg.role === "user" ? "You" : "Bot"}:</b>{" "}
            {msg.text}
          </div>
        ))}

        {loading && <p>⏳ Bot is thinking...</p>}
      </div>

      {/* Input Form */}
      <form onSubmit={handleSubmit} style={{ display: "flex", gap: "5px" }}>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Ask something..."
          style={{ flex: 1, padding: "8px" }}
          disabled={loading}
        />
        <button type="submit" disabled={loading}>
          Send
        </button>
      </form>
    </div>
  );
}

export default App;
