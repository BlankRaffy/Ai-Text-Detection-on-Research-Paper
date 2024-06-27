import pandas as pd

# Carica il CSV in un DataFrame
data = pd.read_csv('Semantic_Similarity/semantic_rank/semantic_rank.csv')

# Funzione per trovare i primi 5 file con i punteggi massimi
def find_top_5_scores(group):
    top_abstract = group.nlargest(5, 'abstract_semantic_score')[['compare_file', 'abstract_semantic_score']]
    top_intro = group.nlargest(5, 'intro_semantic_score')[['compare_file', 'intro_semantic_score']]
    top_conclusion = group.nlargest(5, 'conclusion_semantic_score')[['compare_file', 'conclusion_semantic_score']]

    return pd.Series({
        'abstract_files': top_abstract['compare_file'].tolist(),
        'abstract_scores': top_abstract['abstract_semantic_score'].tolist(),
        'intro_files': top_intro['compare_file'].tolist(),
        'intro_scores': top_intro['intro_semantic_score'].tolist(),
        'conclusion_files': top_conclusion['compare_file'].tolist(),
        'conclusion_scores': top_conclusion['conclusion_semantic_score'].tolist()
    })

# Raggruppa i dati per 'input_file' e applica la funzione
results = data.groupby('input_file').apply(find_top_5_scores).reset_index()

# Mostra il risultato
print(results)

# Salva i risultati in un nuovo file CSV
results.to_csv('AI_Detection/results/most_similar_part_to_compute_average_precision.csv', index=False)
