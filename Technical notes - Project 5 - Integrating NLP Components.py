import nltk
import spacy
from nltk.tokenize import word_tokenize
from transformers import pipeline # 1. Initialization & Setup # nltk.download(['punkt', 'averaged_perceptron_tagger'])
nlp_spacy = spacy.load("en_core_web_sm")
sentiment_task = pipeline("sentiment-analysis")
query = "My Cisco router is overheating after the firmware update!" # 2. Preprocessing & Syntactic Analysis (NLTK)
tokens = word_tokenize(query)
pos_tags = nltk.pos_tag(tokens)
print(f"POS Tags: {pos_tags[:3]}...") # [('My', 'PRP$'), ('Cisco', 'NNP'), ('router', 'NN')] # 3. Semantic Grounding / NER (spaCy)
doc = nlp_spacy(query)
entities = [(ent.text, ent.label_) for ent in doc.ents]
print(f"Entities Found: {entities}") # [('Cisco', 'ORG')] # 4. Pragmatic Analysis (Transformers)
sentiment = sentiment_task(query)
print(f"User Sentiment: {sentiment}") # [{'label': 'NEGATIVE', 'score': 0.98}]