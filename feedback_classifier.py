from transformers import pipeline

# Load pre-trained sentiment classifier (DistilBERT)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(text):
    result = classifier(text)[0]
    label = result['label'].lower()
    if label == 'positive':
        return 'positive'
    elif label == 'negative':
        return 'negative'
    else:
        return 'neutral'
