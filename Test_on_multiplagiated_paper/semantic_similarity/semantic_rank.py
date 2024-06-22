import pandas as pd

# Caricare il CSV
file_path = 'Test_on_multiplagiated_paper/semantic_similarity/semantic_on_all_file_all_part.csv'  # Sostituire con il percorso corretto del file
df = pd.read_csv(file_path)

# Raggruppare per file di input e ottenere i top 5 per punteggio di abstract
top_3_abstract_scores = df.groupby('input_file').apply(lambda x: x.nlargest(3, 'conclusion_semantic_score')).reset_index(drop=True)
top_3_abstract_scores = top_3_abstract_scores.drop(['intro_semantic_score','abstract_semantic_score'], axis=1)
# Visualizzare i risultati
print(top_3_abstract_scores)

# Per salvare i risultati in un nuovo CSV, decomentare la riga seguente
top_3_abstract_scores.to_csv('Test_on_multiplagiated_paper/semantic_similarity/semantic_rank/semantic_rank_conclusion.csv', index=False)
