# mcq_generation.py

from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load T5 model and tokenizer
t5_model = T5ForConditionalGeneration.from_pretrained("t5-small")
t5_tokenizer = T5Tokenizer.from_pretrained("t5-small")

def generate_mcqs(processed_data):
    """
    Generates MCQs based on preprocessed data.
    """
    questions = []
    for sentence in processed_data:
        input_text = f"generate question: {sentence}"
        input_ids = t5_tokenizer(input_text, return_tensors="pt").input_ids
        outputs = t5_model.generate(input_ids)
        question = t5_tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Simplified distractor generation
        questions.append({
            "question": question,
            "options": [
                question, # Correct answer placeholder
                "Distractor 1", "Distractor 2", "Distractor 3"
            ]
        })
    return questions