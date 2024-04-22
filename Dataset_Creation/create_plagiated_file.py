from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def paraphrase_with_gpt2(text):
    input_ids = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)
    output = model.generate(input_ids, max_length=512, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id, early_stopping=True)
    paraphrased_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print("the original_abstract:")
    print(original_abstract)
    print("the new_abstract:")
    print(paraphrased_text)
    return paraphrased_text

# Read the cleaned text from the file
input_file = "output_test/cleaned_text.txt"
with open(input_file, "r", encoding="utf-8") as file:
    cleaned_text = file.read()

# Extract the original abstract
start_index = cleaned_text.find("Abstract")
end_index = cleaned_text.find("Introduction")
original_abstract = cleaned_text[start_index:end_index].strip()

# Paraphrase the original abstract using GPT-2
paraphrased_abstract = paraphrase_with_gpt2(original_abstract)

# Replace the original abstract with the paraphrased one
modified_text = cleaned_text.replace(original_abstract, paraphrased_abstract)

# Save the modified text to a file
output_file = "output_test/modified_text_with_paraphrased_abstract.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(modified_text)

print("Modified text with paraphrased abstract saved to:", output_file)
