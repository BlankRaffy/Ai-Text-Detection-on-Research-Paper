

import topic_extraction
import pandas as pd
import os
import tqdm

'''
# Definisci le colonne del DataFrame
columns = ['file', 'abstract', 'introduction', 'conclusion']
df_yake = pd.DataFrame(columns=columns)

original_paper = 'Dataset/original_paper'

# Estrai tutte le parole chiave da ciascun file
for file in tqdm.tqdm(os.listdir(original_paper)):
    path = os.path.join(original_paper, file)
    abstract, intro, conclusion = topic_extraction.yake_extraction(path)
    
    # Trasforma le liste di parole chiave in stringhe separate da virgole
    abstract_str = ', '.join(abstract)
    intro_str = ', '.join(intro)
    conclusion_str = ', '.join(conclusion)
    
    # Creazione di una nuova riga per il DataFrame
    new_row = {'file': file, 'abstract': abstract_str, 'introduction': intro_str, 'conclusion': conclusion_str}
    
    # Aggiungi la nuova riga al DataFrame
    df_yake = pd.concat([df_yake, pd.DataFrame([new_row])], ignore_index=True)

# Percorso per il file CSV di output
csv_file_path = 'Topic_Extraction/topic/original_topic.csv'

# Salva il DataFrame nel file CSV
df_yake.to_csv(csv_file_path, index=False)

print(f"DataFrame salvato con successo in: {csv_file_path}")
'''

# Definisci le colonne del DataFrame
columns = ['file', 'abstract', 'introduction', 'conclusion']
df_nmf = pd.DataFrame(columns=columns)

original_paper = 'Dataset/plagiated_paper'

# Estrai tutte le parole chiave da ciascun file
for file in tqdm.tqdm(os.listdir(original_paper)):
    path = os.path.join(original_paper, file)
    abstract, intro, conclusion = topic_extraction.NMF_extraction(path)
    
    # Trasforma le liste di parole chiave in stringhe separate da virgole
    abstract_str = ', '.join(abstract)
    intro_str = ', '.join(intro)
    conclusion_str = ', '.join(conclusion)
    
    # Creazione di una nuova riga per il DataFrame
    new_row = {'file': file, 'abstract': abstract_str, 'introduction': intro_str, 'conclusion': conclusion_str}
    
    # Aggiungi la nuova riga al DataFrame
    df_nmf = pd.concat([df_nmf, pd.DataFrame([new_row])], ignore_index=True)

# Percorso per il file CSV di output
csv_file_path = 'Topic_Extraction/topic/plagiated_topic_nmf.csv'

# Salva il DataFrame nel file CSV
df_nmf.to_csv(csv_file_path, index=False)

print(f"DataFrame salvato con successo in: {csv_file_path}")