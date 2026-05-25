from textblob import TextBlob
text = "I love this new phone! It is amazing."
blob = TextBlob(text) # Polarity ranges from -1 (Neg) to +1 (Pos)
# Subjectivity ranges from 0 (Fact) to 1 (Opinion)
print(f"Polarity: {blob.sentiment.polarity}, Subjectivity: {blob.sentiment.subjectivity}")

from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
text = "The service was terrible! I'm so disappointed :("
scores = sia.polarity_scores(text) # The 'compound' score is the overall sentiment metric
print(f"Compound Score: {scores['compound']}") # Output: ~ -0.52

from transformers import pipeline # Loads a pretrained DistilBERT model
analyzer = pipeline("sentiment-analysis")
result = analyzer("It's okay, not great but not bad either.")
print(result) # Output: [{'label': 'POSITIVE', 'score': 0.85}]