# main.py

from preprocessing import preprocess_chat, extract_entities
from mcq_generation import generate_mcqs
from article_generation import generate_article

# Example chat history
chat_history = [
    "Can you explain supervised learning?",
    "Supervised learning is a type of machine learning where a model is trained on labeled data.",
    "What’s the difference between supervised and unsupervised learning?",
    "In unsupervised learning, the model works with unlabeled data, finding patterns without guidance.",
    "Could you give examples?",
    "Sure! Classification is a supervised learning task, and clustering is often unsupervised."
]

# Preprocess chat data
processed_data = preprocess_chat(chat_history)

# Generate MCQs
mcqs = generate_mcqs(processed_data)
print("MCQs Generated:")
for i, mcq in enumerate(mcqs, 1):
    print(f"\nQuestion {i}: {mcq['question']}")
    for option in mcq["options"]:
        print(f"- {option}")

# Generate a summarized article
chat_summary = " ".join(processed_data)
article = generate_article(chat_summary)
print("\nGenerated Article:")
print(article)

# import tkinter as tk
# from tkinter import messagebox
# from transformers import pipeline

# # Function to generate MCQs or Article
# def generate_output():
#     chat_history = text_area.get("1.0", tk.END).strip()
#     option = output_option.get()

#     if not chat_history:
#         messagebox.showwarning("Input Error", "Please enter chat history.")
#         return

#     # Load the transformer model for text generation
#     generator = pipeline("text2text-generation", model="your-model-name")

#     if option == "MCQs":
#         # Generating MCQs
#         output = generator(f"Generate 3 MCQs with answers from the following chat history: {chat_history}")
#     else:
#         # Generating an article
#         output = generator(f"Generate an article summarizing the following chat history: {chat_history}")

#     output_text.delete("1.0", tk.END)
#     output_text.insert(tk.END, output[0]['generated_text'])

# # Setting up the GUI window
# root = tk.Tk()
# root.title("Chat History MCQ/Article Generator")
# root.geometry("600x400")

# # Input Frame
# frame_input = tk.Frame(root)
# frame_input.pack(pady=10)

# label = tk.Label(frame_input, text="Enter Chat History:")
# label.pack()

# text_area = tk.Text(frame_input, height=10, width=50)
# text_area.pack()

# # Output Options
# output_option = tk.StringVar(value="MCQs")
# radio_mcq = tk.Radiobutton(root, text="Generate MCQs", variable=output_option, value="MCQs")
# radio_article = tk.Radiobutton(root, text="Generate Article", variable=output_option, value="Article")

# radio_mcq.pack()
# radio_article.pack()

# # Generate Button
# generate_button = tk.Button(root, text="Generate", command=generate_output)
# generate_button.pack(pady=10)

# # Output Frame
# frame_output = tk.Frame(root)
# frame_output.pack(pady=10)

# label_output = tk.Label(frame_output, text="Output:")
# label_output.pack()

# output_text = tk.Text(frame_output, height=10, width=50)
# output_text.pack()

# # Run the GUI
# root.mainloop()