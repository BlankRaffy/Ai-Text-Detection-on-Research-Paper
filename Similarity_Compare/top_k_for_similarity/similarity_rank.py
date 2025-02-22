import pandas as pd

# Carica il file CSV
data = pd.read_csv(r'C:\Users\Blank\Desktop\Ai-Text-Detection-on-Research-Paper\Similarity_Compare\topic_with_final_score.csv')
k=100
# Ordina i dati in base all'input_file e al final_score
data_sorted = data.sort_values(by=['input_file', 'final_score'], ascending=[True, False])

# Dizionario per tenere traccia delle prime 5 righe per ciascun input_file
top_5_rows_per_input_file = {}

for index, row in data_sorted.iterrows():
    input_file = row['input_file']
    if input_file not in top_5_rows_per_input_file:
        top_5_rows_per_input_file[input_file] = []

    # Aggiungi la riga corrente al dizionario se ha meno di 5 righe
    if len(top_5_rows_per_input_file[input_file]) < k:
        top_5_rows_per_input_file[input_file].append(row)

# Crea un elenco delle righe selezionate
result_rows = []
for rows in top_5_rows_per_input_file.values():
    result_rows.extend(rows)

# Crea un nuovo DataFrame con le righe selezionate
result_df = pd.DataFrame(result_rows)

# Salva il risultato in un nuovo file CSV
result_df.to_csv(r'C:\Users\Blank\Desktop\Ai-Text-Detection-on-Research-Paper\Similarity_Compare\top_k_for_similarity\paper_topic_similarity_rank.csv', index=False)
