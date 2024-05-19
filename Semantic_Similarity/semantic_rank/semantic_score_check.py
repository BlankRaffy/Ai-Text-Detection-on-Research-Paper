import csv
from collections import defaultdict

# Input filename
input_filename = 'Semantic_Similarity/semantic_rank/semantic_rank.csv'
count=0
# Read input CSV file
rows = []
with open(input_filename, 'r', newline='') as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        rows.append(row)

# Group rows by input_file
grouped_rows = defaultdict(list)
for row in rows:
    grouped_rows[row['input_file']].append(row)

# Check if the first compare_file matches the input_file without "_plagiated"
for input_file, group in grouped_rows.items():
    first_compare_file = group[0]['compare_file']
    input_file_without_plagiated = input_file.replace('_plagiated', '')
    
    if first_compare_file == input_file_without_plagiated:
        count += 1
        #print(f"For input_file '{input_file}', the first compare_file matches: '{first_compare_file}'")
    #else:
        #print(f"For input_file '{input_file}', the first compare_file does not match. Found: '{first_compare_file}', expected: '{input_file_without_plagiated}'")

print(f'Percentual of plagiated paper that are most similar to the orginal one: {count/174}')