import xml.etree.ElementTree as ET
import os

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


def change_abstract (file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    passages = root.findall('.//passage')
    for passage in passages:
        text = passage.find(".//infon[@key='section_type']")
        if(text.text=='ABSTRACT'):
            abstract = passage.find('.//text').text
            paraphrased_abstract = paraphrase(abstract)
            print('il testo originale \n',abstract)
            print('il testo falso \n', paraphrased_abstract)       
    #return tree

def save_tree(file_path,tree):
    file_name_no_ext= os.path.splitext(os.path.basename(file_path))[0]

    output_path = 'output_test/' + file_name_no_ext+'_plagiated.xml'
    tree.write(output_path)