import plagiated_function

# Define the file paths
input_file_path = 'output_test\cleaned_text.txt'
output_file_path = 'output_test\cleaned_text_with_paraphrased_abstract.txt'

'''
# Paraphrase the abstract in the input file and write the modified content to a new file
plagiated_function.paraphrase_abstract_in_file(input_file_path, output_file_path)

print("The Abstract was correct modified and saved:", output_file_path)
'''



'''

from transformers import pipeline

def get_title(file_path):
    with open(file_path,'r') as file:
     title = file.readline()
    
    return title

def generate_introduction(title):
# TEST THE MODEL ON THE GENERATION PART, COMPARE WITH T5-BASE
    generator = pipeline("text-generation", model="gpt2-medium", tokenizer="gpt2-medium") 
    input_text = f"Generate an introduction based on the title: '{title}'.\n\nIntroduction:"  #test to get the best prompt
    generated_text = generator(input_text, max_length=200, temperature=0.7, num_return_sequences=1, do_sample=True, early_stopping=True)[0]['generated_text']
    return generated_text

title = get_title(input_file_path)
intro = generate_introduction(title)
print(intro)
'''
plagiated_function.change_introduction(input_file_path)

