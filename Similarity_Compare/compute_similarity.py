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

original_abstact_tp = df_original['abstract'][1]
plagiated_abstract_tp = df_plagiated['abstract'][1]
print(original_abstact_tp)
print(plagiated_abstract_tp)

original_intro_tp = df_original['introduction'][1]
plagiated_intro_tp = df_plagiated['introduction'][1]
print(original_intro_tp)
print(plagiated_intro_tp)

original_conclusion_tp = df_original['conclusion'][1]
plagiated_conclusion_tp = df_plagiated['conclusion'][1]
print(original_conclusion_tp)
print(plagiated_conclusion_tp)


abstract_similarity = []
intro_similarity = []
conclusion_similarity = []


for kw in plagiated_abstract_tp:
    max_similarity = 0
    kw1 = nlp(kw)
    for kw in original_abstact_tp:
        kw2 = nlp(kw)
        similarity_score = kw1.similarity(kw2)
        #print(f' la similarità semantica tra {word1} e {word2} è: {similarity_score}')
        if similarity_score > max_similarity:
            max_similarity=similarity_score
    abstract_similarity.append(max_similarity)

print('il massimo di similarità di ogni parola è:', sum(abstract_similarity)/len(abstract_similarity))


