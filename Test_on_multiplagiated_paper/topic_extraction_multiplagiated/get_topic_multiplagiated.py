

import topic_extraction
import pandas as pd
import os
import tqdm

#abbiamo più modelli per estrare i file

# Definisci le colonne del DataFrame
columns = ['file', 'abstract', 'introduction', 'conclusion']
df_lsa = pd.DataFrame(columns=columns)

original_paper = 'Test_on_multiplagiated_paper\multi_plagiated_paper'

# Estrai tutte le parole chiave da ciascun file
for file in tqdm.tqdm(os.listdir(original_paper)):
    path = os.path.join(original_paper, file)
    abstract, intro, conclusion = topic_extraction.LDA_extraction(path)
    
    # Trasforma le liste di parole chiave in stringhe separate da virgole
    abstract_str = ', '.join(abstract)
    intro_str = ', '.join(intro)
    conclusion_str = ', '.join(conclusion)
    
    # Creazione di una nuova riga per il DataFrame
    new_row = {'file': file, 'abstract': abstract_str, 'introduction': intro_str, 'conclusion': conclusion_str}
    
    # Aggiungi la nuova riga al DataFrame
    df_lsa = pd.concat([df_lsa, pd.DataFrame([new_row])], ignore_index=True)

# Percorso per il file CSV di output
csv_file_path = 'Test_on_multiplagiated_paper/topic_extraction_multiplagiated/topic_extracted_for_multiplagiated_LDA.csv'

# Salva il DataFrame nel file CSV
df_lsa.to_csv(csv_file_path, index=False)

print(f"DataFrame salvato con successo in: {csv_file_path}")