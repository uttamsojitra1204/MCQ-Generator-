import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import pipeline

# Ensure necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the language model (you can replace 'gpt-2' with your chosen model)
model = pipeline("text-generation", model="gpt-2")  # Example using GPT-2

# Pre-processing function
def preprocess_chat_data(chat_messages):
    stop_words = set(stopwords.words('english'))
    processed_messages = []
    for message in chat_messages:
        tokens = word_tokenize(message.lower())
        filtered_message = [word for word in tokens if word not in stop_words]
        processed_messages.append(" ".join(filtered_message))
    return processed_messages

# Function to generate MCQs
def generate_mcqs(chat_messages):
    prompt = f"Generate 3-5 MCQs based on the following messages: {chat_messages}"
    mcqs = model(prompt, max_length=150)[0]['generated_text']
    return mcqs.strip()

# Function to generate article with word count check
def generate_article_with_constraints(chat_messages):
    prompt = f"Summarize the following messages into an article between 200-300 words: {chat_messages}"
    article = model(prompt, max_length=300)[0]['generated_text']

    word_count = len(article.split())
    if word_count < 200 or word_count > 300:
        return generate_article_with_constraints(chat_messages)  # Recursive call for adjustment

    return article.strip()

# Example chat history
chat_history = [
    "What is the impact of AI on education?",
    "AI can personalize learning experiences for students.",
    "It can help in grading assignments faster.",
    "Some fear it may replace teachers.",
    "What do you think about AI tutors?",
]

# Process chat history
processed_history = preprocess_chat_data(chat_history)

# Generate outputs
mcq_output = generate_mcqs(processed_history)
article_output = generate_article_with_constraints(processed_history)

# Print outputs
print("MCQs Output:")
print(mcq_output)
print("\nArticle Output:")
print(article_output)
