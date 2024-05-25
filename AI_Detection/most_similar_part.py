import pandas as pd

# Carica il CSV in un DataFrame
data = pd.read_csv('Semantic_Similarity/semantic_rank/semantic_rank.csv')

# Funzione per trovare i file con i punteggi massimi
def find_max_scores(group):
    max_abstract = group.loc[group['abstract_semantic_score'].idxmax()]
    max_intro = group.loc[group['intro_semantic_score'].idxmax()]
    max_conclusion = group.loc[group['conclusion_semantic_score'].idxmax()]

    return pd.Series({
        'abstract_file': max_abstract['compare_file'],
        'abstract_score': max_abstract['abstract_semantic_score'],
        'intro_file': max_intro['compare_file'],
        'intro_score': max_intro['intro_semantic_score'],
        'conclusion_file': max_conclusion['compare_file'],
        'conclusion_score': max_conclusion['conclusion_semantic_score']
    })

# Raggruppa i dati per 'input_file' e applica la funzione
results = data.groupby('input_file').apply(find_max_scores).reset_index()

# Mostra il risultato
print(results)

# Salva i risultati in un nuovo file CSV
results.to_csv('AI_Detection/results/most_similar_part_for_file.csv', index=False)
