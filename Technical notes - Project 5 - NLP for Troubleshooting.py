import spacy # Load a pre-trained NLP model
nlp = spacy.load("en_core_web_sm")
def process_ticket(text):
    doc = nlp(text)  # 1. Sentiment Analysis (Basic Logic)
    # In a real scenario, use doc._.blob.sentiment or a specialized model
    print(f"Processing Issue: '{text}'") # 2. Information Extraction (NER/Pattern Matching)
    found_entities = []
    for token in doc: # Simulate identifying an error code (often alphanumeric/uppercase)
        if token.text.isupper() and any(char.isdigit() for char in token.text):
            found_entities.append(f"ERROR_CODE: {token.text}") # 3. Root Word Extraction (Lemmatization)
        if token.pos_ == "VERB":
            print(f"Action detected: {token.lemma_}")
    return found_entities # Example Test Case
user_input = "My laptop keeps CRASHING whenever I see error ERR_99_SYS."
entities = process_ticket(user_input)
print(f"Extracted Data: {entities}")