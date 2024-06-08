import os
import xml.etree.ElementTree as ET
import get_text
from xml.dom import minidom
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
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
    max_length=400 
):
    input_ids = tokenizer(
        f'rephrase: {sentence}',
        return_tensors="pt",
        padding="longest",
        max_length=max_length,
        truncation=False,
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

def split_text(text, max_length=400):
    import re
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 > max_length:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            current_chunk += " " + sentence
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def paraphrase_text(text, max_length=400):
    chunks = split_text(text, max_length)
    paraphrased_chunks = [paraphrase(chunk) for chunk in chunks]
    return " ".join(paraphrased_chunks)

def find_passage_by_section_type(root, section_type):
    passages = root.findall(".//passage")
    for passage in passages:
        infon = passage.find(".//infon[@key='section_type']")
        if infon is not None and infon.text == section_type:
            return passage
    return None

def save_tree(abstract_file_path, intro_file_path, conclusion_file_path, output_file_path):
    # Load intro XML
    abstract_tree = ET.parse(abstract_file_path)
    intro_tree = ET.parse(intro_file_path)
    conclusion_tree = ET.parse(conclusion_file_path)
    
    abstract_text = get_text.extract_abstract(abstract_tree)
    intro_text = get_text.extract_intro(intro_tree)
    conclusion_text = get_text.extract_conclusion(conclusion_tree)

    # Create a new XML tree
    new_root = ET.Element("root")

    # TITLE
    title_passage_element = ET.SubElement(new_root, "passage")
    title_infon_element = ET.SubElement(title_passage_element, "infon", key="section_type")
    title_infon_element.text = "TITLE"
    title_text_element = ET.SubElement(title_passage_element, "text")
    title_text_element.text = get_text.get_title(abstract_tree)

    # ABSTRACT
    abstract_passage_element = ET.SubElement(new_root, "passage")
    abstract_infon_element = ET.SubElement(abstract_passage_element, "infon", key="section_type")
    abstract_infon_element.text = "ABSTRACT"
    abstract_text_element = ET.SubElement(abstract_passage_element, "text")
    paraphrase_abstract = paraphrase_text(abstract_text)
    abstract_text_element.text = paraphrase_abstract

    print(f'the len of the original abstract is : {len(abstract_text)}')
    print(f'the len of the new abstract is : {len(paraphrase_abstract)}')

    # INTRO
    intro_passage_element = ET.SubElement(new_root, "passage")
    intro_infon_element = ET.SubElement(intro_passage_element, "infon", key="section_type")
    intro_infon_element.text = "INTRO"
    intro_text_element = ET.SubElement(intro_passage_element, "text")
    paraphrase_intro = paraphrase_text(intro_text)
    intro_text_element.text = paraphrase_intro

    print(f'the len of the original intro is : {len(intro_text)}')
    print(f'the len of the new intro is : {len(paraphrase_intro)}')

    # CONCLUSION
    conclusion_passage_element = ET.SubElement(new_root, "passage")
    conclusion_infon_element = ET.SubElement(conclusion_passage_element, "infon", key="section_type")
    conclusion_infon_element.text = "CONCL"
    conclusion_text_element = ET.SubElement(conclusion_passage_element, "text")
    paraphrase_conclusion = paraphrase_text(conclusion_text)
    conclusion_text_element.text = paraphrase_conclusion

    print(f'the len of the original conclusion is : {len(conclusion_text)}')
    print(f'the len of the new conclusion is : {len(paraphrase_conclusion)}')

    # Convert tree to a string
    rough_string = ET.tostring(new_root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    output_string = reparsed.toprettyxml(indent="  ", encoding='utf-8').decode('utf-8')

    # Save the new XML tree to a file
    with open(output_file_path, "wb") as f:
        f.write(output_string.encode('utf-8'))

    return output_file_path

# Test the code
# save_tree("path_to_abstract.xml", "path_to_intro.xml", "path_to_conclusion.xml", "output.xml")
