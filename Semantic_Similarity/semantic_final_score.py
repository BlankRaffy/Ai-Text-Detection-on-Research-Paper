import csv
from tqdm import tqdm

def computed_final_score(row):
    abstract_wg = 0.4
    intro_wg = 0.2
    conclusion_wg = 0.4
    
    final_score = (float(row['abstract_semantic_score']) * abstract_wg +
                   float(row['intro_semantic_score']) * intro_wg +
                   float(row['conclusion_semantic_score']) * conclusion_wg)
    return final_score

# Input and output filenames
input_filename = 'Semantic_Similarity/semantic_rank/semantic_no_final_score.csv'
output_filename = 'Semantic_Similarity/semantic_rank/semantic_rank_all.csv'

# Read input CSV file and compute final scores
rows = []
with open(input_filename, 'r', newline='') as input_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames

    for row in tqdm(reader):
        # Compute the new final_score
        row['final_semantic_score'] = computed_final_score(row)
        rows.append(row)

# Sort the rows by 'file_name' and 'final_score'
rows.sort(key=lambda x: (x['input_file'], -float(x['final_semantic_score'])))

# Write sorted data to output CSV file
with open(output_filename, 'w', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Modified data saved to '{output_filename}'")
