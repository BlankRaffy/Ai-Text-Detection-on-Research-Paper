from transformers import BartForConditionalGeneration, BartTokenizer

# Load BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

# Original text
original_text = """Apart from counting words and characters, our online editor can help you to improve word choice and writing style, and, optionally, help you to detect grammar mistakes and plagiarism. To check word count, simply place your cursor into the text box above and start typing. You'll see the number of characters and words increase or decrease as you type, delete, and edit them. You can also copy and paste text from another program over into the online editor above.
"""

# Prompt for paraphrasing
prompt = "paraphrase: "

# Combine prompt and original text
sequence = prompt + original_text

# Tokenize input text
inputs = tokenizer(sequence, return_tensors="pt", max_length=1024, truncation=True)

# Generate paraphrased text
paraphrased_ids = model.generate(**inputs)

# Decode paraphrased text
paraphrased_text = tokenizer.decode(paraphrased_ids[0], skip_special_tokens=True)

# Print paraphrased text
print(paraphrased_text)
