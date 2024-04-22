from transformers import BartForConditionalGeneration, BartTokenizer

# Load BART model and tokenizer
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

# Load text file
file_path = "output_test\cleaned_text.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Find the starting index of the abstract
abstract_start_index = text.find("Abstract")

# Find the ending index of the abstract
abstract_end_index = text.find("1 Introduction")

# Extract the abstract section
abstract = text[abstract_start_index:abstract_end_index].strip()

# Print abstract
print("Abstract:")
print(abstract)
print()

# Prompt for paraphrasing
prompt = "paraphrase it: \n"

# Combine prompt and abstract
sequence = prompt + abstract

# Tokenize input text
inputs = tokenizer(sequence, return_tensors="pt", max_length=1024, truncation=True)

# Generate paraphrased text
paraphrased_ids = model.generate(**inputs)

# Decode paraphrased text
paraphrased_abstract = tokenizer.decode(paraphrased_ids[0], skip_special_tokens=True)

# Print paraphrased abstract
print("\nParaphrased Abstract:")
print(paraphrased_abstract)
