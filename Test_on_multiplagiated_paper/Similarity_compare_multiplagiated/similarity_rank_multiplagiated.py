import pandas as pd

# Read the CSV file
df = pd.read_csv('Test_on_multiplagiated_paper\Similarity_compare_multiplagiated\dataset_topic_compare_multiplagiated.csv')

# Function to get top 5 entries for a given score
def get_top_n(df, score_column, n=5):
    return df.nlargest(n, score_column)[['input_file', 'compare_file', score_column]]

# Group by 'input_file'
grouped = df.groupby('input_file')

# Lists to store top scores
top_abstracts = []
top_intros = []
top_conclusions = []

for input_file, group in grouped:
    top_abstract = get_top_n(group, 'abstract_score')
    top_intro = get_top_n(group, 'intro_score')
    top_conclusion = get_top_n(group, 'conclusion_score')
    
    top_abstracts.append(top_abstract)
    top_intros.append(top_intro)
    top_conclusions.append(top_conclusion)

# Concatenate the lists into DataFrames
top_abstracts_df = pd.concat(top_abstracts, ignore_index=True)
top_intros_df = pd.concat(top_intros, ignore_index=True)
top_conclusions_df = pd.concat(top_conclusions, ignore_index=True)

# Save the top scores to CSV files
top_abstracts_df.to_csv('top_abstract_scores.csv', index=False)
top_intros_df.to_csv('top_intro_scores.csv', index=False)
top_conclusions_df.to_csv('top_conclusion_scores.csv', index=False)

print("Top scores have been saved to CSV files.")
