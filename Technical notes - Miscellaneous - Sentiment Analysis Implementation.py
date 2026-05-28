import nltk
# Ensure required lexical corpora are available locally
nltk.download('punkt', quiet=True)
nltk.download('vader_lexicon', quiet=True)

from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

# Always lock down your specific model variant to guarantee deterministic outputs
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
