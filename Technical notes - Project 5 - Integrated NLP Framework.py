import nltk
from nltk.tokenize import word_tokenize # Setup
nltk.download(['punkt_tab', 'averaged_perceptron_tagger_eng'])
text = "My laptop is overheating after the firmware update." # Step 1: Tokenization (Morphology)
tokens = word_tokenize(text.lower()) # Step 2: POS Tagging (Syntax)
tagged = nltk.pos_tag(tokens)
print(f"POS Tags: {tagged[:3]}") # e.g., [('my', 'PRP$'), ('laptop', 'NN')]

import spacy # Step 3: Named Entity Recognition (Semantics)
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
print("Entities Found:")
for ent in doc.ents:
    print(f"- {ent.text} ({ent.label_})") # Extracts 'laptop' or 'update'
    
from transformers import pipeline # Step 4: Sentiment Analysis (Pragmatics/Intent)
sentiment_logic = pipeline('sentiment-analysis')
sentiment = sentiment_logic(text) # Step 5: Summarization (Discourse)
summarizer = pipeline('summarization') # For short text, this provides a rephrased 'Core Issue'
summary = summarizer(text, max_length=15, min_length=5, do_sample=False)
print(f"User Sentiment: {sentiment[0]['label']}")
print(f"Issue Summary: {summary[0]['summary_text']}")
