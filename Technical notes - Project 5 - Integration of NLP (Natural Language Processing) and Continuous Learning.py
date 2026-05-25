import nltk
from transformers import pipeline # 1. Setup & Pre-trained Model Loading
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
sentiment_analyzer = pipeline("sentiment-analysis") # 2. Knowledge Base (Source of Truth)
kb = {"overheating": "Clean fans and check ventilation.", "slow": "Close background apps and restart."}
def agent_logic(query):    # --- PHASE 1: PERCEIVE (NLP) ---
    tokens = nltk.word_tokenize(query)
    sentiment = sentiment_analyzer(query)[0]    # --- PHASE 2: REASON (Decision Logic) ---
    # Prioritize if user is highly frustrated (Negative Sentiment)
    if sentiment['label'] == 'NEGATIVE' and sentiment['score'] > 0.9:
        return "PRIORITY ESCALATION: Human expert required due to high frustration."
    # --- PHASE 3: ACT (Solution Generation) ---
    query_low = query.lower()
    for issue, solution in kb.items():
        if issue in query_low:
            return f"Solution: {solution}"
    return "Can you provide more details about the issue?" # Testing the Agent
print(agent_logic("My laptop is overheating!"))
print(agent_logic("THIS IS TERRIBLE, IT'S SO SLOW!!"))