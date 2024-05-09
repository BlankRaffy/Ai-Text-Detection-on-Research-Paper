import spacy
import tqdm
import statistics

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


plagiated_abstract_tp = df_plagiated['abstract'][0]
plagiated_intro_tp = df_plagiated['introduction'][0]
plagiated_conclusion_tp = df_plagiated['conclusion'][0]
columns = ['input_file','compare_file','abstract_score','intro_score','conclusion_score','final_score']
df_result = pd.DataFrame(columns= columns)


#compare a single file with all original one, TO IMPLEMENT ALL FILE COMPARISON
for i in tqdm.tqdm(range(len(df_original))):
    original_abstact_tp = df_original['abstract'][i]
    original_intro_tp = df_original['introduction'][i]
    original_conclusion_tp = df_original['conclusion'][i]


    abstract_similarity = []
    intro_similarity = []
    conclusion_similarity = []

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
    absract_median =  statistics.median(sorted(abstract_similarity))  
    #print(f'il valore mediano per ABSTRACT è {statistics.median(sorted(abstract_similarity))}')

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
    #print(f'il valore mediano per INTRO è {statistics.median(sorted(intro_similarity))}')
    intro_media = statistics.median(sorted(intro_similarity))

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
    #print(f'il valore mediano per CONCLUSION è {statistics.median(sorted(conclusion_similarity))}')
    conclusion_median = statistics.median(sorted(conclusion_similarity))

    new_row = {'input_file':df_plagiated.iloc[0][0],'compare_file': df_original.iloc[i][0],
            'abstract_score': absract_median, 'intro_score':intro_media,'conclusion_score':conclusion_median,
                'final_score': 0 }

    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)


csv_file_path = 'Similarity_Compare/dataset_topic_compare.csv'

df_result.to_csv(csv_file_path, index=False)

print(f"DataFrame salvato con successo in: {csv_file_path}")




   