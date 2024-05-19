import get_text
import xml.etree.ElementTree as ET
import csv
import pandas as pd 
import tqdm
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('distiluse-base-multilingual-cased')

def text_similarity_bert(text1, text2):
    embeddings = model.encode([text1, text2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity

columns = ['input_file','compare_file','abstract_semantic_score','intro_semantic_score','conclusion_semantic_score','final_semantic_score']
df_result = pd.DataFrame(columns= columns)

# Nome del file di input
input_filename = 'Similarity_Compare/top_k_for_similarity/paper_topic_similarity_rank.csv'

# Lista per memorizzare i dati estratti
top_k_list = []

# Apertura del file CSV
with open(input_filename, mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterazione sulle righe del file
    for row in reader:
        # Estrazione dei campi desiderati
        extracted_data = {
            'input_file': row['input_file'],
            'compare_file': row['compare_file']
        }
        top_k_list.append(extracted_data)


plagiated_file_directory ='Dataset/plagiated_paper'
orginal_file_directory='Dataset/original_paper'


#LOAD ALL THE ENTRY ON THE LIST
for i in tqdm.tqdm(range(len(top_k_list))):
    plagiated_file_name = plagiated_file_directory+'/'+top_k_list[i]['input_file']
    plagiated_tree = ET.parse(plagiated_file_name)

    plagiated_abstract= get_text.extract_abstract(plagiated_tree)
    plagiated_intro = get_text.extract_intro(plagiated_tree)
    plagiated_conclusion = get_text.extract_conclusion(plagiated_tree)

    #load original file
    original_file_name = orginal_file_directory+'/'+top_k_list[i]['compare_file']
    orginal_tree = ET.parse(original_file_name)

    original_abstract= get_text.extract_abstract(orginal_tree)
    original_intro = get_text.extract_intro(orginal_tree)
    original_conclusion = get_text.extract_conclusion(orginal_tree)

    abstract_semantic_score = text_similarity_bert(plagiated_abstract, original_abstract)
    #print("Similarity Score (BERT) for abstract:", abstract_semantic_score)

    intro_semantic_score = text_similarity_bert(plagiated_intro, original_intro)
    #print("Similarity Score (BERT) for introduction:", intro_semantic_score)

    conclusion_semantic_score = text_similarity_bert(plagiated_conclusion, original_conclusion)
    #print("Similarity Score (BERT) for conclusion:", conclusion_semantic_score)

    new_row = {'input_file':top_k_list[i]['input_file'],'compare_file': top_k_list[i]['compare_file'],
                    'abstract_semantic_score': abstract_semantic_score, 
                    'intro_semantic_score':intro_semantic_score,'conclusion_semantic_score':conclusion_semantic_score,
                        'final_semantic_score': 0 }

    df_result = pd.concat([df_result, pd.DataFrame([new_row])], ignore_index=True)

csv_file_path = 'Semantic_Similarity/semantic_rank/semantic_no_final_score.csv'

df_result.to_csv(csv_file_path, index=False)

print(f"DataFrame salvato con successo in: {csv_file_path}")
