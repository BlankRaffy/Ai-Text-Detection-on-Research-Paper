import pandas as pd
import nltk
import pandas as pd
import xml.etree.ElementTree as ET
import get_text
import csv
from nltk import sent_tokenize
from transformers import pipeline
import tqdm
import os

nltk.download('punkt')

detector = pipeline(task='text-classification', model='SJTU-CL/RoBERTa-large-ArguGPT-sent')

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

    
    
    '''
    df.to_csv('result.csv')
    
    overall_score = df.score.mean()
    if overall_score <= 0.5:
        overall_label = 'Human'
    else:
        overall_label = 'Machine'
    sum_str = f'The essay is probably written by {overall_label}. The probability of being generated by AI is {overall_score}'
    '''
    return res

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

# Example usage
#non abbiamo ancora impostato la soglia per andare a far il confronto
columns=['plagiated_file','abstract_sentence','intro_sentence','conclusion_sentence']
df_final_result = pd.DataFrame(columns= columns)


plagiated_file_directory ='Test_on_more_multiplagiated_paper\multi_plagiated_paper'


for ele in tqdm.tqdm(os.listdir(plagiated_file_directory)):
    plagiated_file_name= plagiated_file_directory+'/'+ele
    print(plagiated_file_name)
    plagiated_tree = ET.parse(plagiated_file_name)

    #ABSTRACT 
    abstract_text = get_text.extract_abstract(plagiated_tree)
    df_result_abstract = predict_doc(abstract_text)
    
 
    intro_text = get_text.extract_intro(plagiated_tree) 
    df_result_intro = predict_doc(intro_text)




    conclusion_text = get_text.extract_conclusion(plagiated_tree)
    df_result_conclusion = predict_doc(conclusion_text)

    new_row = {'plagiated_file':ele,'abstract_sentence':df_result_abstract,'intro_sentence':df_result_intro,'conclusion_sentence':df_result_conclusion} 
    df_final_result = pd.concat([df_final_result, pd.DataFrame([new_row])], ignore_index=True)

df_final_result.to_csv('Test_on_more_multiplagiated_paper/TEST_Ai_Detection_result.csv',index=False)
#NOTE stiamo salvando per ogni file un lista delle frasi di ogni parte con il relativo punteggio e label, durante la creazione del csv questi dataframe è
#come se venissero persi, si devono riconvertire quando si carica il df