import spacy
import tqdm

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

#original_abstact_tp = df_original['abstract'][1]
plagiated_abstract_tp = df_plagiated['abstract'][6]
#print(original_abstact_tp)
#print(plagiated_abstract_tp)

#original_intro_tp = df_original['introduction'][1]
plagiated_intro_tp = df_plagiated['introduction'][6]
#print(original_intro_tp)
#print(plagiated_intro_tp)

#original_conclusion_tp = df_original['conclusion'][1]
plagiated_conclusion_tp = df_plagiated['conclusion'][6]
#print(original_conclusion_tp)
#print(plagiated_conclusion_tp)
columns = ['file','results']
df_result = pd.DataFrame(columns= columns)

for i in tqdm.tqdm(range(len(df_original))):
    original_abstact_tp = df_original['abstract'][i]
    original_intro_tp = df_original['introduction'][i]
    original_conclusion_tp = df_original['conclusion'][i]


    abstract_similarity = []
    intro_similarity = []
    conclusion_similarity = []
    verdetto = 0

    for kw in plagiated_abstract_tp:
        max_similarity = 0
        kw1 = nlp(kw)
        for kw in original_abstact_tp:
            kw2 = nlp(kw)
            similarity_score = kw1.similarity(kw2)
            #print(f' la similarità semantica tra {kw1} e {kw2} è: {similarity_score}')
            if similarity_score > max_similarity:
                max_similarity=similarity_score
        abstract_similarity.append(max_similarity)

    if sum(abstract_similarity)/len(abstract_similarity) > 0.7:
        verdetto= verdetto+1
    #print('lo score della similarità per ABSTRACT è:', sum(abstract_similarity)/len(abstract_similarity))


    for kw in plagiated_intro_tp:
        max_similarity = 0
        kw1 = nlp(kw)
        for kw in original_intro_tp:
            w2 = nlp(kw)
            similarity_score = kw1.similarity(kw2)
            #print(f' la similarità semantica tra {word1} e {word2} è: {similarity_score}')
            if similarity_score > max_similarity:
                max_similarity=similarity_score
        intro_similarity.append(max_similarity)
    if sum(intro_similarity)/len(intro_similarity) > 0.5:
        verdetto= verdetto+1
    #print('lo score della similarità per INTRODUCIOTN è:', sum(intro_similarity)/len(intro_similarity))

    for kw in plagiated_conclusion_tp:
        max_similarity = 0
        kw1 = nlp(kw)
        for kw in original_conclusion_tp:
            kw2 = nlp(kw)
            similarity_score = kw1.similarity(kw2)
            #print(f' la similarità semantica tra {word1} e {word2} è: {similarity_score}')
            if similarity_score > max_similarity:
                max_similarity=similarity_score
        conclusion_similarity.append(max_similarity)

    if sum(conclusion_similarity)/len(conclusion_similarity) > 0.7:
        verdetto= verdetto+1

    #print('lo score della similarità per CONCLUSION è:', sum(conclusion_similarity)/len(conclusion_similarity))
    new_row = {'file':df_original.iloc[i][0], 'results':verdetto}
    
    # Aggiungi la nuova riga al DataFrame
    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)

print(f'i risultati della similarità del file: {df_plagiated.iloc[1][0]} ')
csv_file_path = 'Similarity_Compare/result_semantic_similarity.csv'

# Salva il DataFrame nel file CSV
df_result.to_csv(csv_file_path, index=False)

print(f"DataFrame salvato con successo in: {csv_file_path}")
    
