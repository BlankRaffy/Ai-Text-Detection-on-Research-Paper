import spacy

nlp = spacy.load("en_core_web_md")  # python -m spacy download en_core_web_md

import pandas as pd

def convert_to_list(string):
    if isinstance(string, str):
        return string.split(',')
    else:
        return []
    


# Carica il DataFrame dal file CSV, specificando la funzione di conversione per le colonne desiderate
df_original = pd.read_csv('Topic_Extraction/topic/original_topic.csv', converters={'abstract': convert_to_list, 'introduction': convert_to_list, 'conclusion': convert_to_list})
df_plagiated= pd.read_csv('Topic_Extraction/topic/plagiated_topic.csv', converters={'abstract': convert_to_list, 'introduction': convert_to_list, 'conclusion': convert_to_list})

origianal_abstact_tp = df_original['abstract'][0]
print(origianal_abstact_tp[0])

'''
originale_tp_abstract = ['breast cancer susceptibility',  'cancer susceptibility genes',  'susceptibility genes encode',  'normal cellular functions', 'genes encode proteins', 'breast cancer']
plagiated_tp_abstract = ['complex cellular functions',  'encode breast cancer',  'breast cancer susceptibility',  'multiple complex cellular',  'cancer susceptibility genes', 'cellular functions']

abstract_similarity = []

for ele in originale_tp_abstract:
    max_similarity = 0
    word1 = nlp(ele)
    for item in plagiated_tp_abstract:
        word2 = nlp(item)
        similarity_score = word1.similarity(word2)
        #print(f' la similarità semantica tra {word1} e {word2} è: {similarity_score}')
        if similarity_score > max_similarity:
            max_similarity=similarity_score
    abstract_similarity.append(max_similarity)

print('il massimo di similarità di ogni parola è:', sum(abstract_similarity)/len(abstract_similarity))
'''

