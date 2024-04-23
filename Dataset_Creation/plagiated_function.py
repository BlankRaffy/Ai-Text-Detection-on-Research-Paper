from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

device = "cuda" 

tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base").to(device)

def paraphrase(
    question,
    num_beams=5,
    num_beam_groups=5,
    num_return_sequences=1,
    repetition_penalty=10.0,
    diversity_penalty=3.0,
    no_repeat_ngram_size=2,
    temperature=0.7,
    max_length=512
):
    input_ids = tokenizer(
        f'paraphrase: {question}',
        return_tensors="pt", padding="longest",
        max_length=max_length,
        truncation=True,
    ).input_ids.to(device)
    
    outputs = model.generate(
        input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
        num_beams=num_beams, num_beam_groups=num_beam_groups,
        max_length=max_length, diversity_penalty=diversity_penalty
    )

    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return res[0]


#the function find and rephrase the abstract
def paraphrase_abstract_in_file(input_file_path, output_file_path):
    # Read text from the input file
    with open(input_file_path, 'r') as file:
        content = file.readlines()
    
    # Find the indices of lines containing 'Abstract' and '1. Introduction'
    abstract_start_index = -1
    introduction_index = -1
    for i, line in enumerate(content):
        if line.strip().lower().startswith("abstract"):
            abstract_start_index = i
        elif line.strip().lower().startswith("1 introduction") or line.strip().lower().startswith("1. introduction"):
            introduction_index = i
            break
    
    # If 'Abstract' and '1. Introduction' are found, paraphrase the abstract
    if abstract_start_index != -1 and introduction_index != -1:
        abstract = ''.join(content[abstract_start_index:introduction_index])
        paraphrased_abstract = paraphrase(abstract)
        paraphrased_abstract_lines = paraphrased_abstract.split('\n')
        # Insert the paraphrased abstract into the content
        content[abstract_start_index] = f"Abstract\n{paraphrased_abstract_lines[0]}\n"
        content[abstract_start_index+1:introduction_index] = paraphrased_abstract_lines[1:]
        # Add a blank line after the end of the abstract
        content.insert(introduction_index, '\n')
    else:
        print("Error: 'Abstract' or '1. Introduction' not found in the input file.")
        return
    
    # Write the modified content to the output file
    with open(output_file_path, 'w') as file:
        file.writelines(content)


def change_introduction(input_file_path):
    # Read text from the input file
    with open(input_file_path, 'r') as file:
        content = file.readlines()
    
    # Find the indices of lines containing '1. Introduction' and 'in this paper'
    introduction_start_index = -1
    introduction_end_index = -1
    for i, line in enumerate(content):
        if line.strip().lower().startswith("1. introduction"):
            introduction_start_index = i
        elif "in this paper" in line.lower():
            introduction_end_index = i
            break

    
    # If both start and end indices are found, extract the introduction
    if introduction_start_index != -1 and introduction_end_index != -1:
        introduction_lines = content[introduction_start_index:introduction_end_index]
        # Join all lines
        introduction = ''.join(introduction_lines)
        
        # Extract words from the line containing 'in this paper' before the phrase
        words_before_phrase = line.split(".")[0].strip()+'.'
        introduction = introduction + words_before_phrase
        print(introduction)
        
        # Prepend the words to the introduction
        
        #print(introduction)

