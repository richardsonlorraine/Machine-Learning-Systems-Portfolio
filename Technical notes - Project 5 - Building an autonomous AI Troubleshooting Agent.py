import nltk
import spacy
from transformers import pipeline # Initial setup
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline('sentiment-analysis')
# 1. Deterministic Knowledge Base
kb = {"overheating": "Check your cooling system and clean the fans.", "slow": "Close background apps and check for malware."}
def troubleshoot_agent(query):    # --- PHASE 1: NLP PERCEPTION ---
    doc = nlp(query)
    sentiment = sentiment_analyzer(query)[0]    # --- PHASE 2: DECISION LOGIC ---
    # Prioritize if user is highly frustrated
    if sentiment['label'] == 'NEGATIVE' and sentiment['score'] > 0.95:
        print("LOG: High urgency detected.")
    query_low = query.lower()
    if "overheating" in query_low:
        return kb["overheating"]
    elif "slow" in query_low:
        return kb["slow"]
    else:
        return "Can you provide more details about the issue?" # Testing
user_query = "My laptop is overheating after the update."
print(f"Agent Response: {troubleshoot_agent(user_query)}")
