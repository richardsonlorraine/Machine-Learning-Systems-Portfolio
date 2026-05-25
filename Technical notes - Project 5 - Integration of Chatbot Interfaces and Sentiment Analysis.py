// Step 1: Handle User Input (Pillar: UI/UX)
function sendMessage() {const input = document.getElementById("userInput");
    const userText = input.value.trim();
    if (!userText) return;
    appendMessage("You", userText, "user-style");
    input.value = "";
    // Step 2: Simulated Latency (Pillar: Conversational Design)
    setTimeout(() => {const botResponse = getBotResponse(userText);
        appendMessage("Chatbot", botResponse, "bot-style");}, 1000);}
// Step 3: Knowledge Retrieval Logic (Pillar: NLP)
function getBotResponse(text) {const query = text.toLowerCase();
    const knowledgeBase = {"hello": "Hi there! How can I assist you today?", "status": "I can check your order status if you provide an ID.", "name": "I am the Lighthouse Troubleshooting Agent."};
    // Fallback logic for unrecognized intent
    return knowledgeBase[query] || "I'm sorry, I don't recognize that. Try a quick-reply below!";}
    
# Simulated Sentiment Scoring (Pillar: Analysis)
def analyze_sentiment(text):    # Scale: -1.0 (Very Negative) to 1.0 (Very Positive)
    score = model.predict_polarity(text) 
    if score > 0.5:
        return "PROMOTER: Send discount code."
    elif score < -0.5:
        return "DETRACTOR: Escalate to human manager immediately."
    else:
        return "NEUTRAL: Log for market research."