import nltk
import spacy
from transformers import pipeline

# 1. Ensure NLTK models are downloaded silently before text manipulation
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

# 2. Safety wrapper to verify spaCy language pack availability
try:
    nlp_spacy = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp_spacy = spacy.load("en_core_web_sm")

# 3. Explicitly declare model architectures to maintain consistent intent classification
sentiment_task = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
