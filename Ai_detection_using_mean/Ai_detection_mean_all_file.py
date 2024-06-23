#abbiamo un problema con la compatibilità delle varie librerie
import nltk
import pandas as pd
from nltk import sent_tokenize
from transformers import pipeline
import os
import xml.etree.ElementTree as ET
import get_text
import tqdm

nltk.download('punkt')

detector = pipeline(task='text-classification', model='SJTU-CL/RoBERTa-large-ArguGPT-sent')
columns=['input_file','abstract_probability','intro_probability','conclusion_probability']
df_result =pd.DataFrame(columns=columns)

def predict_doc(doc):
    sents = sent_tokenize(doc)
    data = {'sentence': [], 'label': [], 'score': []}
    res = []
    for sent in sents:
        prob = predict_one_sent(sent)

        data['sentence'].append(sent)
        data['score'].append(round(prob, 4))
        if prob <= 0.5:
            data['label'].append('Human')
        else:
            data['label'].append('Machine')

        res.append((sent, prob))

    df = pd.DataFrame(data)
    #df.to_csv('result.csv')
    overall_score = df.score.mean()
    if overall_score <= 0.5:
        overall_label = 'Human'
    else:
        overall_label = 'Machine'
    sum_str = f'{overall_score}'

    return sum_str
    #res, df, 'result.csv'


def predict_one_sent(sent):
    '''
    convert to prob 
    LABEL_1, 0.66 -> 0.66
    LABEL_0, 0.66 -> 0.34
    '''
    res = detector(sent)[0]
    org_label, prob = res['label'], res['score']
    if org_label == 'LABEL_0':
        prob = 1 - prob
    return prob

for ele in tqdm.tqdm(os.listdir('Test_on_multiplagiated_paper/multi_plagiated_paper')):
    original_file_name= 'Test_on_multiplagiated_paper/multi_plagiated_paper'+'/'+ele
    original_tree = ET.parse(original_file_name)

    abstract_text = get_text.extract_abstract(original_tree)
    result_abstract = predict_doc(abstract_text)
    #print(result_abstract)

    intro_text = get_text.extract_intro(original_tree)
    result_intro = predict_doc(intro_text)
    #print(result_intro)

    conclusion_text = get_text.extract_conclusion(original_tree)
    result_conclusion = predict_doc(conclusion_text)
    #print(result_conclusion)
    new_row = {'input_file':ele,'abstract_probability':result_abstract,'intro_probability':result_intro,'conclusion_probability':result_conclusion}
    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)
    

csv_filename='Ai_detection_using_mean/ai_detection_mean_for_part.csv'
df_result.to_csv('Ai_detection_using_mean/ai_detection_mean_for_part_multiplagiated.csv',index=None)

print(f"CSV file '{csv_filename}' containing the result has been saved.")
