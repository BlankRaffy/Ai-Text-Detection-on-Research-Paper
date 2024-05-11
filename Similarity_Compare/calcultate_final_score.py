import csv
import tqdm

def computed_final_score(row):
    abstract_wg = 0.4
    intro_wg = 0.2
    conclusion_wg = 0.4
    
    final_score = float(row['abstract_score']) * abstract_wg + float(row['intro_score']) * intro_wg + float(row['conclusion_score']) * conclusion_wg
    return final_score

# Input and output filenames
input_filename = 'Similarity_Compare/dataset_topic_compare.csv'
output_filename = 'Similarity_Compare/topic_with_final_score.csv'

# Open input CSV file for reading and output CSV file for writing
with open(input_filename, 'r', newline='') as input_file, open(output_filename, 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames

    # Append a new fieldname for the modified final_score
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    # Process each row in the input CSV file
    for row in tqdm.tqdm(reader):
        # Compute the new final_score
        final_score = computed_final_score(row)

        # Update the row with the new final_score
        row['final_score'] = final_score

        # Write the updated row to the output CSV file
        writer.writerow(row)

print(f"Modified data saved to '{output_filename}'")
