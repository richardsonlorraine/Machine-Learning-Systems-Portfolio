import spacy
import re

nlp = spacy.load("en_core_web_sm")

def process_ticket(text):
    doc = nlp(text)
    print(f"Processing Issue: '{text}'")
    found_entities = []
    
    # Robust alphanumeric error pattern (matches ERR_99, err99, 500-SYS, etc.)
    error_pattern = re.compile(r'\b[A-Za-z]*_?\d+_\s*[A-Za-z]*|\b\d{3}\b|\bERR_[0-9]+_[A-Z]+\b', re.IGNORECASE)
    
    # Extract structural regular regex items
    matches = error_pattern.findall(text)
    for match in matches:
        found_entities.append(f"ERROR_CODE: {match.upper().strip()}")
        
    # Associate actions
    actions = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    if actions:
        print(f"Detected Actions: {', '.join(actions)}")
        
    return found_entities

user_input = "My laptop keeps crashing whenever I see error err_99_sys or code 500."
print(f"Extracted Data: {process_ticket(user_input)}")
