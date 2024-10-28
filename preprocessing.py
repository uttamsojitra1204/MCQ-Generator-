# preprocessing.py

import nltk
from nltk.corpus import stopwords
from transformers import pipeline

# Load stopwords (download if not already available)
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def preprocess_chat(chat_history):
    """
    Preprocesses chat data by removing stop words and performing basic cleaning.
    """
    processed_data = []
    for message in chat_history:
        tokens = nltk.word_tokenize(message)
        filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
        processed_data.append(" ".join(filtered_tokens))
    return processed_data

def extract_entities(chat_data):
    """
    Extracts named entities using a NER pipeline.
    """
    ner = pipeline("ner", grouped_entities=True)
    entities = []
    for sentence in chat_data:
        entities.extend(ner(sentence))
    return entities