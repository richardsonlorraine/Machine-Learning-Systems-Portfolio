<div id="chat-container">
    <div id="messages"></div>
    <div class="quick-replies">
        <button onclick="quickReply('Hello')">Hello</button>
        <button onclick="quickReply('Status')">Check Status</button>
    </div>
    <input type="text" id="userInput" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>
</div>

const responses = {"hello": "Hi! How can I help you today?", "status": "Your order is currently out for delivery.", "goodbye": "Goodbye! Have a great day!"};
function sendMessage() {const input = document.getElementById("userInput");
    const userMessage = input.value.trim().toLowerCase();
    if (!userMessage) return;
    displayMessage("You", userMessage);
    input.value = "";
    // Simulate "Bot is typing..." and network delay
    setTimeout(() => {const botReply = responses[userMessage] || "I'm not sure about that. Could you try rephrasing?";
        displayMessage("Chatbot", botReply);}, 1000);}
function displayMessage(sender, text) {const msgDiv = document.createElement("div");
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
    document.getElementById("messages").appendChild(msgDiv);}
function quickReply(text) {document.getElementById("userInput").value = text;
    sendMessage();}