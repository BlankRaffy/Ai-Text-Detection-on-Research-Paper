import pandas as pd

# Carica il file CSV
data = pd.read_csv(r'Semantic_Similarity\semantic_rank\semantic_rank_all.csv')

# Ordina i dati in base all'input_file e al final_score
data_sorted = data.sort_values(by=['input_file', 'final_semantic_score'], ascending=[True, False])

# Dizionario per tenere traccia delle prime 3 righe per ciascun input_file
top_5_rows_per_input_file = {}

k = 1
for index, row in data_sorted.iterrows():
    input_file = row['input_file']
    if input_file not in top_5_rows_per_input_file:
        top_5_rows_per_input_file[input_file] = []

    # Aggiungi la riga corrente al dizionario
    top_5_rows_per_input_file[input_file].append(row)

# Seleziona solo le prime 5 righe per ciascun input_file
result_rows = []
for input_file, rows in top_5_rows_per_input_file.items():
    result_rows.extend(rows[:k])

# Crea un nuovo DataFrame con le righe selezionate
result_df = pd.DataFrame(result_rows)

# Salva il risultato in un nuovo file CSV
result_df.to_csv(f'Semantic_Similarity\semantic_rank\semantic_final_score_top_{k}.csv', index=False)
