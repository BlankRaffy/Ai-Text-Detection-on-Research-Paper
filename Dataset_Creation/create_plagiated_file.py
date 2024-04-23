import plagiated_function

# Define the file paths
input_file_path = 'output_test\cleaned_text.txt'
output_file_path = 'output_test\cleaned_text_with_paraphrased_abstract.txt'

# Paraphrase the abstract in the input file and write the modified content to a new file
#plagiated_function.paraphrase_abstract_in_file(input_file_path, output_file_path)

#print("The Abstract was correct modified and saved:", output_file_path)

with open(input_file_path,'r') as file:
    content = file.readline()

#generation of the first part of the introduction
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Step 1: Read the first line of the file
def read_first_line(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
    return first_line

# Step 2: Use a specified model to generate introduction
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
title='Lessons learned from the deployment of a high-interaction honeypot'
output = generator(f"Please generate an introduction for a scientific article titled: {title},", max_length=150, num_return_sequences=1)
print(output[0])