import spacy # Load the NLP engine (Pillar: Perception)
nlp = spacy.load("en_core_web_sm")
def process_query(text):
    doc = nlp(text)
    print(f"Original Text: {text}\n" + "-"*30)    # 1. Morphological & Syntactic Analysis
    for token in doc:
        print(f"Word: {token.text:10} | Lemma: {token.lemma_:10} | POS: {token.pos_}")    # 2. Semantic Analysis: Named Entity Recognition (NER)
    if doc.ents:
        print("\nNamed Entities Identified:")
        for ent in doc.ents:
            print(f"Entity: {ent.text:10} | Label: {ent.label_}") # Example Case: Identifying intent and entities
process_query("Book a flight to London for tomorrow.")