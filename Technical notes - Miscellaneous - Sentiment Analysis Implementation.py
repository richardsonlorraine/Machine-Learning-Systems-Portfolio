# Install dependencies
# !pip install torch transformers tokenizers
from transformers import pipeline # Initialize the Neural Pipeline
# Uses DistilBERT fine-tuned on the SST-2 dataset
analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print("Neural Pipeline Initialized.")
# Processing complex, multi-line feedback
reviews = ["I love this product! It is amazing.", "The setup was a bit confusing, but the performance is incredible. Extremely satisfied!", "The service was terrible and I am very disappointed."]
def run_sentiment_audit(text_list):
    for text in text_list:        # Neural Inference
        result = analyzer(text)[0]
        label = result['label']
        confidence = result['score']
        print(f"Review: {text[:50]}...")
        print(f"Result: {label} ({confidence:.2%})\n")
run_sentiment_audit(reviews)