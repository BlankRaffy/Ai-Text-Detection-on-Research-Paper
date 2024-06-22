import pandas as pd
import nltk
import xml.etree.ElementTree as ET
from nltk import sent_tokenize
from transformers import pipeline
import tqdm
import os
import get_text

nltk.download('punkt')

# Initialize the model
detector = pipeline(task='text-classification', model='SJTU-CL/RoBERTa-large-ArguGPT-sent')

# Define function to predict document
def predict_doc(doc):
    sents = sent_tokenize(doc)
    res = []
    for sent in sents:
        prob = predict_one_sent(sent)
        res.append((sent, prob))
    return res

# Define function to predict single sentence
def predict_one_sent(sent):
    res = detector(sent)[0]
    org_label, prob = res['label'], res['score']
    if org_label == 'LABEL_0':
        prob = 1 - prob
    return prob

# Load the data
plagiated_file_directory = 'Test_on_multiplagiated_paper/multi_plagiated_paper'
df_abstract = pd.read_csv('Test_on_multiplagiated_paper/semantic_similarity/semantic_rank/semantic_rank_abstract.csv')
df_intro = pd.read_csv('Test_on_multiplagiated_paper/semantic_similarity/semantic_rank/semantic_rank_intro.csv')
df_conclusion = pd.read_csv('Test_on_multiplagiated_paper/semantic_similarity/semantic_rank/semantic_rank_conclusion.csv')

# Get the first element for each group with the same input_file
df_abstract_first = df_abstract.drop_duplicates(subset='input_file', keep='first')
df_intro_first = df_intro.drop_duplicates(subset='input_file', keep='first')
df_conclusion_first = df_conclusion.drop_duplicates(subset='input_file', keep='first')

# Initialize the final result DataFrame
columns = ['plagiated_file', 'abstract_sentence', 'intro_sentence', 'conclusion_sentence']
df_final_result = pd.DataFrame(columns=columns)

# Function to extract and predict sentences for a section
def process_section(plagiated_tree, score, threshold, extract_func):
    if score > threshold:
        text = extract_func(plagiated_tree)
        return predict_doc(text)
    else:
        return [('NO SIMILAR SENTENCE FOUND ON SEMANTIC CONTROL', 0)]

# Process each file
for i, (abstract_row, intro_row, conclusion_row) in tqdm.tqdm(enumerate(zip(df_abstract_first.iterrows(), df_intro_first.iterrows(), df_conclusion_first.iterrows())), total=df_abstract_first.shape[0]):
    input_file = abstract_row[1]['input_file']
    abstract_score = abstract_row[1]['abstract_semantic_score']
    intro_score = intro_row[1]['intro_semantic_score']
    conclusion_score = conclusion_row[1]['conclusion_semantic_score']
    
    plagiated_file_name = os.path.join(plagiated_file_directory, input_file)
    plagiated_tree = ET.parse(plagiated_file_name)

    df_result_abstract = process_section(plagiated_tree, abstract_score, 0.4, get_text.extract_abstract)
    df_result_intro = process_section(plagiated_tree, intro_score, 0.4, get_text.extract_intro)
    df_result_conclusion = process_section(plagiated_tree, conclusion_score, 0.4, get_text.extract_conclusion)

    new_row = {
        'plagiated_file': input_file,
        'abstract_sentence': df_result_abstract,
        'intro_sentence': df_result_intro,
        'conclusion_sentence': df_result_conclusion
    }
    df_final_result = pd.concat([df_final_result, pd.DataFrame([new_row])], ignore_index=True)

# Save the final results to a CSV file
output_path = 'Test_on_multiplagiated_paper/Ai_Detection/Ai_Detection_result_multiplagiated.csv'
df_final_result.to_csv(output_path, index=False)
