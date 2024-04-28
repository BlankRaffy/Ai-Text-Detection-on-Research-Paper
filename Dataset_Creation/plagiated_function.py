import xml.etree.ElementTree as ET
import os

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM #import neeeded for paraphrase
from transformers import pipeline
import copy

device = "cuda" 

tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base").to(device)

def paraphrase(
    sentence,
    num_beams=5,
    num_beam_groups=5,
    num_return_sequences=1,
    repetition_penalty=5.0,
    diversity_penalty=10.0,
    no_repeat_ngram_size=2,
    temperature=0.7,
    max_length=400  # Increase max_length to accommodate longer outputs
):
    input_ids = tokenizer(
        f'rephrase: {sentence}',
        return_tensors="pt",
        padding="longest",
        max_length=max_length,
        truncation=True,
    ).input_ids.to(device)
    
    outputs = model.generate(
        input_ids,
        temperature=temperature,
        repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=no_repeat_ngram_size,
        num_beams=num_beams,
        num_beam_groups=num_beam_groups,
        max_length=max_length,
        diversity_penalty=diversity_penalty
    )

    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return res[0]


# The following function can be adapatate to any type of file
# Just need to access and overwrite the element
def generate_introduction(title):
# TEST THE MODEL ON THE GENERATION PART, COMPARE WITH T5-BASE
    generator = pipeline("text-generation", model="gpt2-medium", tokenizer="gpt2-medium") 
    input_text = f"Generate an introduction for a medical reseach titeled: '{title}'.\n\nIntroduction:"  #test to get the best prompt
    generated_text = generator(input_text, max_length=200, temperature=0.6, num_return_sequences=1, do_sample=True, early_stopping=True)[0]['generated_text']
    intro_text = generated_text.split('\n\nIntroduction:')[-1].strip()
    return intro_text


def change_abstract(tree):
    
    root = tree.getroot()
    
    # Trova tutti gli elementi 'passage' nell'albero XML 
    passages = root.findall('.//passage')
    
    # Itera su ciascun elemento 'passage'
    for passage in passages:
        # Trova l'elemento 'infon' con attributo 'section_type' uguale a 'ABSTRACT'
        section_type = passage.find(".//infon[@key='section_type']")
        
        if section_type is not None and section_type.text == 'ABSTRACT':
            # Trova l'elemento 'text' all'interno del 'passage' (abstract)
            abstract_element = passage.find('.//text')
            
            if abstract_element is not None:
                abstract_text = passage.find('.//text').text
                passage.find('.//text').text = paraphrase(abstract_text)
                ##print(passage.find('.//text').text+"\n\n")
    
    # Restituisci l'albero XML copiato e modificato
    return tree

def change_intro(tree):
    root = tree.getroot()
    generated = True #boolean to to modify the first element of the introduction
    # Trova tutti gli elementi 'passage' nell'albero XML 
    passages = root.findall('.//passage')
    
    # Itera su ciascun elemento 'passage'
    for passage in passages:
        # Trova l'elemento 'infon' con attributo 'section_type' uguale a 'ABSTRACT'
        section_type = passage.find(".//infon[@key='section_type']")
        
        
        if section_type is not None and section_type.text == 'TITLE':
            # Trova l'elemento 'text' all'interno del 'passage' (abstract)
            title_element = passage.find('.//text')
            introduction_first = generate_introduction(title_element.text)
        
        if section_type is not None and section_type.text == 'INTRO':
            if passage.find('.//text').text != 'Introduction':
                #Adding the generated introduction based on the title
                if generated:
                    passage.find('.//text').text = introduction_first
                    #print(introduction_first +'\n\n')
                    generated = False
                #rephrase the other part of the introduction
                else:
                    text_to_rephrase = passage.find('.//text').text

                    ##print(f"TESTO DA RIFRASERE :\n\n {text_to_rephrase}")
                    ##print(f"TESTO RIFRASATO: \n\n {paraphrase(text_to_rephrase)}")
                    passage.find('.//text').text = paraphrase(text_to_rephrase)
                    #print(passage.find('.//text').text +'\n\n')
                
            

    return tree

def change_conclusion(tree):
    root = tree.getroot()
    generated = True #boolean to to modify the first element of the introduction
    # Trova tutti gli elementi 'passage' nell'albero XML 
    passages = root.findall('.//passage')
    
    # Itera su ciascun elemento 'passage'
    for passage in passages:
        # Trova l'elemento 'infon' con attributo 'section_type' uguale a 'CONCL'
        section_type = passage.find(".//infon[@key='section_type']")
        
        if section_type is not None and section_type.text == 'CONCL':
            if passage.find('.//text').text != 'Conclusion':
                text_to_rephrase = passage.find('.//text').text
                passage.find('.//text').text = paraphrase(text_to_rephrase)
                #print(passage.find('.//text').text + '\n\n')
    return tree




def save_tree(file_path,tree):
    file_name_no_ext= os.path.splitext(os.path.basename(file_path))[0]
    destination_folder = 'Dataset/plagiated_paper'+'/'

    output_path = destination_folder+file_name_no_ext+'_plagiated.xml'
    tree.write(output_path)