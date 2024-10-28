# article_generation.py

from transformers import BartForConditionalGeneration, BartTokenizer

# Load BART model and tokenizer
bart_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
bart_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

def generate_article(chat_summary):
    """
    Generates an article from the summarized chat data.
    """
    input_ids = bart_tokenizer(chat_summary, return_tensors="pt").input_ids
    summary_ids = bart_model.generate(input_ids, max_length=200, min_length=100, length_penalty=2.0)
    article = bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return article